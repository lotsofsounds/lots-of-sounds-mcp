# Installing Lots of Sounds MCP

Lots of Sounds is a hosted, remote Streamable HTTP MCP server. There is nothing to clone, build, or run locally.

- Endpoint: `https://api.lotsofsounds.com/mcp`
- Transport: `streamableHttp` (`http`)
- Free tier: `browse_samples` works without an API key.
- Paid tier: `search_sounds`, `get_sound`, and `download_sound` require a Pro or Enterprise key (`x-api-key` header) from https://www.lotsofsounds.com/dashboard/api-keys.

## Cline (`cline_mcp_settings.json`)

Add the following entry under `mcpServers` in `cline_mcp_settings.json` (the `headers` field is optional if you only need `browse_samples`):

```json
{
  "mcpServers": {
    "lotsofsounds": {
      "url": "https://api.lotsofsounds.com/mcp",
      "type": "streamableHttp",
      "headers": {
        "x-api-key": "los_your_key"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```
