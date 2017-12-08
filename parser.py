#!/usr/bin/python
# -*- coding: utf-8 -*-
#parser.py
#parsing with Alpino parser
#16-10-2017
#Jun Jun Zhang (s2988240)
#using the alpino parser via edited .bashrc script
#look for the documentation on http://www.let.rug.nl/vannoord/alp/Alpino/
#command:
#	python parser.py

import os
import subprocess
import re

def main():

	directory = "tokenized_reviews/"
	parsed_directory = "parsed_reviews/"
	check = os.listdir(parsed_directory)
	for filename in os.listdir(directory):
		#print(filename)
		if filename == '.DS_Store':
			continue
		else:
			file_r = open(directory + filename, "r")
			file_w = open(parsed_directory + filename, "w")
			#filename = os.path.join(directory, filename)
			for line in file_r:
				print(line)
				#next lines are from: https://stackoverflow.com/questions/7353054/call-a-shell-command-containing-a-pipe-from-python-and-capture-stdout
				p1 = subprocess.Popen(["echo", line], stdout=subprocess.PIPE)
				p2 = subprocess.Popen(["sh",".bashrc"], stdin=p1.stdout, stdout=subprocess.PIPE)
				p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
				output,err = p2.communicate()
				file_w.write(output)
			file_r.close()			
			file_w.close()

main()
