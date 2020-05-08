import subprocess
import sys
import re

if len(sys.argv) is not 2:
	print("Usage: yarn.py <name of file>")
	exit()

command = "strings " + sys.argv[1]
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, errors = process.communicate()

# probably important things 
output = output.decode()
print("Any string starting with 2 letters, length of 5+\n")
for line in output.split("\n"):
	if re.search(r"^[A-Za-z]{2}.*", line):
		if len(line) > 5:
			print(line)

# probably important things 
for line in output.split("\n"):
	if re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", line):
		print("POSSIBLE IP ADDRESS: " + line)
	
	if re.search(r"[Cc]:\\", line):
		print("POSSIBLE WINDOWS PATH: " + line)

	if re.search(r"(https)|(http)", line):
		print("POSSIBLE URI: " + line)
	
	if "user-agent" in line.lower() or "user agent" in line.lower():
		print("POSSIBLE USER-AGENT: " + line)

	if re.search(r"(HTTP)|(GET)|(PTTH)|(TEG)", line):
		print("POSSIBLE HTTP HEADER: " + line)

	if "connection" in line.lower() or "socket" in line.lower() or "port" in line.lower():
		print("POSSIBLE NETWORK TERMINOLOGY: " + line)

	if "download" in line.lower() or "upload" in line.lower():
		print("POSSIBLE FILE TRANSFER: " + line)

	if "bitcoin" in line.lower() or "ethereum" in line.lower() or "monero" in line.lower():
		print("POSSIBLE CRYPTOCURRENCY REFERENCE: " + line)

	if "password" in line.lower() or "passwd" in line.lower() or "shadow" in line.lower() or "pass" in line.lower():
		print("POSSIBLE PASSWORD ACTIVITY: " + line)

