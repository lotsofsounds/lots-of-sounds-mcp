"""Use the Lots of Sounds MCP server as a tool source for an OpenAI agent."""
import asyncio
import os

from agents import Agent, Runner
from agents.mcp import MCPServerStreamableHttp


async def main() -> None:
    async with MCPServerStreamableHttp(
        params={
            "url": "https://api.lotsofsounds.com/mcp",
            "headers": {"x-api-key": os.environ["LOS_API_KEY"]},
        }
    ) as sounds:
        agent = Agent(
            name="Sound assistant",
            instructions="Find CC0 sound effects. Search with short keywords and use max_duration for short sounds.",
            mcp_servers=[sounds],
        )
        result = await Runner.run(agent, "Find a short UI success sound")
        print(result.final_output)


asyncio.run(main())
