import asyncio
import step_1_create_story
import step_2_get_spec_name
import step_3_implement_story

async def main():
    context = {}
    # await step_1_create_story.execute_step_1()
    await step_2_get_spec_name.execute_step_2(context)
    await step_3_implement_story.execute_step_3(context)


if __name__ == "__main__":
    asyncio.run(main())
