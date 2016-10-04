import subprocess
subprocess.call(["python", "readFile.py", "row_text.txt" ])
tt =subprocess.check_output(["python", "readFile.py", "row_text.txt" ])
print tt
t2 = subprocess.Popen(["python", "readFile.py", "row_text.txt" ])
