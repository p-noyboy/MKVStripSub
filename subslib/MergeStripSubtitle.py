#B:\Users\Chris\Documents\Programming\MKV\StripSubs\MergeStripSubtitle.py
import os
import subprocess

#Command line input to run in the function
#2 = new file, 3 = source file, 12 = source sub file
cli_command = [r"C:/Program Files/MKVToolNix/mkvmerge.exe", "-o", "", "", "--language", "0:eng", "--default-track", "0", "--forced-track", "0", "--track-name", "0:Signs & Song", ""]

'''
Takes in a cmd line input and 
returns the text result as output_lines
'''
def cli(cmd):
	p = subprocess.check_output(cmd)
	output_string = p.decode()
	output_lines = output_string.split('\n')
	return output_lines

'''
Update the extract command to extract the subtitles
from the current file being looped, and save it as that
file's .ass file
'''
def update_cli(file):
	cli_command.pop()
	cli_command.pop(3)
	cli_command.pop(2)
	cli_command.insert(2, "NEW - " + file)
	cli_command.insert(3, file)
	cli_command.append("NEW - " + file[:-4] + ".ass")

def merge_all_files():
	all_files = os.listdir()

	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			print()
			print("    > " + file)
			update_cli(file)
			output_lines = cli(cli_command)
			#for line in output_lines:
				#print(line)
			print("    ^^^^^^^^^^^^^^^^^^")
			print("    Merged " + file)
	print("**********************************************")
	print("Finished merging all files")
	print("**********************************************")

if __name__ == '__main__':
	merge_all_files()
#input()