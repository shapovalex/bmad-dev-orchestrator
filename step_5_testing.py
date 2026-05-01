import agent_executor

async def execute_step_5(context):

    PROMPT=f"""/bmad-agent-dev
    Current specification is @{context['spec_file']}
    Run the application and verify that everything works as expected. Perform a quick regression testing for APIs and UI.
    You can use Chrome to test UI.
    Verify UV_PROJECT_ENVIRONMENT variable and set it up to correct value before executing any commands.
    Verify test coverage and linter after fixing issues, fix broken tests and linter even if they were broken by another ticket implementation.
    """

    await agent_executor.execute_agent(prompt=PROMPT)
