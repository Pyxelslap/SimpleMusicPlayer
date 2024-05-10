import os,sys,cmd,curses,math
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
helpmsg = "Simple Music Player by LoccxlBedrock666\nParamwters list:\n\n - Parameter 1: Audio File\n - Parameter 2: Cover art file\n\nKey list:\n\n  p: Pause the Audio\n  r: Repeat the current audio\n  q or ESC: Exit the music player"
if len(sys.argv[1]) == 1:
    print(helpmsg)
    exit()
if sys.argv[1] == "help":
    print(helpmsg)
    exit()
if os.path.exists(sys.argv[1]) == False:
    print("Error: '"+sys.argv[1]+"' No such file or directory")
    exit(1)
if len(sys.argv) == 3:
    if os.path.exists(sys.argv[2]) == False:
        print("Error: '"+sys.argv[2]+"' No such file or directory")
        exit(1)
import pygame,datetime
from mutagen.mp3 import MP3

termlen = [int(cmd.cmdrun("tput cols")),int(cmd.cmdrun("tput lines"))]
constterm = [int(cmd.cmdrun("tput cols")),int(cmd.cmdrun("tput lines"))]
music_file = sys.argv[1]
musix = MP3(sys.argv[1])
def playa():
    pygame.mixer.init()
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(0)
playa()
durmil = ""
thingprint = ""
for i in range(termlen[1]):
    thingprint+=" "
rset = "\033["+str(termlen[0])+"D\033["+str(termlen[1])+"A"
stdscr = curses.initscr()
back = "\033["+str(termlen[0])+"D"
curses.noecho()
stdscr.keypad(True)
stdscr.timeout(60)
print("\033[?25l",end="")
ispaused = False
pausething = ""
title = ""
repeat = False
repeatthing = ""
samplerate = ""
s = False
border = back+"=["
durlen = ""

while True:
    try:
        termlen = [int(cmd.cmdrun("tput cols")),int(cmd.cmdrun("tput lines"))]
        if constterm[0] == termlen[0]:
            print("",end='')
        else:
            os.system('clear')
            constterm = [int(cmd.cmdrun("tput cols")),int(cmd.cmdrun("tput lines"))]
        if constterm[1] == termlen[1]:
            print("",end='')
        else:
            os.system('clear')
            constterm = [int(cmd.cmdrun("tput cols")),int(cmd.cmdrun("tput lines"))]
        text = "Simple Music Player"
        lines = (termlen[0] - len(text)) // 2
        title = " "
        #asart = cmd.cmdrun("jp2a --colors "+sys.argv[2]).replace("\n","\033["+str(termlen[0])+"D\n")
        border = back+"=["
#        for i in range(int(termlen[0]/3)):
 #           title += " "
        for i in range(termlen[0]-1):
            title += " "
        key = stdscr.getch()
    # Memeriksa apakah tombol 'q' ditekan
        if key == ord('q') or key == 27:
            print("Tombol Q Ditekan")
            break
        elif key == ord('p'):
            if ispaused == False:
                pausething = " (Paused)"
                pygame.mixer.music.pause()
                ispaused = True
            elif ispaused == True:
                pausething = ""
                pygame.mixer.music.unpause()
                ispaused = False
        elif key == ord('r'):
            if repeat == False:
                repeat = True
                repeatthing = " (Repeat)"
            else:
                repeat = False
                repeatthing = ""
        elif key == curses.KEY_UP:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.05)
        elif key == curses.KEY_DOWN:
            pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.05)
        samplerate = back+"\nSample Rate: "+str(musix.info.sample_rate)+"Hz"
        print(rset,end='')
        curses.raw()
        stdscr.attron(curses.A_REVERSE)
        stdscr.addstr(0,0,title)
        stdscr.addstr(0,lines,text)
        stdscr.attroff(curses.A_REVERSE)
        stdscr.refresh()
        print("\033[37;27m\n")
        whowins = 0
        if termlen[0] >= termlen[1]:
            whowins = termlen[1]
        else:
            whowins = termlen[0]
        if len(sys.argv) == 3:
            asart = cmd.cmdrun("jp2a --colors "+sys.argv[2]+" --width="+str(whowins))
            asartraw = cmd.cmdrun("jp2a "+sys.argv[2]+" --width="+str(whowins))
            asartm = (termlen[0] - len(asartraw.split("\n")[0])) // 2
            asartmod = asart.replace("\n","\033["+str(termlen[0])+"D\033["+str(asartm)+"C\n")
            print("\033["+str(asartm)+"C"+asartmod)
        durmil = pygame.mixer.music.get_pos()
        millisecondd = datetime.timedelta(milliseconds=pygame.mixer.music.get_pos())
        milliseconds = datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(millisecondd.total_seconds()), "%H:%M:%S")
        milliseconds1 = datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(musix.info.length), "%H:%M:%S")
        seconds = float(datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(millisecondd.total_seconds()), "%S.%f"))
        if key == curses.KEY_LEFT:
             pygame.mixer.init()
             pygame.mixer.music.load(music_file)
             pygame.mixer.music.play(start=0)
        #milliseconds = datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(durmil), "%D:%H:%M:%S")
        playing = music_file.split("/")[len(music_file.split("/"))-1]
        playingcount = (termlen[0] - len(playing)) // 2
        print("\033["+str(termlen[0])+"D"+"\033["+str(playingcount)+"C"+playing)
        dur = "["+str(milliseconds)+" - "+str(milliseconds1)+"]"+pausething+repeatthing
        if len(durlen) == (termlen[0] - len(dur)) // 2:
            durlen += ""
        else:
            durlen = ""
            for i in range((termlen[0] - len(dur)) // 2):
                durlen += " "

        print("\033["+str(termlen[0])+"D"+durlen+""+dur+"                   ")
        print("\033[1A\033["+str(termlen[0])+"D"+"\033["+str(termlen[1]+1)+"A")
        print("\033[1A",end='')
        if milliseconds == milliseconds1:
            if repeat == True:
                playa()
            else:
                os.system('clear')
                print("\033[?47l")
                print("\033[?25h",end="")
                exit()
        #hai
    except KeyboardInterrupt:
        os.system("clear")
        print("\033[?25h",end="")
        print("\033[?47l")
        exit()

print("\033[?25h",end="")
curses.endwin()
