"""
A Python function, fizzBuzz(), prints
a sequence of numbers and words based
on the set of "FizzBuzz" rules.
"""

import maya.cmds as cmds
import os, sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

def resource_path(relative_path):
    base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

form = resource_path("main.ui")
CLASS_FORM = uic.loadUiType(form)[0]

class MainUi(QMainWindow, CLASS_FORM):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.fizzbuzz = FizzBuzz

class FizzBuzz:
    def fizzBuzz():
        for Number in range (1, 51):
            #Prints FizzBuzz for Multiples of 4 and 9
            if Number % 4 == 0 and Number % 9 == 0:
                print ("FizzBuzz")
            #Prints Fizz for Multiples of 4
            elif Number % 4 == 0:
                print ("Fizz")
            #Prints Buzz for Multiples of 9
            elif Number % 9 == 0:
                print ("Buzz")
            #Prints Number for Anything Else
            else:
                print (Number)

    def fizzBuzzList():
        #Collects and Prints Fizz Numbers into a List
        fizzMultiples = []
        for Number in range (1,51):
            if Number % 4 == 0:
                fizzMultiples.append((Number))
        print ('Fizz Multiples :', (fizzMultiples))
        #Collects and Prints Buzz Numbers into a List
        buzzMultiples = []
        for Number in range (1,51):
            if Number % 9 == 0:
                buzzMultiples.append((Number))
        print ('Buzz Multiples :', (buzzMultiples))
        #Collects and Prints FizzBuzz Numbers into a List
        fizzBuzzMultiples = []
        for Number in range (1, 51):
            if Number % 4 == 0 and Number % 9 == 0:
                fizzBuzzMultiples.append((Number))
        print ('FizzBuzz Multiples :', (fizzBuzzMultiples))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainUi()
    mainWindow.show()
    app.exec()