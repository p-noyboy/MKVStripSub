#B:\Users\Chris\Documents\Programming\Python\StripSubs\mkvinfo.py
import os
import subprocess
all_files = os.listdir()

#Command line input to run in the function
cli_command = [r"C:/Program Files/MKVToolNix/mkvinfo.exe", ""]
search0 = "+ Title:"
search1 = "+ Track number:"
search2 = "+ Track type:"
search3 = "+ Name"
search4 = "+ Codec ID:"
search5 = "+ Default track flag: 1"
search6 = "+ Forced track flag: 1"
search7 = "+ Language:"

'''
Takes in a cmd line input and 
returns the text result as output_lines
'''
def cli(cmd):
	p = subprocess.check_output(cmd)
	output_string = p.decode()
	output_lines = output_string.split('\n')
	return output_lines

#Takes a file in and identifies its tracks
#or all info if is_tracks = False
def info_unique_file(file, is_tracks):
	cli_command.pop() #pops blank file at the end of the command or the previous file to add the current file
	cli_command.append(file)
	output_lines = cli(cli_command)
	print()
	if is_tracks == False:
		for line in output_lines:
			print(line)
	else:
		for line in output_lines:
			if line.find(search0) != -1 or line.find(search1) != -1:
				print()
				print("    " + line)
			elif line.find(search2) != -1 or line.find(search3) != -1 or line.find(search4) != -1 or line.find(search5) != -1 or line.find(search6) != -1 or line.find(search7) != -1:
				print("    " + line)
	print("^^^^^^^^^^^^^^^^^^")

'''
Runs through all files but breaks out of the
loop after identifying the first file
'''
def info_first_file(is_tracks):
	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			print(file)
			cli_command.pop() #pops blank file at the end of the command or the previous file to add the current file
			cli_command.append(file)
			output_lines = cli(cli_command)
			print()
			if is_tracks == False:
				for line in output_lines:
					print(line)
			else:
				for line in output_lines:
					if line.find(search0) != -1 or line.find(search1) != -1:
						print()
						print("    " + line)
					elif line.find(search2) != -1 or line.find(search3) != -1 or line.find(search4) != -1 or line.find(search5) != -1 or line.find(search6) != -1 or line.find(search7) != -1:
						print("    " + line)
			print("^^^^^^^^^^^^^^^^^^")
			break

def info_all_files_subs():
	for file in all_files:
		#print("******************")
		if file.endswith('.mkv'):
			print(file)
			cli_command.pop() #pops blank file at the end of the command or the previous file to add the current file
			cli_command.append(file)
			output_lines = cli(cli_command)
			print()
			for line in output_lines:
				print("    " + line)
			print("^^^^^^^^^^^^^^^^^^")
			print()
	print("******************")
	print("Finished running all files")

if __name__ == '__main__':
	#identify_unique_file("Fire.mkv")
	info_first_file(True)
	#identify_unique_file("[Cleo]Kono_Subarashii_Sekai_ni_Shukufuku_wo!_2_-_01_(Dual Audio_10bit_BD1080p_x265).mkv")
	#identify_a_file()			
	#identify_all_files()