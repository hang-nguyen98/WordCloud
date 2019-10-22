#Hang Nguyen
#Programming Assignment 4
#COM110
#Professor Chung
#Nov. 1, 2018


from graphics import *
from random import *
from buttonclass import *

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


def freq(wDict,pair):
    items = list(wDict.items()) 
    items.sort(key = getKey, reverse = True) #order by frequency
    return items


def wordSize(n, sizeList, output): #wordSize
    sizeList = []
    size = 70 #maximum size
    for i in range(n):    
        sizeList.append(size)
        size = round(size/1.05) #set smaller size for words
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
                if xMax>800 or xMin<0 or (xMinList[i] < x < xMaxList[i] and yMinList[i] < y < yMaxList[i]):
                
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


def undraw(wordCloudList):
    for j in range(len(wordCloudList)):
        wordCloudList[j].undraw()


def main():
    win = GraphWin("Word Cloud Generator", 800, 750)

    intro = drawText(win, Point(400,200), 20, "Welcome to Word Cloud Generator Program! \n\n\
This program will create a word cloud from a text of your choice,\n or from the default file. \
This is useful as a visual representation of\n text analysis, as the size of each word represents \
its frequency in the text.")

    #Create button:
    button1 = Button (win, Point (200, 680), 100, 40, "Start")
    button2 = Button (win, Point (600, 680), 100, 40, "Quit")
    button2.deactivate()

    pt = win.getMouse()
    while not button1.isClicked(pt): #does not do anything until the user click 'Start' button
        pt = win.getMouse()

    #once the user clicked 'Start' button, remove it and the intro line and activate 'Quit button'.
    button1.changeLabel("Create")
    button2.activate()
    button3 = Button(win,Point(400,680),100,40, "Clear")
    button3.deactivate()
    intro.undraw()
        
    #ask user to input filename input("Please type the file name: ")
    textBox = inputBox (win,Point(400,75), 50, "white")
    numBox = inputBox (win, Point(400,150), 30, "white")

    textPrompt = drawText (win, Point(400,50), 15, "Please enter the file name: (e.g: TSA.txt) ")    
    numPrompt = drawText (win, Point(400,125), 15, "Please enter the number of words you want to display (best if less than 100): ")
    
    display = Text (Point(400,180), "")
    display.draw(win)
    pt = win.getMouse()
    textStr = textBox.getText()
    n = numBox.getText()
      

    while not button2.isClicked(pt):
        warning =""
        if button1.isClicked(pt):
            if n == "" or n == "0" or (not n.isnumeric()): #Does not turn the key to an integer until the program checks if the user input an integer.
                warning = "Please enter an integer greater than 0 in the key box."
            elif textStr == "":
                warning = "Please enter a file name."
            else:
                n = int(n) #after the user entered an integer, turn n into an int() type to avoid program crash.
                textfile = open(textStr, "r").read()
                text = textfile.lower()
                
                stopWordFile = open("stopwords.txt","r").read()
                                
                wDict = wordDict(text, stopWordFile)
                items = freq(wDict,getKey)
                
                if n > len(items): #if the user enter a larger number than the number of unique words:
                    n = len(items)
                    warning = "Your chosen number is greater than the unique words in the text.\n\
The program will display the word cloud of all unique words in the text."
                    


                #Calculate the location of the first word:
                xCenter,yCenter = randrange(100,700),randrange(200,550) #get a random coordinate for the text
                xMinList, xMaxList, yMinList, yMaxList,wordCloudList = [],[],[],[],[]

                size = 50 #maximum font size
                

                
                #create a for loop to iterate through lists:
                for i in range(n):
                    word = items[i][0] #display the word and not the frequency of the tuple
                    sizeList = wordSize (n, size, word)
                    
                    while checkLocation(word,sizeList[i], xCenter,yCenter, xMinList,xMaxList,yMinList,yMaxList) is False:
                        xCenter,yCenter = randrange(100,700),randrange(200,600)
                        newLocation = checkLocation(word,sizeList[i], xCenter,yCenter,xMinList,xMaxList,yMinList,yMaxList)

                    #After having a qualified location, calculate xMin, xMax, yMin, yMax and put them into lists for future references
                    xMax = int(xCenter + len (word) * sizeList[i] * 0.3)
                    xMin = int(xCenter - len (word) * sizeList[i] * 0.3)
                    yMax = int(yCenter + sizeList[i] * 0.6)
                    yMin = int(yCenter - sizeList[i] * 0.6)
                    xMinList.append(xMin)
                    xMaxList.append(xMax)
                    yMinList.append(yMin)
                    yMaxList.append(yMax)
                  
                    #when we have the coordinate, start drawing the word cloud
                    wordCloud = drawText(win, Point(xCenter,yCenter), sizeList[i], word)    
                    wordCloud.setFill(color_rgb(randrange(0,255),randrange(0,255),randrange(0,255)))  #random color
                    wordCloudList.append(wordCloud) #put each word into a list for undraw/recreate.

                    button3.activate()
                    
                        

        display.setText(warning)
        display.setFill("blue3")
        display.setStyle("bold")
            
        

        
        #when the user want to clear the canvas:
        if button3.isClicked(pt):
            undraw(wordCloudList)

        textStr = textBox.getText()
        n = numBox.getText()
        pt = win.getMouse()
        
        
                        
    win.close()
                
            

    
main()

