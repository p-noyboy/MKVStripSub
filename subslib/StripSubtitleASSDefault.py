#B:\Users\Chris\Documents\Programming\MKV\StripSubs\StripSubtitleASSDefault.py
'''
This file will read all files in a folder
It will read the files one by one,
strip the file of a line based off of user's input
in hopes of removing all regular dialogue from a
subtitle file to keep just the sign and songs.

Saves the stripped lines in an array and writes
it out to a new subtitle file appended with " - New"
'''

import os
import re

#cwd = os.getcwd()
#print(cwd)
check_array = [""]

'''
Matches to remove lines that have the word "default" in it,
has stuff in the middle, and then has
,,. or ,,[\w] where [\w] is any alpha character
'''
#pattern = re.compile(r"(?i).+(default.+0,,[\w]|default.+0,,\.).+")
#patternDefault = re.compile(r"(?i).+(default.+0,,[\w\W]|while.+0,,[\w\W]|alt.+0,,[\w\W]|default.+0,,[\.']|default.+0,,-|default.+0,,{\\i1}[\w]).+")
'''With quotes'''
#patternDefault = re.compile(r"(?i).+(default.+0,,[\w]|default.+0,,\"|default.+0,,--|while.+0,,[\w]|alt.+0,,[\w]|default.+0,,[\.']|default.+0,,-|default.+0,,{\\i1}[\w]).+")
'''Without quotes'''
patternDefault = re.compile(r"(?i).+(default.+0,,[\w]|default.+0,,--|while.+0,,[\w]|alt.+0,,[\w]|default.+0,,[\.']|default.+0,,-|default.+0,,{\\i1}[\w]|Italics.+0,,[\w]).+") 
#pattern = re.compile(r"(?i).+(Main,,|Secondary,,|Thoughts,,|Narrator,,|Flashback,,).+") 
#patternMain = re.compile(r"(?i).+(Default,|DefaultAlt,|Dialogue,|Main.+0,,[\w]|Main.+0,,[\W\w]|Main.+0,,\.|Main I,|Italics,|Secondary,|Thoughts,|Narrator,|Flashback,|Narration,|Top,|Overlap,).+")
patternMain = re.compile(r"(?i).+(Default,|DefaultAlt,|Dialogue,|Main.+0,,[\w]|Main.+0,,[\W][\w]|Main.+0,,\.|Main I,|Italics,|Secondary,|Thoughts,|Narrator,|Flashback,|Narration,|Top,|Overlap,).+")
#pattern2 = re.compile(r"(?i).+(default.+0,,{\\i1}[\w]).+")


#**********************************Start of Functions

#Opens file and returns all of its lines in an array
def get_lines(file):
	#with open(file, 'rt', encoding='utf8') as fd:
	with open(file, 'rt', encoding='utf8') as fd:
		all_lines = fd.readlines()
	fd.close()
	#print(all_lines)
	'''
	for line in all_lines:
		print(line)
	'''
	return all_lines
	

#Returns the line if it matches or None if it doesn't
def match_line(subtitle_line, is_default):
	try:
		#print(is_default)
		if is_default == True:
			match = patternDefault.search(subtitle_line)
			return match
		elif is_default == False:
			match = patternMain.search(subtitle_line)
			#if subtitle_line.find("Sign,0") != -1 or subtitle_line.find("sign,0") != -1:
			#	return None
			return match			
	except:
		return "Pickles"

#Returns the line if it matches or None if it doesn't
def match_line_main(subtitle_line):
	try:
		match = patternMain.search(subtitle_line)
		#print(match)
		return match
	except:
		return "Pickles"


#Opens a new file and writes all new lines to it
def rewrite_lines(new_file, all_lines):
	all_lines.insert(2, "Script stripped to be Signs & Songs by P-NoyBoy\n")
	wd = open(new_file, 'wt', encoding='utf8')
	for line in all_lines:
		wd.write(line)
	wd.close()
	print("     Wrote to " + new_file)

#Returns a new file name by adding -New to it
def get_new_name(filename):
	'''
	name_part1 = filename[:-4]
	name_part2 = filename[-4:]
	new_file_name = name_part1 + "-NEW" + name_part2
	'''
	new_file_name = "NEW - " + filename
	return new_file_name

def print_check_lines():
	wd = open('CheckLines.txt', 'wt', encoding='utf8')
	for line in check_array:
		wd.write(line)
	wd.close()
	print("  Wrote to CheckLines.txt for questionable subs")

'''
Asks the user to select a choice and
loops through until the user picks a valid choice
'''
def choice_loop():
	choice = ""
	
	print()
	while choice != "1" and choice != "2":
		print("    1 Subtitles use Default subs, basic")
		print("    2 Subtitles use Main subs, advanced")
		choice = input("Which number associates best with the subtitles? ")
		print()
		if choice != "1" and choice != "2":
			print("Invalid choice, please try again")
		elif choice == "1":
			return True
		elif choice == "2":
			return False
	
def strip_all_files():
	all_files = os.listdir()
	is_default = False
	is_first = True
	
	for file in all_files:
		if file.endswith(".ass"):
			new_array = [""]
			print("     > " + file)
			print()
			if is_first == True:
				is_default = choice_loop()
				is_first = False
			check_array.append(file + '\n')
			all_lines = get_lines(file)
			new_file_name = get_new_name(file)
			for line in all_lines:
				checked_line = match_line(line, is_default)
				if checked_line == None:
					new_array.append(line)
					#print(line)
			rewrite_lines(new_file_name, new_array)
	print("**********************************************")
	print("Finished stripping all files")
	print("**********************************************")
	print()
	input("Ready to continue?")
#**********************************End of Functions

if __name__ == '__main__':
	strip_all_files()
#input()