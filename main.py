import asyncio
import step_1_create_story

async def main():
    await step_1_create_story.execute_step_1()


if __name__ == "__main__":
    asyncio.run(main())
