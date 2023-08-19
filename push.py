import subprocess
import os

subprocess.run(
    "push.bat", shell=True, env=os.environ.copy()
)
