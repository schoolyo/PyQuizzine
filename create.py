from quizpy import Quiz, Category, MultipleChoice, ShortAnswer, Numerical
import os
import re

def makeQuestions():
    """
    Creates a Quiz object and adds questions to it using user input

    :return: a Quiz object q
    :type q: Quiz
    """
    count = 1
    q = Quiz()
    qName = input("What is the name of the quiz?: ")
    qCategory = q.add_category(qName)
    while True: # loop for creating all questions
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
                    mc = MultipleChoice(f"q{count}", question, points)
                    makeMC(mc)
                    qCategory.questions.append(mc)
                    clearScreen()
                    count += 1
                    break
                elif qType == 2: # create Numerical question & append to category
                    num = Numerical(f"q{count}", question, points)
                    answer = float(input("What is the correct numerical answer?: "))
                    num.add_answer(answer, 100.0, "Correct!")
                    qCategory.questions.append(num)
                    clearScreen()
                    count += 1
                    break
                elif qType == 3: # create Short Answer question & append to category
                    sa = ShortAnswer(f"q{count}", question, points)
                    answer = input("What is the correct answer?: ")
                    sa.add_answer(answer, 100.0, "Correct!", "plain_text")
                    qCategory.questions.append(sa)
                    clearScreen()
                    count += 1
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
    return q


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
    count = 0
    while count < 4:
        choice = input("Enter an answer choice: ")
        try:
            correct = int(input("is this the correct answer?\n1) Yes\n2) No\n"))
        except:
            raise ValueError("Number did not meet input requirements")
        clearScreen()
        if 1 <= correct <= 2:
            count += 1
            if correct == 1: # is correct answer
                mc.add_choice(choice + "_", 100.0, "correct!")
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


quiz = makeQuestions()
name = input("What is the filename?")
exportXML(quiz, name)
