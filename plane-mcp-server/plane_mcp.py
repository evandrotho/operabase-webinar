"""
Plane.so MCP Server
Connects Claude Code to a Plane.so instance via Model Context Protocol.
Supports all core operations: projects, work items, cycles, modules, states, labels, etc.
"""

import os
import asyncio
import json
from typing import Optional
from enum import Enum

import httpx
from pydantic import BaseModel, Field, ConfigDict
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

API_BASE_URL = os.environ.get("PLANE_API_BASE_URL", "https://plane.operabase.io/api/v1")
API_KEY = os.environ.get("PLANE_API_KEY", "")
WORKSPACE_SLUG = os.environ.get("PLANE_WORKSPACE_SLUG", "operabaseai")
CHARACTER_LIMIT = 25_000

mcp = FastMCP(
    "plane",
    instructions="Plane.so project management — read and write projects, work items, cycles, modules, and more.",
)

# ---------------------------------------------------------------------------
# Shared HTTP helpers
# ---------------------------------------------------------------------------


async def _request(
    endpoint: str,
    method: str = "GET",
    body: dict | None = None,
    params: dict | None = None,
    *,
    workspace_scoped: bool = True,
) -> dict | list:
    """Make an authenticated request to the Plane.so API."""
    if not API_KEY:
        return {"error": "PLANE_API_KEY not configured. Set the environment variable."}

    base = f"{API_BASE_URL}/workspaces/{WORKSPACE_SLUG}" if workspace_scoped else API_BASE_URL
    url = f"{base}/{endpoint.lstrip('/')}"

    headers = {
        "X-API-Key": API_KEY,
        "Content-Type": "application/json",
    }

    # Strip None values from params
    if params:
        params = {k: v for k, v in params.items() if v is not None}

    async with httpx.AsyncClient(timeout=30.0) as client:
        for attempt in range(3):
            try:
                resp = await client.request(
                    method,
                    url,
                    headers=headers,
                    json=body,
                    params=params,
                )
                if resp.status_code == 429:
                    retry_after = int(resp.headers.get("X-RateLimit-Reset", "5"))
                    await asyncio.sleep(min(retry_after, 10))
                    continue
                resp.raise_for_status()
                if resp.status_code == 204:
                    return {"success": True}
                return resp.json()
            except httpx.HTTPStatusError as e:
                return {
                    "error": f"HTTP {e.response.status_code}",
                    "detail": e.response.text[:500],
                }
            except httpx.RequestError as e:
                if attempt < 2:
                    await asyncio.sleep(2 ** attempt)
                    continue
                return {"error": f"Request failed: {str(e)}"}

    return {"error": "Max retries exceeded"}


async def _paginated_list(
    endpoint: str,
    params: dict | None = None,
    max_results: int = 100,
) -> list:
    """Fetch a paginated list endpoint, collecting up to max_results items."""
    all_items: list = []
    cursor = None
    page_params = dict(params or {})

    while len(all_items) < max_results:
        if cursor:
            page_params["cursor"] = cursor

        data = await _request(endpoint, params=page_params)

        if isinstance(data, dict) and "error" in data:
            return [data]

        # Handle paginated response
        if isinstance(data, dict) and "results" in data:
            all_items.extend(data["results"])
            cursor = data.get("next_cursor")
            if not cursor or len(data["results"]) == 0:
                break
        elif isinstance(data, list):
            all_items.extend(data)
            break
        else:
            all_items.append(data)
            break

    return all_items[:max_results]


def _truncate(text: str) -> str:
    """Truncate text to CHARACTER_LIMIT."""
    if len(text) <= CHARACTER_LIMIT:
        return text
    return text[:CHARACTER_LIMIT] + "\n\n... [truncated]"


def _format_items(items: list, title: str, fields: list[str] | None = None) -> str:
    """Format a list of items as readable markdown."""
    if not items:
        return f"## {title}\n\nNenhum item encontrado."

    if isinstance(items[0], dict) and "error" in items[0]:
        return f"## {title}\n\nErro: {items[0]['error']}"

    lines = [f"## {title}", f"Total: {len(items)}", ""]
    for item in items:
        if isinstance(item, dict):
            name = item.get("name") or item.get("comment_stripped") or item.get("comment") or str(item.get("id", ""))
            identifier = item.get("identifier", "")
            prefix = f"[{identifier}] " if identifier else ""
            lines.append(f"- **{prefix}{name}**")
            if fields:
                for f in fields:
                    val = item.get(f)
                    if val is not None:
                        lines.append(f"  - {f}: {val}")
            lines.append(f"  - id: `{item.get('id', 'N/A')}`")
        else:
            lines.append(f"- {item}")

    return _truncate("\n".join(lines))


# ===========================================================================
# TIER 1 — Core Operations (10 tools)
# ===========================================================================


# --- Projects ---

@mcp.tool()
async def plane_list_projects() -> str:
    """List all projects in the Plane.so workspace."""
    items = await _paginated_list("projects/")
    return _format_items(items, "Projetos", ["description", "total_members", "total_cycles", "total_modules"])


@mcp.tool()
async def plane_get_project(project_id: str) -> str:
    """Get details of a specific project.

    Args:
        project_id: UUID of the project
    """
    data = await _request(f"projects/{project_id}/")
    if isinstance(data, dict) and "error" in data:
        return f"Erro: {data['error']}"
    return _truncate(json.dumps(data, indent=2, default=str))


@mcp.tool()
async def plane_create_project(
    name: str,
    identifier: str,
    description: str = "",
    network: int = 2,
) -> str:
    """Create a new project in the workspace.

    Args:
        name: Project name
        identifier: Short identifier (e.g., 'WEB', 'MKT') used in work item IDs
        description: Optional project description
        network: 0 for secret, 2 for public (default: 2)
    """
    body = {
        "name": name,
        "identifier": identifier,
        "description": description,
        "network": network,
    }
    data = await _request("projects/", method="POST", body=body)
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao criar projeto: {data['error']}\n{data.get('detail', '')}"
    return f"Projeto criado com sucesso!\n- Nome: {data.get('name')}\n- ID: {data.get('id')}\n- Identifier: {data.get('identifier')}"


# --- Work Items ---

@mcp.tool()
async def plane_list_work_items(
    project_id: str,
    state: Optional[str] = None,
    priority: Optional[str] = None,
    assignee: Optional[str] = None,
    label: Optional[str] = None,
    expand: Optional[str] = None,
    limit: int = 50,
) -> str:
    """List work items (tasks) in a project.

    Args:
        project_id: UUID of the project
        state: Filter by state UUID
        priority: Filter by priority: urgent, high, medium, low, none
        assignee: Filter by assignee UUID
        label: Filter by label UUID
        expand: Comma-separated fields to expand: assignees, state, labels, module
        limit: Max results (default 50, max 100)
    """
    params = {
        "state": state,
        "priority": priority,
        "assignee": assignee,
        "label": label,
        "expand": expand,
    }
    items = await _paginated_list(
        f"projects/{project_id}/issues/",
        params=params,
        max_results=min(limit, 100),
    )
    return _format_items(
        items,
        "Work Items",
        ["priority", "state", "start_date", "target_date", "assignees"],
    )


@mcp.tool()
async def plane_get_work_item(
    project_id: str,
    work_item_id: str,
    expand: Optional[str] = None,
) -> str:
    """Get details of a specific work item.

    Args:
        project_id: UUID of the project
        work_item_id: UUID of the work item
        expand: Comma-separated fields to expand: assignees, state, labels, module
    """
    params = {"expand": expand} if expand else None
    data = await _request(
        f"projects/{project_id}/issues/{work_item_id}/",
        params=params,
    )
    if isinstance(data, dict) and "error" in data:
        return f"Erro: {data['error']}"
    return _truncate(json.dumps(data, indent=2, default=str))


@mcp.tool()
async def plane_create_work_item(
    project_id: str,
    name: str,
    description_html: str = "",
    state: Optional[str] = None,
    priority: str = "none",
    assignees: Optional[list[str]] = None,
    labels: Optional[list[str]] = None,
    parent: Optional[str] = None,
    module: Optional[str] = None,
    start_date: Optional[str] = None,
    target_date: Optional[str] = None,
    estimate_point: Optional[int] = None,
) -> str:
    """Create a new work item (task) in a project.

    Args:
        project_id: UUID of the project
        name: Work item name/title
        description_html: HTML-formatted description
        state: State UUID
        priority: Priority level: urgent, high, medium, low, none
        assignees: List of user UUIDs to assign
        labels: List of label UUIDs
        parent: Parent work item UUID (for sub-tasks)
        module: Module UUID to add this item to
        start_date: Start date in YYYY-MM-DD format
        target_date: Target/due date in YYYY-MM-DD format
        estimate_point: Estimate points (0-7)
    """
    body: dict = {"name": name, "priority": priority}
    if description_html:
        body["description_html"] = description_html
    if state:
        body["state"] = state
    if assignees:
        body["assignees"] = assignees
    if labels:
        body["labels"] = labels
    if parent:
        body["parent"] = parent
    if module:
        body["module"] = module
    if start_date:
        body["start_date"] = start_date
    if target_date:
        body["target_date"] = target_date
    if estimate_point is not None:
        body["estimate_point"] = estimate_point

    data = await _request(f"projects/{project_id}/issues/", method="POST", body=body)
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao criar work item: {data['error']}\n{data.get('detail', '')}"
    return (
        f"Work item criado!\n"
        f"- Nome: {data.get('name')}\n"
        f"- ID: {data.get('id')}\n"
        f"- Identifier: {data.get('identifier', 'N/A')}\n"
        f"- Priority: {data.get('priority', 'none')}"
    )


@mcp.tool()
async def plane_update_work_item(
    project_id: str,
    work_item_id: str,
    name: Optional[str] = None,
    description_html: Optional[str] = None,
    state: Optional[str] = None,
    priority: Optional[str] = None,
    assignees: Optional[list[str]] = None,
    labels: Optional[list[str]] = None,
    parent: Optional[str] = None,
    start_date: Optional[str] = None,
    target_date: Optional[str] = None,
    estimate_point: Optional[int] = None,
) -> str:
    """Update an existing work item. Only provided fields are changed.

    Args:
        project_id: UUID of the project
        work_item_id: UUID of the work item to update
        name: New name/title
        description_html: New HTML description
        state: New state UUID
        priority: New priority: urgent, high, medium, low, none
        assignees: New list of assignee UUIDs (replaces current)
        labels: New list of label UUIDs (replaces current)
        parent: New parent work item UUID
        start_date: New start date (YYYY-MM-DD)
        target_date: New target date (YYYY-MM-DD)
        estimate_point: New estimate points (0-7)
    """
    body: dict = {}
    if name is not None:
        body["name"] = name
    if description_html is not None:
        body["description_html"] = description_html
    if state is not None:
        body["state"] = state
    if priority is not None:
        body["priority"] = priority
    if assignees is not None:
        body["assignees"] = assignees
    if labels is not None:
        body["labels"] = labels
    if parent is not None:
        body["parent"] = parent
    if start_date is not None:
        body["start_date"] = start_date
    if target_date is not None:
        body["target_date"] = target_date
    if estimate_point is not None:
        body["estimate_point"] = estimate_point

    if not body:
        return "Nenhum campo fornecido para atualizar."

    data = await _request(
        f"projects/{project_id}/issues/{work_item_id}/",
        method="PATCH",
        body=body,
    )
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao atualizar: {data['error']}\n{data.get('detail', '')}"
    return f"Work item atualizado!\n- Nome: {data.get('name')}\n- ID: {data.get('id')}"


@mcp.tool()
async def plane_delete_work_item(
    project_id: str,
    work_item_id: str,
) -> str:
    """Delete a work item permanently.

    Args:
        project_id: UUID of the project
        work_item_id: UUID of the work item to delete
    """
    data = await _request(
        f"projects/{project_id}/issues/{work_item_id}/",
        method="DELETE",
    )
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao deletar work item: {data['error']}\n{data.get('detail', '')}"
    return f"Work item deletado com sucesso!\n- ID: {work_item_id}"


@mcp.tool()
async def plane_search_work_items(
    project_id: str,
    query: str,
    limit: int = 20,
) -> str:
    """Search work items by text in a project.

    Args:
        project_id: UUID of the project
        query: Search text
        limit: Max results (default 20)
    """
    params = {"search": query}
    items = await _paginated_list(
        f"projects/{project_id}/issues/",
        params=params,
        max_results=min(limit, 100),
    )
    return _format_items(items, f"Busca: '{query}'", ["priority", "state", "target_date"])


# --- States ---

@mcp.tool()
async def plane_list_states(project_id: str) -> str:
    """List all workflow states for a project.

    Args:
        project_id: UUID of the project
    """
    items = await _paginated_list(f"projects/{project_id}/states/")
    return _format_items(items, "Estados", ["color", "group", "sequence"])


@mcp.tool()
async def plane_list_labels(project_id: str) -> str:
    """List all labels for a project.

    Args:
        project_id: UUID of the project
    """
    items = await _paginated_list(f"projects/{project_id}/labels/")
    return _format_items(items, "Labels", ["color", "description"])


# ===========================================================================
# TIER 2 — Organization & Planning (8 tools)
# ===========================================================================


# --- Cycles ---

@mcp.tool()
async def plane_list_cycles(project_id: str) -> str:
    """List all cycles (sprints) in a project.

    Args:
        project_id: UUID of the project
    """
    items = await _paginated_list(f"projects/{project_id}/cycles/")
    return _format_items(items, "Ciclos", ["start_date", "end_date", "owned_by"])


@mcp.tool()
async def plane_create_cycle(
    project_id: str,
    name: str,
    description: str = "",
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
) -> str:
    """Create a new cycle (sprint) in a project.

    Args:
        project_id: UUID of the project
        name: Cycle name
        description: Optional description
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
    """
    body: dict = {"name": name}
    if description:
        body["description"] = description
    if start_date:
        body["start_date"] = start_date
    if end_date:
        body["end_date"] = end_date

    data = await _request(f"projects/{project_id}/cycles/", method="POST", body=body)
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao criar ciclo: {data['error']}\n{data.get('detail', '')}"
    return f"Ciclo criado!\n- Nome: {data.get('name')}\n- ID: {data.get('id')}"


@mcp.tool()
async def plane_add_items_to_cycle(
    project_id: str,
    cycle_id: str,
    work_item_ids: list[str],
) -> str:
    """Add work items to a cycle.

    Args:
        project_id: UUID of the project
        cycle_id: UUID of the cycle
        work_item_ids: List of work item UUIDs to add
    """
    body = {"issues": work_item_ids}
    data = await _request(
        f"projects/{project_id}/cycles/{cycle_id}/cycle-issues/",
        method="POST",
        body=body,
    )
    if isinstance(data, dict) and "error" in data:
        return f"Erro: {data['error']}\n{data.get('detail', '')}"
    return f"{len(work_item_ids)} item(s) adicionado(s) ao ciclo."


# --- Modules ---

@mcp.tool()
async def plane_list_modules(project_id: str) -> str:
    """List all modules in a project.

    Args:
        project_id: UUID of the project
    """
    items = await _paginated_list(f"projects/{project_id}/modules/")
    return _format_items(items, "Modulos", ["status", "start_date", "target_date", "lead"])


@mcp.tool()
async def plane_create_module(
    project_id: str,
    name: str,
    description: str = "",
    status: str = "backlog",
    start_date: Optional[str] = None,
    target_date: Optional[str] = None,
    lead: Optional[str] = None,
    members: Optional[list[str]] = None,
) -> str:
    """Create a new module in a project.

    Args:
        project_id: UUID of the project
        name: Module name
        description: Optional description
        status: Module status: backlog, planned, in-progress, paused, completed, cancelled
        start_date: Start date (YYYY-MM-DD)
        target_date: Target date (YYYY-MM-DD)
        lead: Lead user UUID
        members: List of member UUIDs
    """
    body: dict = {"name": name, "status": status}
    if description:
        body["description"] = description
    if start_date:
        body["start_date"] = start_date
    if target_date:
        body["target_date"] = target_date
    if lead:
        body["lead"] = lead
    if members:
        body["members"] = members

    data = await _request(f"projects/{project_id}/modules/", method="POST", body=body)
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao criar modulo: {data['error']}\n{data.get('detail', '')}"
    return f"Modulo criado!\n- Nome: {data.get('name')}\n- ID: {data.get('id')}\n- Status: {data.get('status')}"


@mcp.tool()
async def plane_add_items_to_module(
    project_id: str,
    module_id: str,
    work_item_ids: list[str],
) -> str:
    """Add work items to a module.

    Args:
        project_id: UUID of the project
        module_id: UUID of the module
        work_item_ids: List of work item UUIDs to add
    """
    body = {"issues": work_item_ids}
    data = await _request(
        f"projects/{project_id}/modules/{module_id}/module-issues/",
        method="POST",
        body=body,
    )
    if isinstance(data, dict) and "error" in data:
        return f"Erro: {data['error']}\n{data.get('detail', '')}"
    return f"{len(work_item_ids)} item(s) adicionado(s) ao modulo."


# --- Members ---

@mcp.tool()
async def plane_list_project_members(project_id: str) -> str:
    """List all members of a project.

    Args:
        project_id: UUID of the project
    """
    items = await _paginated_list(f"projects/{project_id}/members/")
    return _format_items(items, "Membros do Projeto", ["role", "member"])


@mcp.tool()
async def plane_list_workspace_members() -> str:
    """List all members of the workspace."""
    items = await _paginated_list("members/")
    return _format_items(items, "Membros do Workspace", ["role", "member"])


# ===========================================================================
# TIER 3 — Details & Analysis (7 tools)
# ===========================================================================


@mcp.tool()
async def plane_list_comments(
    project_id: str,
    work_item_id: str,
) -> str:
    """List comments on a work item.

    Args:
        project_id: UUID of the project
        work_item_id: UUID of the work item
    """
    items = await _paginated_list(
        f"projects/{project_id}/issues/{work_item_id}/comments/"
    )
    return _format_items(items, "Comentarios", ["comment_stripped", "created_at", "created_by"])


@mcp.tool()
async def plane_create_comment(
    project_id: str,
    work_item_id: str,
    comment_html: str,
    access: str = "INTERNAL",
) -> str:
    """Add a comment to a work item.

    Args:
        project_id: UUID of the project
        work_item_id: UUID of the work item
        comment_html: Comment in HTML format (e.g., '<p>My comment</p>')
        access: INTERNAL (default) or EXTERNAL
    """
    body = {"comment_html": comment_html, "access": access}
    data = await _request(
        f"projects/{project_id}/issues/{work_item_id}/comments/",
        method="POST",
        body=body,
    )
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao criar comentario: {data['error']}\n{data.get('detail', '')}"
    return f"Comentario adicionado!\n- ID: {data.get('id')}"


@mcp.tool()
async def plane_list_activity(
    project_id: str,
    work_item_id: str,
) -> str:
    """List activity/change history of a work item.

    Args:
        project_id: UUID of the project
        work_item_id: UUID of the work item
    """
    items = await _paginated_list(
        f"projects/{project_id}/issues/{work_item_id}/activities/"
    )
    lines = ["## Historico de Atividades", ""]
    for item in items:
        if isinstance(item, dict) and "error" not in item:
            comment = item.get("comment", "")
            field = item.get("field", "")
            old_val = item.get("old_value", "")
            new_val = item.get("new_value", "")
            created = item.get("created_at", "")
            if field:
                lines.append(f"- **{field}**: `{old_val}` -> `{new_val}` ({created})")
            else:
                lines.append(f"- {comment} ({created})")
        elif isinstance(item, dict):
            return f"Erro: {item['error']}"
    if len(lines) == 2:
        lines.append("Nenhuma atividade encontrada.")
    return _truncate("\n".join(lines))


@mcp.tool()
async def plane_create_label(
    project_id: str,
    name: str,
    color: str = "#6366f1",
    description: str = "",
) -> str:
    """Create a new label in a project.

    Args:
        project_id: UUID of the project
        name: Label name
        color: Hex color code (default: '#6366f1' indigo)
        description: Optional description
    """
    body: dict = {"name": name, "color": color}
    if description:
        body["description"] = description

    data = await _request(f"projects/{project_id}/labels/", method="POST", body=body)
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao criar label: {data['error']}\n{data.get('detail', '')}"
    return f"Label criada!\n- Nome: {data.get('name')}\n- Cor: {data.get('color')}\n- ID: {data.get('id')}"


@mcp.tool()
async def plane_create_state(
    project_id: str,
    name: str,
    color: str = "#6366f1",
) -> str:
    """Create a new workflow state in a project.

    Args:
        project_id: UUID of the project
        name: State name (e.g., 'Em Revisao', 'Bloqueado')
        color: Hex color code (default: '#6366f1')
    """
    body = {"name": name, "color": color}
    data = await _request(f"projects/{project_id}/states/", method="POST", body=body)
    if isinstance(data, dict) and "error" in data:
        return f"Erro ao criar estado: {data['error']}\n{data.get('detail', '')}"
    return f"Estado criado!\n- Nome: {data.get('name')}\n- Cor: {data.get('color')}\n- ID: {data.get('id')}"


@mcp.tool()
async def plane_list_pages(project_id: Optional[str] = None) -> str:
    """List all pages (wiki/docs) in a project or the workspace.

    Args:
        project_id: UUID of the project (recommended). If omitted, lists workspace-level pages.
    """
    if project_id:
        items = await _paginated_list(f"projects/{project_id}/pages/")
    else:
        items = await _paginated_list("pages/")

    # Check for API limitation (pages LIST not available in current Plane version)
    if items and isinstance(items[0], dict) and "error" in items[0]:
        error_detail = items[0].get("detail", "")
        if "404" in str(items[0].get("error", "")):
            return (
                "## Paginas\n\n"
                "**Limitacao da API:** O endpoint de listagem de paginas nao esta disponivel "
                "nesta versao do Plane.so. Use a interface web do Plane para ver e gerenciar paginas.\n\n"
                "**Alternativa:** Use `plane_get_page` com o UUID da pagina para acessar paginas individualmente."
            )
    return _format_items(items, "Paginas", ["created_at", "updated_at"])


@mcp.tool()
async def plane_get_page(
    page_id: str,
    project_id: Optional[str] = None,
) -> str:
    """Get a specific page by ID.

    Args:
        page_id: UUID of the page
        project_id: UUID of the project. If omitted, fetches workspace-level page.
    """
    if project_id:
        data = await _request(f"projects/{project_id}/pages/{page_id}/")
    else:
        data = await _request(f"pages/{page_id}/")
    if isinstance(data, dict) and "error" in data:
        return f"Erro: {data['error']}\n{data.get('detail', '')}"
    return _truncate(json.dumps(data, indent=2, default=str))


@mcp.tool()
async def plane_create_page(
    name: str,
    description_html: str = "",
    project_id: Optional[str] = None,
) -> str:
    """Create a new page (wiki/doc) in a project or the workspace.

    Args:
        name: Page title
        description_html: Page content in HTML format
        project_id: UUID of the project (recommended). If omitted, creates at workspace level.
    """
    body: dict = {"name": name}
    if description_html:
        body["description_html"] = description_html

    endpoint = f"projects/{project_id}/pages/" if project_id else "pages/"
    data = await _request(endpoint, method="POST", body=body)
    if isinstance(data, dict) and "error" in data:
        error_str = str(data.get("error", ""))
        if "404" in error_str:
            return (
                "Erro ao criar pagina: endpoint nao disponivel nesta versao do Plane.so.\n"
                "**Solucao:** Crie a pagina manualmente pela interface web do Plane.so."
            )
        return f"Erro ao criar pagina: {data['error']}\n{data.get('detail', '')}"
    return f"Pagina criada!\n- Nome: {data.get('name', name)}\n- ID: {data.get('id')}"


# ===========================================================================
# TIER 4 — Composite Dashboard Tool
# ===========================================================================


@mcp.tool()
async def plane_project_dashboard(project_id: str) -> str:
    """Generate a consolidated dashboard for a project.
    Fetches project details, work items, cycles, modules, and states in parallel.

    Args:
        project_id: UUID of the project
    """
    # Fetch data in parallel
    project_task = _request(f"projects/{project_id}/")
    items_task = _paginated_list(f"projects/{project_id}/issues/", max_results=100)
    states_task = _paginated_list(f"projects/{project_id}/states/")
    cycles_task = _paginated_list(f"projects/{project_id}/cycles/")
    modules_task = _paginated_list(f"projects/{project_id}/modules/")

    project, items, states, cycles, modules = await asyncio.gather(
        project_task, items_task, states_task, cycles_task, modules_task
    )

    # Build state name map
    state_map: dict[str, str] = {}
    if isinstance(states, list):
        for s in states:
            if isinstance(s, dict) and "id" in s:
                state_map[s["id"]] = s.get("name", "?")

    # Count items by state
    state_counts: dict[str, int] = {}
    overdue: list[dict] = []
    upcoming: list[dict] = []
    total = 0

    from datetime import date

    today = date.today().isoformat()

    if isinstance(items, list):
        for item in items:
            if not isinstance(item, dict) or "error" in item:
                continue
            total += 1
            sid = item.get("state", "")
            sname = state_map.get(sid, sid[:8] if sid else "Sem estado")
            state_counts[sname] = state_counts.get(sname, 0) + 1

            target = item.get("target_date")
            item_name = item.get("name", "?")
            item_id = item.get("identifier", item.get("id", ""))

            if target and target < today and sname.lower() not in ("done", "concluido", "concluída", "cancelled"):
                overdue.append({"name": item_name, "id": item_id, "target_date": target, "state": sname})
            elif target and target >= today and target <= _add_days(today, 7):
                upcoming.append({"name": item_name, "id": item_id, "target_date": target, "state": sname})

    # Build dashboard
    lines = []
    proj_name = project.get("name", "?") if isinstance(project, dict) else "?"
    lines.append(f"# Dashboard: {proj_name}")
    lines.append(f"\n**Total de work items:** {total}")
    lines.append("")

    # State summary
    lines.append("## Distribuicao por Estado")
    lines.append("")
    lines.append("| Estado | Quantidade | % |")
    lines.append("|--------|-----------|---|")
    for sname, count in sorted(state_counts.items(), key=lambda x: -x[1]):
        pct = round(count / total * 100) if total > 0 else 0
        lines.append(f"| {sname} | {count} | {pct}% |")

    # Overdue
    lines.append("")
    if overdue:
        lines.append(f"## Tarefas Atrasadas ({len(overdue)})")
        lines.append("")
        for o in sorted(overdue, key=lambda x: x["target_date"]):
            lines.append(f"- **[{o['id']}] {o['name']}** — prazo: {o['target_date']} (estado: {o['state']})")
    else:
        lines.append("## Tarefas Atrasadas\nNenhuma tarefa atrasada!")

    # Upcoming
    lines.append("")
    if upcoming:
        lines.append(f"## Proximos 7 dias ({len(upcoming)})")
        lines.append("")
        for u in sorted(upcoming, key=lambda x: x["target_date"]):
            lines.append(f"- **[{u['id']}] {u['name']}** — prazo: {u['target_date']} (estado: {u['state']})")
    else:
        lines.append("## Proximos 7 dias\nNenhuma tarefa com prazo nos proximos 7 dias.")

    # Cycles
    lines.append("")
    if isinstance(cycles, list) and cycles and not (isinstance(cycles[0], dict) and "error" in cycles[0]):
        lines.append(f"## Ciclos ({len(cycles)})")
        lines.append("")
        for c in cycles:
            if isinstance(c, dict):
                lines.append(f"- **{c.get('name', '?')}** ({c.get('start_date', '?')} a {c.get('end_date', '?')})")
    else:
        lines.append("## Ciclos\nNenhum ciclo configurado.")

    # Modules
    lines.append("")
    if isinstance(modules, list) and modules and not (isinstance(modules[0], dict) and "error" in modules[0]):
        lines.append(f"## Modulos ({len(modules)})")
        lines.append("")
        for m in modules:
            if isinstance(m, dict):
                lines.append(f"- **{m.get('name', '?')}** — status: {m.get('status', '?')}")
    else:
        lines.append("## Modulos\nNenhum modulo configurado.")

    return _truncate("\n".join(lines))


def _add_days(date_str: str, days: int) -> str:
    """Add days to a YYYY-MM-DD date string."""
    from datetime import date as dt_date, timedelta
    d = dt_date.fromisoformat(date_str)
    return (d + timedelta(days=days)).isoformat()


# ===========================================================================
# Entry point
# ===========================================================================

if __name__ == "__main__":
    mcp.run()
