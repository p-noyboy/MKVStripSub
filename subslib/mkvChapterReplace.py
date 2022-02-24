import os
from datetime import datetime, date

mkvsearch = "ChapterString"
mkvsearch2 = "ChapterTimeStart>"
chap_num = 100
chap_time = 100 #Where the chapter time string starts relative to the chapter string
lst_choice = []


def int_dictionary():
	choice_dict = {
		"1": "Prologue",
		"2": "Opening",
		"3": "Part A",
		"4": "Part B",
		"5": "Ending",
		"6": "Preview",
		}
	return choice_dict

#Opens file and returns all of its lines in an array
def get_lines(file):
	#with open(file, 'rt', encoding='utf8') as fd:
	with open(file, 'rt') as fd:
		all_lines = fd.readlines()
	fd.close()
	return all_lines

'''
Creates a list with all array numbers where 
all_lines has a line from mkvsearch (ChapterString)
'''
def get_total_chapers(all_lines, chapter_string_list):
	global chap_time
	line_number = -1
	
	for line in all_lines:
		line_number += 1
		if line.find(mkvsearch) != -1:
			chapter_string_list.append(line_number)
			
	for x in range(chapter_string_list[0], 0, -1):
		if all_lines[x].find(mkvsearch2) != -1:
			chap_time = chapter_string_list[0] - x
			break
	return chapter_string_list

def clear_lists():
	for x in range(len(lst_choice)):
		lst_choice.pop()
	
#Returns the line but edits it first if need be
def update_lines(all_lines):
	global chap_num
	chapter_string_list = []
	#print(lst_choice)
	
	chapter_string_list = get_total_chapers(all_lines, chapter_string_list)
	chap_num_current = len(chapter_string_list)
		
	if chap_num != chap_num_current:
		chap_num = chap_num_current
		clear_lists()
		
		for x in range(chap_num): #For loop prints chapter timestamps
			timestamp = get_timestamp(x, all_lines, chapter_string_list)
			print("  Chapter " + str(x + 1) + " " + timestamp)
			print(timestamp)
			#print(all_lines[chapter_string_list[x]])
			
		print() 
		for x in range(chap_num): #Loop that asks for chapter name
			choice = input("    What's the name for chapter " + str(x + 1) + "? ")
			lst_choice.append(choice)
		print()

	for y in range(chap_num): #Loop that adds chapter name to file
		#print(all_lines[chapter_string_list[y]])
		all_lines[chapter_string_list[y]] = "        <ChapterString>" + lst_choice[y] + "</ChapterString>\n"
	return all_lines

def get_timestamp(x, all_lines, chapter_string_list):
	timestring = all_lines[chapter_string_list[x] - chap_time][24:32]
	return timestring
	
#Opens a new file and writes all new lines to it
def rewrite_lines(file, all_lines):
	new_file = "NEW - " + file
	wd = open(new_file, 'wt')
	for line in all_lines:
		wd.write(line)
	wd.close()
	print("    > Wrote to > " + new_file)

def replace_all_chapters():
	all_files = os.listdir()
	print()
	
	for file in all_files:
		#print("******************")
		if file.endswith('.xml'):
			all_lines = get_lines(file)
			
			new_array = update_lines(all_lines)
			rewrite_lines(file, new_array)
	print("******************")
	print("Finished replacing all chapter names")
	print("******************")

if __name__ == '__main__':
	replace_all_chapters()
	print("mkvChapterReplace program complete")