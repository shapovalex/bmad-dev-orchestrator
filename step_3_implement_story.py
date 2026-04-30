import agent_executor

async def execute_step_3(context):

    PROMPT=f"""/bmad-dev-story
    Implement story @{context['spec_file']}
    Verify UV_PROJECT_ENVIRONMENT variable and set it up to correct value before executing any commands
    """

    await agent_executor.execute_agent(prompt=PROMPT)
