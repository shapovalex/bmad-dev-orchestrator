import agent_executor

async def execute_step_1():

    PROMPT="""/bmad-create-story
    """

    await agent_executor.execute_agent(prompt=PROMPT)
