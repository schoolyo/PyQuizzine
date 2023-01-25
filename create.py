from quizpy import Quiz, Category, MultipleChoice, ShortAnswer, Numerical
import os
import re

quiz = Quiz()
quizQuestions = quiz.add_category("example category")
def makeQuestions():
<<<<<<< HEAD
    #while True:
    pass
=======
    while True:
        title = input("What is the question title?: ")
        question = input("What is the question?:")
        points = float(input("How many points for getting this question correct?: "))
        clearScreen()
        while True:
            try:
                qType = int(input("""What kind of question do you want to make?: 
                1) Multiple Choice
                2) Numerical
                3) Short Answer\n"""))
            except:
                raise ValueError("input does not meet the conditions")
            clearScreen()

            if 1 <= qType <= 3:
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

        try:
            done = int(input("Are you done creating questions?:\n1) Yes\n2) No\n"))
        except:
            raise ValueError("Number did not match the input requirements")
        if 1 <= done <= 2:
            if done == 1:
                clearScreen()
                break
            elif done == 2:
                clearScreen()


def exportXML(qz, fname, *qs):
    qz.questions.extend(qs)

    qz.export(fname)
>>>>>>> 1ccff9af458bb627aafa841c9e4e831b873a0cf5


def makeMC(mc):
    while True:
        choice = input("Enter an answer choice: ")
        try:
            correct = int(input("is this the correct answer?\n1) Yes\n2) No\n"))
        except:
            raise ValueError("Number did not meet input requirements")
        clearScreen()
        if 1 <= correct <= 2:
            if correct == 1:
                mc.add_choice(choice, 100.0, "correct!")
            elif correct == 2:
                mc.add_choice(choice, 0.0, "incorrect!")
        try:
            done = int(input("Are you done inputting answer choices?\n1) Yes\n2) No\n"))
        except:
            raise ValueError("Number did not meet the input requirements")
        if 1 <= done <= 2:
            if done == 1:
                clearScreen()
                break
            elif done == 2:
                clearScreen()


def clearScreen():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
