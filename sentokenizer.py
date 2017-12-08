#!/usr/bin/python
# -*- coding: utf-8 -*-
#parser.py
#tokenizes the data
#16-10-2017
#Jun Jun Zhang (s2988240)
#prepares for the alpino parser
#puts a sentence on each line per review
#removes all punctuation except ! ? , .
#command:
#	python3 sentokenizer.py

import os
import re

def main():

	directory = "csicorpus/reviews_propname/"
	target_directory = "tokenized_reviews/"
	check = os.listdir(target_directory)
	for filename in os.listdir(directory):
		#print(filename)
		if filename == '.DS_Store':
			continue
		else:
			file_r = open(directory + filename, "r")
			file_w = open(target_directory + filename, "w")
			for line in file_r:
				line = re.sub('[!?\.]+', '\g<0>|', line.strip())
				line = re.sub('[@#$%^&*()-+=<>\/;:„“”‘’"\']+', '', line)
				line = re.sub('[!?\.]+', ' \g<0>', line)
				line = line.strip().split('|')[:-1]
				for sen in line:
					sen = sen.strip()
					file_w.write(sen.lower() + '\n')
			file_r.close()			
			file_w.close()
					
main()
