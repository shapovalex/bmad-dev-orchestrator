import asyncio
import os

import step_1_create_story
import step_2_get_spec_name
import step_3_implement_story
import step_4_code_review
import step_5_testing
import step_6_commit_and_push

from dotenv import load_dotenv
load_dotenv()

async def main():
    steps = int(os.getenv("AGENTIC_LOOP_STEPS", 1))
    for i in range(steps):
        print("----------------------------------")
        print(f"Performing step {i+1}/{steps}")
        print("----------------------------------")
        context = {}
        await step_1_create_story.execute_step_1()
        await step_2_get_spec_name.execute_step_2(context)
        await step_3_implement_story.execute_step_3(context)
        await step_4_code_review.execute_step_4(context)
        await step_5_testing.execute_step_5(context)
        await step_6_commit_and_push.execute_step_6(context)

if __name__ == "__main__":
    asyncio.run(main())
