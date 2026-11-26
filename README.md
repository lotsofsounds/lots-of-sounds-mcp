# Lots of Sounds MCP server

[![Lots of Sounds MCP connector](https://glama.ai/mcp/connectors/com.lotsofsounds/mcp/badges/score.svg)](https://glama.ai/mcp/connectors/com.lotsofsounds/mcp)

Give Claude, Cursor, ChatGPT or any [Model Context Protocol](https://modelcontextprotocol.io) client access to **12,000+ CC0 sound effects** from [Lots of Sounds](https://www.lotsofsounds.com).

This repo holds setup guides and example prompts for the **hosted** MCP server. There is nothing to install or run yourself.

| | |
|---|---|
| Endpoint | `https://api.lotsofsounds.com/mcp` |
| Transport | Streamable HTTP (stateless) |
| Auth | `x-api-key` header ([get a key](https://www.lotsofsounds.com/dashboard/api-keys), Pro or Enterprise plan) |
| Free tool | `browse_samples` works with no key |
| Sound licence | CC0 1.0: free for commercial use, no attribution required |

## Tools

| Tool | What it does | Needs a key |
|------|--------------|-------------|
| `browse_samples` | Free CC0 sample sounds | No |
| `search_sounds` | Keyword search with tag, category and duration filters | Yes |
| `get_sound` | Full metadata for one sound | Yes |
| `download_sound` | Signed MP3 download URL (expires after 1 hour) | Yes |

Search is a keyword match on sound names and descriptions, not semantic search. Your assistant turns a request into short keywords and filters for you.

## Example prompts

| You say | The assistant calls |
|---------|---------------------|
| "Find me a cinematic boom" | `search_sounds({ q: "boom", tags: ["cinematic"] })` |
| "Find five funny sounds for this video" | `search_sounds({ q: "funny", limit: 5 })` |
| "Find a short UI success sound" | `search_sounds({ q: "success", max_duration: 2 })` |
| "Download the second one" | `download_sound({ id: "fs-..." })` |

## Setup

### Claude Code

```bash
claude mcp add lotsofsounds --transport http https://api.lotsofsounds.com/mcp \
  --header "x-api-key: los_your_key"
```

### Cursor, Windsurf, VS Code

Add this to `~/.cursor/mcp.json` (or your client's MCP config). See [`configs/cursor.json`](configs/cursor.json).

```json
{
  "mcpServers": {
    "lotsofsounds": {
      "url": "https://api.lotsofsounds.com/mcp",
      "headers": { "x-api-key": "los_your_key" }
    }
  }
}
```

### Claude Desktop

Claude Desktop connects to remote servers through `mcp-remote`. See [`configs/claude_desktop_config.json`](configs/claude_desktop_config.json).

### Cline

See [`llms-install.md`](llms-install.md) for one-step Streamable HTTP setup in `cline_mcp_settings.json`.

### OpenAI Agents SDK

See [`configs/openai_agents.py`](configs/openai_agents.py).

## Links

- Full MCP guide: https://www.lotsofsounds.com/docs/mcp
- Developer hub: https://www.lotsofsounds.com/developers
- REST API examples: https://github.com/lotsofsounds/lots-of-sounds-api-examples
- OpenAPI spec: https://www.lotsofsounds.com/openapi.json
- Licence of the sounds: https://www.lotsofsounds.com/license

The configs and docs in this repo are MIT licensed.
