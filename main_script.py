import random
import time
from colorama import Fore, Back, Style
import playing_f
import  styles_f


print(Fore.RED + "______________________WELCOME__________________________")
print(Style.RESET_ALL)

#TEAM AND OVER SETTINGS

over = int(input("SET THE OVER : "))
u_teamN = input("ENTER YOUR TEAM NAME : ")
tN_file = open("team_names.txt","r")
pl_ch = 00

for line in tN_file:
    c_teamN = random.choice(line.split())
    while(c_teamN == u_teamN):
        c_teamN = random.choice(line.split())
styles_f.divider()

print("YOUR TEAM     : ",u_teamN)
print("COMPUTER TEAM : ",c_teamN)
print("OVER          : ",over)

styles_f.divider()

#TOSSING ACTIVITIES

print("--TOSSING PROCESS--")
print("ENTER YOUR CHOICE (H/T) : ")
ch = input()
print("PLEASE WAIT ...." )
time.sleep(0)
toss_li=['H','T']
toss = random.choice(toss_li)
if(toss == ch.upper()):
    print(Fore.GREEN +"\nYOU WON THE TOSS"+Style.RESET_ALL)
    print("CHOICE IS YOURSE :\n1)BATING \n2)BOWLING")
    pl_ch = int(input())
else:
    print(Fore.RED +"\nYOU LOST THE TOSS"+Style.RESET_ALL)
    com_ch = random.choice(['BATING','BOWLING'])
    print("\n"+c_teamN+" CHOOSED ",com_ch)

#caling to play
first = 1
second = 2
if (pl_ch == 1):

    playing_f.playing(u_teamN, over, first)
    playing_f.playing(c_teamN, over, second)

else:

    playing_f.playing(c_teamN, over, first)
    playing_f.playing(u_teamN, over, second)

styles_f.divider()


