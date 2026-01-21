import subprocess
result = subprocess.run("python -m pip install fpdf", shell=True, capture_output=True, text=True)
if result.stdout:
    print("Output:\n", result.stdout)
if result.stderr:
    print("Error:\n", result.stderr)
result = subprocess.run("python -m pip install mysql.connector", shell=True, capture_output=True, text=True)
if result.stdout:
    print("Output:\n", result.stdout)
if result.stderr:
    print("Error:\n", result.stderr)