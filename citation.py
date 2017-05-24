# written by Nazanin Ghasemian
# this program, find the female and male name in a References section of a pdf file.
# for now, I fixed the name of pdf file.
import re
import subprocess
import collections

all_male_names=[]
all_female_names=[]
male_found_names=collections.defaultdict(int)
female_found_names=collections.defaultdict(int)
input_file_ref_extracted=[]


def read_names():
# read male anf female names from files in RawNames
# source: http://deron.meranda.us/data/census-dist-female-first.txt
# source: http://deron.meranda.us/data/census-dist-male-first.txt
	female_name_file=open('./RawNames/census-dist-female-first.txt', 'r')
	for line in female_name_file:
		words=line.split(' ')
		all_female_names.append(words[0])	

	male_name_file=open('./RawNames/census-dist-male-first.txt', 'r')
	for line in male_name_file:
		words=line.split(' ')
		all_male_names.append(words[0])	

def read_input_file():
#read pdf: for now, I dont get it from prompt. 
#	input_pdf_file= '1-s2.0-S0723086915000924-main.pdf'
	input_pdf_file= '1412.5150.pdf'

	args = ['pdftotext', '-layout', '-q', input_pdf_file , '-']
	global input_file_txt 
	input_file_txt = subprocess.check_output(args, universal_newlines=True)
	


def find_name():
	for male_name in all_male_names:
		for words in input_file_ref_extracted:
			if male_name.lower()==words:			
				male_found_names[male_name]+=1;
	for female_name in all_female_names:
		for words in input_file_ref_extracted:
			if female_name.lower()==words:			
				female_found_names[female_name]+=1;



def extract_refrences():
	temp=input_file_txt.split('References')
	for item in temp:
		if '[1]' in item:
			temp1=str(item)
			global input_file_ref_extracted
			input_file_ref_extracted = input_file_ref_extracted + re.findall(r"[\w']+",item.lower())
#			print(re.findall(r"[\w']+",item))


def print_report():
	print("\n\n================References part===============")
	print(input_file_ref_extracted)
	print("\n\n================Male===============")
	for item in male_found_names:
		if male_found_names[item]>0:
			print(item, male_found_names[item])
	print("================Female===============")
	for item in female_found_names:
		if female_found_names[item]>0:
			print(item, female_found_names[item])


read_input_file()
extract_refrences()

read_names()

find_name()
print_report()
