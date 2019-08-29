#!/usr/bin/env python3

import utils
import time
import sys

utils.check_version((3,7))
utils.clear()

def sim_type(str):                  #\
    for letter in str:              # |
        sys.stdout.write(letter)    #  } This section of code was use from one of my older projects form high school
        sys.stdout.flush()          # |
        time.sleep(.05)             #/

sim_type ('Hello, my name is Bryce Whitmer')
print (' ')
name = input('Whats your name? ')
sim_type ('Nice to meet you {name}'.format(name=name))
time.sleep(1)
print (' ')
sim_type ('I guess I will tell you a little bit about myself')
time.sleep(1)
print (' ')
sim_type ('I have played many games on my pc, and my steam library is a testament to that')
print (' ')
sim_type ('If I had to choose what games I enjoy the most it would probably be ARK:Survival Evolved')
print (' ')
sim_type ('But the game I play the most would have to be Minecraft')
time.sleep(1)
print (' ')
sim_type ('I dont really have any concerns about this class although it is not what I expected')
print (' ')
sim_type ('The discription of this class online was very different, but I do not mind this is what I was hoping for')
time.sleep(1)
print (' ')
sim_type ('What excites me is playing games with my friends in my free time')
time.sleep(1)
print (' ')
sim_type ('Ok now its time for the basic stuff')
print (' ')
sim_type ('My stackoverflow user number is: 11996596')
print (' ')
sim_type ('And the URL to my github profile is: https://github.com/brywhitm')
time.sleep(2)
print (' ')
sim_type ('I know a lot of this code is redundant but I wanted a nice look insted of a massive paragraph with all of the info')
# I could have easly just put one print down and typed everything into it but what fun would that have been :)