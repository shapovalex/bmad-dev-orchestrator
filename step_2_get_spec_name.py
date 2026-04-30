import os
import git_utils

async def execute_step_2(context):
    files = git_utils.get_uncommitted_files()
    files = [os.path.basename(f) for f in files]
    files = [f for f in files if f.endswith(".md") and f[0].isdigit()]
    if len(files) == 0:
        raise Exception("No spec file identified")
    context["spec_file"] = files[0]
    print(f"Context={context}")