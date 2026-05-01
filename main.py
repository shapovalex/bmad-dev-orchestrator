import asyncio
import step_1_create_story
import step_2_get_spec_name
import step_3_implement_story
import step_4_code_review
import step_5_testing
import step_6_commit_and_push

async def main():
    context = {}
    # await step_1_create_story.execute_step_1()
    await step_2_get_spec_name.execute_step_2(context)
    # await step_3_implement_story.execute_step_3(context)
    # await step_4_code_review.execute_step_4(context)
    # await step_5_testing.execute_step_5(context)
    await step_6_commit_and_push.execute_step_6(context)

if __name__ == "__main__":
    asyncio.run(main())
