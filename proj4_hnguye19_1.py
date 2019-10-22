#Hang Nguyen
#Top down design 1
#COM110
#Professor Chung
#Nov. 1, 2018


from graphics import *
from random import *
from buttonclass import*

def main():
    #draw GUI for intro, button, input...
    wordDict() #put the words into a dictionary
    freq() #order the dictionary based on the frequency of the words
    wordSize() #adjust word size
    checkLocation() #collision avoidance
main()
