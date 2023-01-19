from quizpy import *
import os

def makeQuestions():
    while True:


def makeMC(mc):
    title = input("What is the question title?: ")
    question = input("What is the question?:" )
    points = float(input("How many points for getting this question correct?: ")) # need to make this check user input
    # need to create the question object, figure out how I'm using the parameter, and make a loop for adding answer choices

def makeNumerical():
    pass

def makeSA():
    pass

def clearScreen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")