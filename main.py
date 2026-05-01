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
    iterations = int(os.getenv("AGENTIC_LOOP_STEPS", 1))
    for i in range(iterations):
        context = {}
        print_progress(i, iterations, 1)
        await step_1_create_story.execute_step_1()
        print_progress(i, iterations, 2)
        await step_2_get_spec_name.execute_step_2(context)
        print_progress(i, iterations, 3)
        await step_3_implement_story.execute_step_3(context)
        print_progress(i, iterations, 4)
        await step_4_code_review.execute_step_4(context)
        print_progress(i, iterations, 5)
        await step_5_testing.execute_step_5(context)
        print_progress(i, iterations, 6)
        await step_6_commit_and_push.execute_step_6(context)

def print_progress(iteration, total_iterations, step):
    print("---------------------------------------------")
    print(f"Iteration {iteration}/{total_iterations}")
    print(f"Step {step}")
    print("---------------------------------------------")

if __name__ == "__main__":
    asyncio.run(main())
