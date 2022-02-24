'''
Uses MKVPropEdit to edit an MKVs title and subtitles.
It will go through all files in a folder and rename
it the title of the show with the season given and
increase episode count with each file, example:
Avatar The Last Airbender - 1x02
That would be the 2nd file in the list given the
season number given was 1.

It asks if there is a subtitle track that should
be Signs and Songs and Forced, or if there is one
that is full English Subtitles and does not force it
'''
from subslib.mkvIdentify import identify_unique_file
from subslib.mkvInfo import info_unique_file
import subprocess
import os

#global variables to assign these via function
choice_title = ""
choice_season = ""
choice_subSign = ""
choice_subEng = ""

#Command line input to run in the function
'''
MKVPropEdit commmand that changes the property
of an MKV to add in the name of the file/show
0 - Location of MKVPropEdit in your computer
4 - Name of the show + [season number] x [episode number]
6 - Subtitle track number that is Signs and Songs
    Sets it as the default track and forces it
14 - Subtitle track number that is NOT Signs and Songs
21 - File name that is being edited
'''
#"C:/Program Files/MKVToolNix/mkvpropedit.exe" --edit info --set "title=!name!" --edit track:s%a% --set flag-default=1 --set flag-forced=1 --set name="Signs & Songs" --edit track:s%b% --set flag-default=0 --set flag-forced=0 --set name="English Subtitles" "%%f"
cli_command = [r"C:/Program Files/MKVToolNix/mkvpropedit.exe", "--edit", "info", "--set", '"title=!name!"', "--edit", "track:s%a%", "--set", "language=eng", "--set", "flag-default=1", "--set", "flag-forced=1", "--set", 'name=Signs & Songs', "--edit", "track:s%b%", "--set", "language=eng", "--set", "flag-default=0", "--set", "flag-forced=0", "--set", 'name=English Subtitles', 'Show Name.mkv']
#22 entries in that list, 1-4 Title, 5-14 Signs, 15-24, English

'''
Updates the CLI command once to 
set the correct subtitle tracks to update
as Signs and Songs and as English Subtitles.
Removes the command completely if a blank
track ID was entered instead
'''
def update_cli_tracks(signid, engid):
	print()
	cli_command.pop(16)
	cli_command.pop(6)
	cli_command.insert(6, "track:s" + signid)
	cli_command.insert(16, "track:s" + engid)
	if engid != "" or signid != "":
		choice_keep_names = input("Type 1 if you want to keep subtitle name as is: ")
		if engid != "" and choice_keep_names == "1":
			cli_command.pop(24)
			cli_command.pop(23)
		if signid != "" and choice_keep_names == "1":
			cli_command.pop(14)
			cli_command.pop(13)
	if engid == "":
		for x in range(24, 14, -1):
			cli_command.pop(x)
	if signid == "":
		for x in range(14, 4, -1):
			cli_command.pop(x)
			

'''
Updates the CLI command to add the title
name with correct episode number and file path.
Leaves blank if the string is empty.
Adds a 0 before the number if under 10
'''
def update_cli(file, episode_number):
	if choice_title != "":
		if episode_number < 10:
			ep_title = choice_title + " - " + choice_season + "x0" + str(episode_number)
		else:
			ep_title = choice_title + " - " + choice_season + "x" + str(episode_number)
		
		cli_command.pop(4)
		cli_command.insert(4, "title=" + ep_title)
	else:
		if cli_command[4].find("!name!") > 0:
			for x in range(4, 0, -1):
				cli_command.pop(x)
	cli_command.pop()
	cli_command.append(file)

#Runs the CLI command through subprocess
def cli_call_program(cmd):
	try:
		p = subprocess.check_output(cmd, shell=True)
		output_string = p.decode()
		output_lines = output_string.split('\n')
	except:
		print("	 ****Error with file " + cli_command[len(cli_command) - 1])
		#print(cli_command)
		return None
	return output_lines

#Asks user for show title, season, and subtitle track
def get_choices():
	global choice_title
	global choice_season
	global choice_subSign
	global choice_subEng
	print()
	print("Subtitle tracks start at 1, they do not match the Track ID")
	print()
	choice_title = input("What is the name of the show? (Leave blank and press Enter if none): ")
	if choice_title != "":
		choice_season = input("What season is this?: ")
	choice_subSign = input("Which subtitle track number is Signs and Songs? (Leave blank and press Enter if none): ")
	choice_subEng = input("Which subtitles are full Englsh? (Leave blank and press Enter if none): ")
	#print("Title in function " + choice_title)
	
'''
Main program that runs through all the files and
edits the MKV based off of input from the user.
First run, identifies the file to see which subtitle
track to edit and updates the CLI command accordingly
Also increments episode number
'''
def edit_all_files():
	all_files = os.listdir()
	is_first = True
	global episode_number
	
	for file in all_files:
		if file.endswith(".mkv"):
			print()
			if is_first == True:
				info_unique_file(file, True)
				get_choices()
				update_cli_tracks(choice_subSign, choice_subEng)
				episode_number = 1
				is_first = False
			update_cli(file, episode_number)
			#print(cli_command) # Testing CLI
			output_lines = cli_call_program(cli_command)
			episode_number += 1
			if output_lines != None:
				print("    Edited file > " + file)
	print("Altered all MKV files")

if __name__ == '__main__':
	edit_all_files()