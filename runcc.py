#!/usr/bin/python3

# --- Import module and method
import argparse
from os import path
from subprocess import run

# -- defined main function
def main(f, s):
	compiler=""
	PRINT_ICON()
	print(f+" output -->\n")
	if s == 0:
		compiler = "gcc"
	elif s == 1:
		compiler = "g++"
	runner(compiler, f)
	return 0

def isValid(f):
	done = -1
	ext = f.split(".")[-1] #get extension
	
	#in --> multiple or
	if ext in ["c","cxx","cc","C"]: 
		done = 0
	elif ext in ["cpp","CPP"]:
		done = 1
	
	return done

def PRINT_ICON():
	print("""
 _ __ _   _ _ __   ___ ___ 
| '__| | | | '_ \ / __/ __|
| |  | |_| | | | | (_| (__ 
|_|   \__,_|_| |_|\___\___|
	""")
	print("============================")
	
def runner(c, f):
	run([c,"-Wall",f])
	run(["./a.out"])
	run(["rm", "a.out"])
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Simple execute source code C/C++")
	parser.add_argument("filename", type=str, help="filename of the source code C/C++")
	args = parser.parse_args()
	status = isValid(args.filename)
	done = -1
	if status in[0,1] and path.isfile(args.filename):
		done = main(args.filename,status)
	else:
		print("runcc: oops, something went wrong...")
	exit(done)
