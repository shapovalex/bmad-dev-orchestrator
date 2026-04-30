import agent_executor

async def execute_step_4(context):

    PROMPT=f"""/bmad-code-review
    Review and automatically without asking fix all issues including minor for @{context['spec_file']}.
    Verify UV_PROJECT_ENVIRONMENT variable and set it up to correct value before executing any commands.
    Verify test coverage and linter after fixing issues, fix broken tests and linter even if they were broken by another ticket implementation.
    """

    await agent_executor.execute_agent(prompt=PROMPT)
