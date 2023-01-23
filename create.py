from quizpy import *
import os

def makeQuestions():
    while True:
        title = input("What is the question title?: ")
        question = input("What is the question?:")
        points = float(input("How many points for getting this question correct?: "))
        clearScreen()
        while True:
            qType = input("What kind of question do you want to make?: \n1) Multiple Choice\n2) Numerical\n3) Short Answer\n")
            clearScreen()
            if intInRange(qType, 1, 3):
                if qType == 1:
                    mc = MultipleChoice(title, question, points)
                    makeMC(mc)
                    clearScreen()
                    break
                elif qType == 2:
                    num = Numerical(title, question, points)
                    answer = float(input("What is the correct numerical answer?: "))  # maybe should do input checking on this line
                    num.add_answer(answer, 100.0, "Correct!")
                    clearScreen()
                    break
                elif qType == 3:
                    sa = ShortAnswer(title, question, points)
                    answer = input("What is the correct answer?: ")
                    sa.add_answer(answer, 100.0, "Correct!", "plain_text")
                    clearScreen()
                    break

        done = input("Are you done creating questions?:\n1) Yes\n2) No\n")
        if intInRange(done, 1, 2):
            if done == "1":
                clearScreen()
                break
            elif done == "2":
                clearScreen()


def makeMC(mc):
    while True:
        choice = input("Enter an answer choice: ")
        correct = input("is this the correct answer?\n1) Yes\n2) No\n")
        clearScreen()
        if intInRange(correct, 1, 2):
            if correct == "1":
                mc.add_choice(choice, 100.0, "correct!")
            elif correct == "2":
                mc.add_choice(choice, 0.0, "incorrect!")
        done = input("Are you done inputting answer choices?\n1) Yes\n2) No\n")
        if intInRange(done, 1, 2):
            if done == "1":
                clearScreen()
                break
            elif done == "2":
                clearScreen()

def clearScreen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def intInRange(num, start, stop):
    try:
        num = int(num)
        if num < start or num > stop:
            raise Exception("number is out of range")
        return True
    except:
        return False

makeQuestions()