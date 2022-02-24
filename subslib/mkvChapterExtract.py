#B:\Users\Chris\Documents\Programming\MKV\PythonSubProcess\mkvidentify.py
import os
import subprocess
all_files = os.listdir()

#Command line input to run in the function
cli_command_extract = [r"C:/Program Files/MKVToolNix/mkvextract.exe", "", "chapters", ""]
mkvsearch = "ChapterString"

#Updates CLI to add filename to extract chapters
def update_cli_extract(file):
	cli_command_extract.pop()
	cli_command_extract.pop(1)
	cli_command_extract.insert(1, file)
	cli_command_extract.append(file[:-4] + ".xml")


'''
Takes in a cmd line input and 
returns the text result as output_lines
'''
def cli(cmd):
	p = subprocess.check_output(cmd)
	output_string = p.decode()
	output_lines = output_string.split('\n')
	return output_lines

def extract_all_chapters():
	is_first = True
	
	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			update_cli_extract(file)
			cli(cli_command_extract)
			print()
			print("    Extracted >" + cli_command_extract[3])
			print("    ^^^^^^^^^^^^^^^^^^")
	print("******************")
	print("Finished extracting all chapters")

if __name__ == '__main__':
	extract_all_chapters()
	print("ok, finished")