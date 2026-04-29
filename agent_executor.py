from dotenv import load_dotenv
from pathlib import Path
from claude_agent_sdk import query, ClaudeAgentOptions, ResultMessage, StreamEvent
import os

load_dotenv()

FOLDER = Path("/Users/oleksii/IdeaProjects/claude-sdk-exp")

async def execute_agent(prompt) -> None:
    folder = os.getenv("BMAD_PROJECT_FOLDER")
    print(f"Working directory: {folder}")
    print(f"Prompt: {prompt}\n")
    print("─" * 60)

    options = ClaudeAgentOptions(
        cwd=str(folder),
        allowed_tools=["Read", "Write", "Edit", "Bash", "Glob", "Grep"],
        include_partial_messages=True,
    )

    async for message in query(prompt=prompt, options=options):
        if isinstance(message, StreamEvent):
            event = message.event
            if event.get("type") == "content_block_delta":
                delta = event.get("delta", {})
                if delta.get("type") == "text_delta":
                    print(delta.get("text", ""), end="", flush=True)
        elif isinstance(message, ResultMessage):
            print(f"\n{'─' * 60}")
            cost = message.total_cost_usd or 0.0
            print(f"Done. Cost: ${cost:.4f} | Turns: {message.num_turns}")
