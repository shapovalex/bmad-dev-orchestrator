import agent_executor

async def execute_step_6(context):

    PROMPT=f"""Commit and push all changes
    """

    await agent_executor.execute_agent(prompt=PROMPT)
