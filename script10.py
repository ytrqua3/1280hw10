#!/usr/bin/python3
import os
import sys
import subprocess
import re

os.chmod("test.txt", int('777',8))
def createFile(fname):
	subprocess.run(["touch", fname])
	with open(fname, mode="w") as file:
		subprocess.run(["echo", "test file"], stdout=file, text=True)

def permStrToOct(perm_str):
	perm=""
	for i in range(len(perm_str)):
		if(perm_str[i] == '-'):
			perm = perm + '0'
		else:
			perm = perm + '1'
	return int(perm, 2)

os.chdir(sys.argv[1])
root=os.getcwd()
print(root)
for line in sys.stdin:
	is_start = line.startswith(".") and line.endswith(":\n")
	is_total = line.startswith("total")
	if is_start:
		target_directory=line.strip("\n").strip(":").replace(".",root)
		#print(target_directory)
		os.chdir(target_directory)
	elif is_total:
		continue
	elif line=="\n":
		continue
	else:
		data=line.strip().split(" ")
		ftype=data[1][0]
		perm=permStrToOct(data[1][1:])
		#print(perm)
		fname=data[-1]
		if ftype=='d':
			os.mkdir(fname)
			os.chmod(fname, perm)
		if ftype=='-':
			createFile(fname)
			os.chmod(fname, perm)
