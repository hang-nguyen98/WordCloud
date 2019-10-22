#Hang Nguyen
#Top down design 2
#COM110
#Professor Chung
#Nov. 1, 2018


from graphics import *
from random import *
from buttonclass import*

               
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
            xMinList, xMaxList, yMinList, yMaxList,wordCloudList = [],[],[],[],[]

            size = 50 #maximun font size

            for i in range(n):
                word = items[i][0] #display the word and not the frequency
                sizeList = wordSize(n,size,word) #adjust word size
                while not checkLocation(): #collision avoidance
                    #append new center point for the new word
                    checkLocation() #check again until the location satisfies the condition

                #After having a qualified location, calculate xMin, xMax, yMin, yMax and put them into lists for future references
                xMax = int(xCenter + len (word) * sizeList[i] * 0.3)
                xMin = int(xCenter - len (word) * sizeList[i] * 0.3)
                yMax = int(yCenter + sizeList[i] * 0.6)
                yMin = int(yCenter - sizeList[i] * 0.6)
                xMinList.append(xMin)
                xMaxList.append(xMax)
                yMinList.append(yMin)
                yMaxList.append(yMax)

                wordCloud = drawText(win, Point(xCenter,yCenter), sizeList[i], word)    
                wordCloud.setFill(color_rgb(randrange(0,255),randrange(0,255),randrange(0,255)))  #random color
                wordCloudList.append(wordCloud) #put each word into a list for undraw/recreate.

                
                
main()
