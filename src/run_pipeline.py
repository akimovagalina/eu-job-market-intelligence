import subprocess
import sys

print("STARTING JOB MARKET PIPELINE\n")

scripts = [
    "src/collect_data.py",
    "src/clean_jobs.py",
    "src/analyze_jobs.py"
]

for script in scripts:

    print(f"Running {script}...")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        print(f"Error while running {script}")
        break

print("\nPipeline finished!")