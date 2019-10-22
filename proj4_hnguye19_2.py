#Hang Nguyen
#Top down design 2
#COM110
#Professor Chung
#Nov. 1, 2018

from graphics import *
from random import *
from buttonclass import*


def wordDict(text, stopWordFile): #remove punctuation and stop words, and put the words into a dictionary.
    for char in text:
        if not (char.isalpha()): #if character is not in the alphabet
            text = text.replace(char, " ")
    wordList = text.split() #return a list of words without punctuation

    wDict = {}   #construct a dictionary of word counts
    for w in wordList: #for words without punctuation    
        if not (w in stopWordFile): #remove filler word
            wDict[w] = wDict.get(w,0) + 1
    return wDict



def getKey(pair):
    return pair[1]

def freq(wDict):
    items = list(wDict.items()) 
    items.sort(key = pair[1, reverse = True) #order by frequency
    return items


def wordSize(n, sizeList, output): #wordSize
    sizeList = []
    size = 70 #maximum size
    for i in range(n):    
        sizeList.append(size)
        size = round(size/1.1) #set smaller size for words
        if size < 15:
            size = 15 #avoid the situation where words become too small to read
        
    return sizeList



def checkLocation(output, size, xCenter, yCenter, xMinList,xMaxList,yMinList,yMaxList):
    #Determine the location by having an invisible rectangle over every word.
    #If the rectangle doesn't overlap, that location works.

    #xMax and yMax are the coordinate of the lower right corner of the rectangle
    #xMin and yMin are the coordinate of the upper left corner of the rectangle
    #Point(xMin,yMin) and Point(xMax,yMax) are 2 points to create a new rectangle
    #if those 2 points work, put the xMin, yMin, xMax, yMax into their corresponding list
    #(which will be done in the main): xMinList, yMinList, xMaxList, yMaxList.

    #each coordinate depends on the center of the word, the word length and the word size.
    #0.3 and 0.6 are estimated numbers so that the rectangle fits the text

    xMax = int(xCenter + len (output) * size * 0.3)
    xMin = int(xCenter - len (output) * size * 0.3)
    yMax = int(yCenter + size * 0.6)
    yMin = int(yCenter - size * 0.6)

    for x in range (xMin,xMax):
        for y in range (yMin,yMax):
            for i in range(len(xMinList)):
                if (xMinList[i] < x < xMaxList[i] and yMinList[i] < y < yMaxList[i]):
                
                    return False

    return True

def drawText(win, center, size, string): #function for drawing the user's instruction
    sentence = Text(center, string)
    sentence.setSize(size)
    sentence.draw(win)
    sentence.setText(string)
    return sentence

def inputBox(win,center,width,color): 
    inputBox = Entry (center,width)
    inputBox.setFill(color)
    inputBox.draw(win)
    return inputBox


def undraw(wordCloudList): #for clearing the canvas
    for j in range(len(wordCloudList)):
        wordCloudList[j].undraw()


               
def main():
    #open text file and stop words file
    #draw GUI for intro, button, input, etc. and get those inputs

    #text = open text file
    #n = number of displayed words
    pt = win.getMouse
               
    while not button2.isClicked(pt): #if user didn't click quit button
        if button1.isClicked(pt): #if user clicked create button
            wDict = wordDict(text,stopWordFile) #put the words into a dictionary
            items = freq(wDict) #tuple type (word,frequency) - order the dictionary based on the frequency of the words
            for i in range(n):
                word = items[i][0] #display the word and not the frequency
                sizeList = wordSize(n,size,word) #adjust word size
                while not checkLocation(): #collision avoidance
                    #append new center point for the new word
                    checkLocation() #check again until the location satisfies the condition

               
main()
