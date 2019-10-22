# buttonClass.py
from graphics import *


class Button:

    """A button is a labeled rectangle in a window.
    It is enabled or disabled with the activate()
    and deactivate() methods. The clicked(pt) method
    returns True if and only if the button is enabled and pt is inside it."""

    def __init__(self, win, center, width, height, label):
        ## as you read through this, ask yourself:  what are the instance variables here?
        ## it would be useful to add comments describing what some of these variables are for...
        """ Creates a rectangular button, eg:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        ## you should comment these variables...
        self.xmax, self.xmin = x+w, x-w 
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.activate() ##this line was not there in class, what does it do?

    
    def getLabel(self):
        """Returns the label string of this button."""
        return self.label.getText()

    def changeLabel(self,string):
        return self.label.setText(string)

    def activate(self):
        """Sets this button to 'active'."""
        self.label.setFill('black') #color the text "black"
        self.rect.setWidth(2)       #set the outline to look bolder
        self.active = True          #set the boolean variable that tracks "active"-ness to True

    ##check 3.  complete the deactivate() method
    def deactivate(self):
        """Sets this button to 'inactive'."""
        self.label.setFill('grey')  ##color the text "darkgray"
        self.rect.setWidth(1)       ##set the outline to look finer/thinner
        self.active = False         ##set the boolean variable that tracks "active"-ness to False

    ##check 4.  complete the clicked() method
    def isClicked(self, p):
        """Returns true if button active and Point p is inside"""
        ##your code here
        while not self.active or (not (p.getX() >= self.xmin and p.getX() <= self.xmax and p.getY() >= self.ymin and p.getY() <= self.ymax)):
            return False
            
        return True
    
def main():
    ##check 2. create a graphical window in which to test the Button class
    win = GraphWin("Lab 9", 200,200)
    
    ##check 3. test the Button constructor method...
    ##create two Button objects, one for "Roll Dice" and the other for "Quit"
    button1 = Button(win, Point(100,120), 100, 20, "Roll Dice")
    button2 = Button(win, Point(100,180), 50, 20, "Quit")
    ##activate the Roll button
    button1.activate()

    ##check 4. now test the deactivate() method...
    ##deactivate the "Quit" button
    button2.deactivate()

    
    pt = win.getMouse()
    ##check 5. test the .clicked() method with an if statement
    ##(remove this test code before moving onto the next check)
    #if button1.isClicked(pt):
    #    print("Roll button was clicked")
    #else:
    #    print("Roll button wasn't clicked")

    
    ##check 6: 
    ##loop until the "Quit" button is clicked...
        ##if the roll button is clicked
            ##activate the quit button
        ##take the next mouse click


    while not button2.isClicked(pt):
        if button1.isClicked(pt):
            button2.activate()
        pt = win.getMouse()
        
    #we reach this line of code when quit button is clicked b/c loop condition breaks
    win.close() #so close the window, ending the program
    
if __name__ == "__main__": 
    main()
