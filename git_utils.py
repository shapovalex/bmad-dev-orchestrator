import subprocess
from dotenv import load_dotenv
import os

load_dotenv()

def get_uncommitted_files() -> list[str]:
    folder = os.getenv("BMAD_PROJECT_FOLDER")
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=True,
    )
    files = []
    for line in result.stdout.splitlines():
        if line.strip():
            files.append(line[3:])
    return files
