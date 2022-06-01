from datetime import datetime, timedelta

finalline = []
format = '%H:%M:%S.%f'

subtitles = [
r"Dialogue: 0,0:02:59.03,0:03:03.57,Signs,,0000,0000,0000,,{\be1\bord1\xshad2\yshad3\pos(640,535)\fad(441,0)}Japan\n\n\nCapital City Shintou Teitou",
r"Dialogue: 0,0:02:59.03,0:03:03.57,Signs,,0000,0000,0000,,{\b1\be1\bord1\xshad2\yshad3\fad(440,0)}— Year 2020 —",
r"Dialogue: 0,0:23:13.04,0:23:16.04,Title Outline,,0000,0000,0000,,{\b1\blur2\bord3\4c&H55049F&\4a&H20&\pos(640,250)}First Wing",
r"Dialogue: 0,0:23:13.04,0:23:16.04,Title,,0000,0000,0000,,{\4c&H55049F&\4a&H20&\pos(640,250)}First Wing",
r"Dialogue: 0,0:23:13.04,0:23:16.04,Title Outline,,0000,0000,0000,,{\b1\be1\4c&H55049F&\4a&H20&\fs100\pos(640,565)}Sekirei",
r"Dialogue: 0,0:23:13.04,0:23:16.04,Title,,0000,0000,0000,,{\b1\4c&H55049F&\4a&H20&\fs100\pos(640,565)}Sekirei",
r"Dialogue: 0,0:23:32.12,0:23:36.06,Signs,,0000,0000,0000,,{\be1\bord1\xshad2\yshad3\pos(640,270)\fs46}Second Wing",
r"Dialogue: 0,0:23:32.12,0:23:36.06,Signs,,0000,0000,0000,,{\be1\bord1\xshad2\yshad3\fs80\pos(640,570)}Door to a New House",
r"Dialogue: 0,0:01:41.33,0:01:44.22,OPRO,,0000,0000,0000,,{\k12}i{\k9}ma {\k32}i{\k24}no{\k0}{\k21}chi{\k6} {\k29}ga {\k11}{\k31}ho{\k10}{\k104}ra",
r"Dialogue: 0,0:01:44.56,0:01:47.50,OPRO,,0000,0000,0000,,{\k20}ki{\k27}za{\k6}{\k21}shi{\k9}{\k11}te {\k7}{\k69}chi{\k16}t{\k50}te{\k11} {\k12}yu{\k8}{\k28}ku",
r"Dialogue: 0,0:01:47.82,0:01:54.02,OPRO,,0000,0000,0000,,{\k10}ni{\k4}{\k6}gi{\k3}{\k20}ri{\k9}{\k23}shi{\k10}{\k13}me{\k6}{\k35}ta {\k6}{\k30}u{\k9}{\k29}n{\k13}{\k34}me{\k6}{\k18}i {\k22}{\k16}mo{\k3}{\k15}u {\k6}{\k28}ma{\k6}{\k22}yo{\k4}{\k14}u{\k9} {\k33}ko{\k8}{\k34}to {\k6}{\k44}wa{\k17} {\k16}na{\k3}{\k30}i",
r"Dialogue: 0,0:00:21.21,0:00:23.75,On Top,,0000,0000,0000,,Yukishiro",
r"Dialogue: 0,0:06:07.05,0:06:12.42,On Top,,0000,0000,0000,,Theme",
r"Dialogue: 0,0:06:52.55,0:06:57.30,OS,,0000,0000,0000,,Hello, everyone!\NHow's it goin'? My name is\NEiji Busuji-",
r"Dialogue: 0,0:07:03.46,0:07:08.21,OS,,0000,0000,0000,,For some more info,\NMake sure you head over to\NMy personal blog!",
r"Dialogue: 0,0:00:02.04,0:00:08.00,Default,,0,0,0,,Causes of death are many and varied.\NOld age, suicide, illness......",
r"Dialogue: 0,0:00:02.06,0:00:08.61,Default,,0,0,0,,Causes of death are many and varied.\NOld age, suicide, illness...",
r"Dialogue: 0,0:00:08.61,0:00:13.20,Default,,0,0,0,,But the cause of death that scares\Nthe most people in this day and age...",
r"Dialogue: 0,0:00:16.99,0:00:18.20,Default,,0,0,0,,...is death by fire.",
r"Dialogue: 0,0:00:35.22,0:00:38.72,Default,,0,0,0,,\"Episode 1:\NA Fire Soldier's Fight\"",
r"Dialogue: 0,0:00:38.72,0:00:41.72,On Top,,0,0,0,,\"Ameyoko\"",
r"Dialogue: 0,0:00:45.60,0:00:47.27,Default,,0,0,0,,Where should we go next?"]

t = "0:00:02.04"
global changetime
changetime = datetime.strptime(t, format)
print(changetime)

def readtimes():
	x = 0
	for line in subtitles:
		strtime = ""
		#print(line[12:22] + " - " + line[23:33] + " - Original time")
		begtime = datetime.strptime(line[12:22], format)
		endtime = datetime.strptime(line[23:33], format)
		print(line)
		begline = line[:12]
		endline = line[33:]
		
		fbegtime = processtime(begtime)
		fendtime = processtime(endtime)
		
		finalline.append(begline + fbegtime + "," + fendtime + endline)
		x+=1

def processtime(ogtime):
	alteredtime = ogtime - changetime
	
	if len(str(alteredtime)) == 7:
		strtime = str(alteredtime) + ".000000"
	else:
		strtime = str(alteredtime)
	return strtime[:-4]

def printtimes():
	x = 0
	for line in finalline:
		print(finalline[x])
		x+=1


readtimes()
print("===============================")
printtimes()
input()


























