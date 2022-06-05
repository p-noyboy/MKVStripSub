from subslib.mkvExtractSubsASS import extract_all_files
from subslib.StripSubtitleASSDefault import strip_all_files
from subslib.MergeStripSubtitle import merge_all_files
from subslib.mkvEditTrackData import edit_all_files
from subslib.mkvChapterExtract import extract_all_chapters
from subslib.mkvChapterReplace import replace_all_chapters
from subslib.mkvChapterMerge import merge_all_chapters
from subslib.mkvInfo import info_first_file
from subslib.retimesubs import retime_subs
import time

dict_error_message = "Invalid choice, please try again"

def int_dictionary():
	choice_dict = {
		"1": extract_all_files,
		"2": strip_all_files,
		"22": retime_subs,
		"3": merge_all_files,
		"4": extract_strip,
		"5": extract_strip_merge,
		"6": edit_all_files,
		"7": strip_edit_merge_chapters,
		"8": edit_merge_chapters,
		"9": info_first_file_func,
		"q": "exit"
		}
	return choice_dict
'''
Function that loops through a menu
and allows different choices to be
selected and actions to be run based
on those choices selected from a 
dictionary. Loops until q is typed
'''
def menu():
	is_menu = True
	choice_dict = int_dictionary()
	while is_menu:
		print()
		print()
		print()
		print()
		print()
		print()
		print("* MKV Subtitle and Chapter Editor")
		print("*************************")
		print("* 1 Extract subtitles from all MKV in folder")
		print("* 2 Strip all subtitles in folder")
		print("* 3 Merge all subtitles into all MKV in folder")
		print("* 4 Extract and strip subtitles from MKVs")
		print("* 5 Extract, Strip, then Merge subs into MKV")
		print("* 22 Retime all subtitles in folder")
		print("* ")
		print("* 6 Edit Title & forced subtitles")
		print("* ")
		print("* 7 Extract, edit, then re-add chapters")
		print("* 8 Edit then re-add chapters")
		print("* ")
		print("* 9 Show file track info")
		print("* q Quit the program")
		print("*************************")
		#print("8 ")
		#print("9 ")
		#print("q Quit")
		print("")
		choice = input("    Which task would you like to run? ")
		x = choice_dict.get(choice, dict_error_message)
		if x == choice_dict.get("q"):
			print("Exiting program")
			break
		elif x == dict_error_message:
			print()
			print(x)
			time.sleep(1)
		else:
			x()
	print()

def extract_strip():
	extract_all_files()
	strip_all_files()

def extract_strip_merge():
	extract_all_files()
	strip_all_files()
	merge_all_files()

def strip_edit_merge_chapters():
	extract_all_chapters()
	replace_all_chapters()
	merge_all_chapters()

def edit_merge_chapters():
	replace_all_chapters()
	merge_all_chapters()

def info_first_file_func():
	info_first_file(True)
	input("    Press enter once finished viewing data")
	
menu()
time.sleep(1)
#input()
