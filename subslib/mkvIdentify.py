#B:\Users\Chris\Documents\Programming\Python\StripSubs\mkvidentify.py
import os
import subprocess
all_files = os.listdir()

#Command line input to run in the function
cli_command = [r"C:/Program Files/MKVToolNix/mkvmerge.exe", "--identify", ""]
mkvsearch = "Track ID"
mkvsearch2 = "subtitles"

'''
Takes in a cmd line input and 
returns the text result as output_lines
'''
def cli(cmd):
	p = subprocess.check_output(cmd)
	output_string = p.decode()
	output_lines = output_string.split('\n')
	return output_lines
	
#Takes a file in and identifies its subtitles
#or all tracks if is_subtitles = false
def identify_unique_file(file, is_subtitles):
	cli_command.pop() #pops blank file at the end of the command or the previous file to add the current file
	cli_command.append(file)
	output_lines = cli(cli_command)
	print()
	if is_subtitles == True:
		for line in output_lines:
			if line.find(mkvsearch) != -1 and line.find(mkvsearch2) != -1:
				print("    " + line)
	else:
		for line in output_lines:
			if line.find(".ttf") == -1 and line.find(".otf") == -1: #filters out .ttf and .otf
				print("    " + line)
	print("^^^^^^^^^^^^^^^^^^")

'''
Runs through all files but breaks out of the
loop after identifying the first file
If is_subtitles is True then it 
'''
def identify_first_file(is_subtitles):
	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			print(file)
			cli_command.pop() #pops blank file at the end of the command or the previous file to add the current file
			cli_command.append(file)
			output_lines = cli(cli_command)
			print()
			if is_subtitles == True:
				for line in output_lines:
					if line.find(mkvsearch) != -1 and line.find(mkvsearch2) != -1:
						print("    " + line)
			else:
				for line in output_lines:
					if line.find(".ttf") == -1 and line.find(".otf") == -1: #filters out .ttf and .otf
						print("    " + line)
			print("^^^^^^^^^^^^^^^^^^")
			break

def identify_all_files_subs():
	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			print(file)
			cli_command.pop() #pops blank file at the end of the command or the previous file to add the current file
			cli_command.append(file)
			output_lines = cli(cli_command)
			print()
			for line in output_lines:
				if line.find(mkvsearch) != -1 and line.find(mkvsearch2) != -1:
					print("    " + line)
			print("^^^^^^^^^^^^^^^^^^")
			print()
	print("******************")
	print("Finished running all files")

if __name__ == '__main__':
	choice = input("Press a number 0 or 1: ")
	if choice == "1":
		identify_all_files_subs()
	elif choice == "2":
		identify_first_file(False)
	elif choice == "3":
		identify_first_file(True)
	elif choice == "4":
		identify_unique_file("Dumbbell.mkv", False)
	else:
		print("Exiting program")
	print("ok, finished")
	#identify_a_file()			
	#identify_all_files()