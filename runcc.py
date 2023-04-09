#!/usr/bin/python3

# --- Import module and method
import argparse
from os import path
from subprocess import run

# -- defined main function
def main():
	pass

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Simple execute source code C/C++")
	parser.add_argument("filename", type=str, help="filename of the source code C/C++")
	args = parser.parse_args()
	

