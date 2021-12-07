import subprocess
import sys
import re
import os

def printColor(prefix, line):
	if os.name == "nt":
		os.system('color')
	print ('\033[93m' + prefix + '\033[0m' + line)

cryptocurrencies = ["Bitcoin", "Litecoin", "Namecoin", "Peercoin", "Dogecoin", "Gridcoin", "Primecoin", "Auroracoin", "Dash", "MazaCoin", "Monero", "Titcoin", "Verge", "Stellar", "Vertcoin", "Ethereum", "Ethereum Classic", "Nano", "Tether", "Firo", "Zcash", "Bitcoin Cash", "EOS.IO", "Cardano", "Tron", "AmbaCoin", "Algorand", "Shiba Inu", "BitClout", "SafeMoon", "Coinye", "OneCoin", "BitConnect", "KodakCoin", "Petro"]

network_terms = ["connection", "socket", " port ", "address", "tcp", "udp", "voip", " ping ", "traceroute", "tracert"]

file_extensions = [".BAT", ".BIN", ".CMD", ".COM", ".CPL", ".EXE", ".INF", ".INS", ".INX", ".ISU", ".JOB", ".JSE", ".LNK", ".MSC", ".MSI", ".MSP", ".MST", ".PAF", ".PIF", ".PS1", ".REG", ".RGS", ".SCR", ".SCT", ".SHB", ".SHS", ".U3P", ".VB", ".VBE", ".VBS", ".VBSC,RIPT" ".WS", ".WSF", ".WSH", ".JAR", ".DLL", ".PDB"]

if len(sys.argv) is not 2:
	print("Usage: yarn.py <name of file>")
	exit()


command = "strings " + sys.argv[1]
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
output, errors = process.communicate()

# probably important things 
output = output.decode()
# print("Any string starting with 2 letters, length of 5+\n")
# for line in output.split("\n"):
# 	if re.search(r"^[A-Za-z]{2}.*", line):
# 		if len(line) > 5:
# 			print(line)

# probably important things 
for line in output.split("\n"):

	lowercase = line.lower()

	if re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", lowercase):
		printColor("POSSIBLE IP ADDRESS: ", line)
	
	if re.search(r"[Cc]:\\", lowercase):
		printColor("POSSIBLE WINDOWS PATH: ", line)

	if re.search(r"(https)|(http)", lowercase):
		printColor("POSSIBLE URI: ", line)
	
	if "user-agent" in lowercase or "user agent" in lowercase:
		printColor("POSSIBLE USER-AGENT: ", line)

	if re.search(r"(HTTP)|(GET)|(PTTH)|(TEG)", line) and len(line) > 6:
		printColor("POSSIBLE HTTP HEADER: ", line)

	if any(netterm in lowercase for netterm in network_terms) and len(line) > 6:
		printColor("POSSIBLE NETWORK TERMINOLOGY: ", line)

	if "download" in lowercase or "upload" in lowercase:
		printColor("POSSIBLE FILE TRANSFER: ", line)

	if any(crypto in lowercase for crypto in cryptocurrencies):
		printColor("POSSIBLE CRYPTOCURRENCY REFERENCE: ", line)

	if "password" in lowercase or "passwd" in lowercase or "shadow" in lowercase or "pass" in lowercase:
		printColor("POSSIBLE PASSWORD ACTIVITY: ", line)
	
	if any(ext in lowercase for ext in file_extensions):
		printColor("POSSIBLE FILE EXTENSION: ", line)

