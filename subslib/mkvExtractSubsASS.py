#B:\Users\Chris\Documents\Programming\MKV\StripSubs\mkvExtractSubsASS.py
'''
Runs through all files in a folder and extracts
the subtitle track based on user input using 
MKVToolNix. Displays the available tracks of
the first file in the folder, displays only the 
subtitle tracks, and asks the user which track
to extract from. 

WARNING: Error handling can anticipate incorrect
track requests, but if the user chooses a non-ass
subtitle track, or a non-subtitle track, the
program will run like normal.
'''

import os
import subprocess
from subslib.mkvIdentify import identify_unique_file
all_files = os.listdir()

#Command line input to run in the function
cli_extract = [r"C:/Program Files/MKVToolNix/mkvextract.exe", "tracks", "", ""]

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
		print("Error with CLI command, exiting program")
		exit()

'''
Update the extract command to extract the subtitles
from the current file being looped, and save it as that
file's .ass file
'''
def update_cli(file, trackid):
	cli_extract.pop()
	cli_extract.pop()
	cli_extract.append(file)
	cli_extract.append(trackid + ':' + file[:-4] + '.ass')
	
'''
Asks the user to select which subtitle to extract and
loops through until the user picks a valid choice
'''
def choice_loop():
	choice = ""
	is_valid = False
	
	print()
	while is_valid == False:
		try:
			choice = input("Which subtitles would you like to extract? ")
			x = int(choice)
			if x >= 0 and x <= 10:
				return choice
			else:
				print("Invalid choice, please try again")
		except:
			print("Invalid choice, please try again")

'''
Runs through each file and 
extracts the ASS subtitle file
'''
def extract_all_files():
	is_first = True
	trackid = ""
	
	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			print()
			print("    > " + file)
			if is_first == True:
				identify_unique_file(file, True)
				trackid = choice_loop()
				is_first = False
			update_cli(file, trackid)
			output_lines = cli(cli_extract)
			try:
				#for line in output_lines:
					#print(line)
				print("    ^^^^^^^^^^^^^^^^^^")
				print("    Extracted  " + file)
			except:
				print("****Error extracing " + file)
	print("**********************************************")
	print("Finished extracting all files")
	print("**********************************************")
#input()

if __name__ == '__main__':
	extract_all_files()