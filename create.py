from quizpy import Quiz, Category, MultipleChoice, ShortAnswer, Numerical
import os
import re

def makeQuestions():
    """
    Creates a Quiz object and adds questions to it using user input

    :return: a Quiz object q
    :type q: Quiz
    """
    q = Quiz()
    qName = input("What is the name of the quiz?: ")
    qCategory = q.add_category(qName)
    while True: # loop for creating all questions
        title = input("What is the question title?: ")
        question = input("What is the question?:")
        points = float(input("How many points for getting this question correct?: "))
        clearScreen()
        while True: # loop for creating a single question
            try:
                qType = int(input("""What kind of question do you want to make?: 
                1) Multiple Choice
                2) Numerical
                3) Short Answer\n"""))
            except:
                raise ValueError("input does not meet the conditions")
            clearScreen()

            if 1 <= qType <= 3:
                if qType == 1: # create Multiple Choice question & append to category
                    mc = MultipleChoice(title, question, points)
                    makeMC(mc)
                    qCategory.questions.append(mc)
                    clearScreen()
                    break
                elif qType == 2: # create Numerical question & append to category
                    num = Numerical(title, question, points)
                    answer = float(input("What is the correct numerical answer?: "))
                    num.add_answer(answer, 100.0, "Correct!")
                    qCategory.questions.append(num)
                    clearScreen()
                    break
                elif qType == 3: # create Short Answer question & append to category
                    sa = ShortAnswer(title, question, points)
                    answer = input("What is the correct answer?: ")
                    sa.add_answer(answer, 100.0, "Correct!", "plain_text")
                    qCategory.questions.append(sa)
                    clearScreen()
                    break

        try:
            done = int(input("Are you done creating questions?:\n1) Yes\n2) No\n"))
        except:
            raise ValueError("Number did not match the input requirements")
        if 1 <= done <= 2:
            if done == 1: # done creating questions
                clearScreen()
                break
            elif done == 2: # not done
                clearScreen()
    return q # the quiz object


def exportXML(qz, fname):
    """
    exports Quiz object as XML file

    :param qz: Quiz object that contains the questions and answers
    :type qz: Quiz
    :param fname: name for exported file
    :type fname: str
    """
    fname = re.sub(" ", "_", fname.lower())
    for i in fname:
        if re.match(r"\W", i):
            fname = fname.replace(i, "", 1)
        else:
            break
    fname += ".xml"
    qz.export(fname)


def makeMC(mc):
    """
    creates a MultipleChoice question object using user input

    :param mc: MultipleChoice object
    """
    while True:
        choice = input("Enter an answer choice: ")
        try:
            correct = int(input("is this the correct answer?\n1) Yes\n2) No\n"))
        except:
            raise ValueError("Number did not meet input requirements")
        clearScreen()
        if 1 <= correct <= 2:
            if correct == 1: # is correct answer
                mc.add_choice(choice, 100.0, "correct!")
            elif correct == 2: # isn't correct answer
                mc.add_choice(choice, 0.0, "incorrect!")
        try:
            done = int(input("Are you done inputting answer choices?\n1) Yes\n2) No\n"))
        except:
            raise ValueError("Number did not meet the input requirements")
        if 1 <= done <= 2:
            if done == 1: # done with answer choices
                clearScreen()
                break
            elif done == 2: # not done with answer choices
                clearScreen()


def clearScreen():
    """clears the terminal of any text"""
    if os.name == "posix": # linux or mac
        os.system("clear")
    else: # windows
        os.system("cls")

exportXML(makeQuestions(), "test")

