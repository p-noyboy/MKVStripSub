'''
Merges chapters that were extracted in an 
XML format that precedes with a "NEW - " 
'''

import os
import subprocess
all_files = os.listdir()

#Command line input to run in the function
cli_command_chapter_merge = [r"C:/Program Files/MKVToolNix/mkvpropedit.exe", "", "--chapters", ""]

#Updates CLI to add filename to extract chapters
def update_cli_chapter_merge(file):
	cli_command_chapter_merge.pop()
	cli_command_chapter_merge.pop(1)
	cli_command_chapter_merge.insert(1, file)
	cli_command_chapter_merge.append("NEW - " + file[:-4] + ".xml")

'''
Takes in a cmd line input and 
returns the text result as output_lines
'''
def cli(cmd):
	try:
		p = subprocess.check_output(cmd)
		output_string = p.decode()
		output_lines = output_string.split('\n')
		return output_lines
	except:
		print("  **Error, could not merge " + cli_command_chapter_merge[1])
		return None

def merge_all_chapters():	
	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			update_cli_chapter_merge(file)
			cli(cli_command_chapter_merge)
			print("    > Merged chapters into > " + cli_command_chapter_merge[1])
			#print("    ^^^^^^^^^^^^^^^^^^")
	print("******************")
	print("Finished merging all chapters")
	print("******************")

if __name__ == '__main__':
	merge_all_chapters()
	print("ok, finished")