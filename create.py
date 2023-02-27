from quizpy import Quiz, Category, MultipleChoice, ShortAnswer, Numerical
import os
import re
import tkinter as tk
from tkinter import font as tkfont

class QuizApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll pack the current page
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.current_frame = None

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""

        # destroy the old page, if there is one
        if self.current_frame is not None:
            self.current_frame.destroy()

        # create the new page and pack it in the container
        cls = globals()[page_name]
        self.current_frame = cls(self.container, self)
        self.current_frame.pack(fill="both", expand=True)


class Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
    def show_frame(self, page_name):
"""
TO DO:
finish the Page class
make other pages child objects of the Page class
make the show_frame method actually work
"""



class StartPage(tk.Frame):
    def __int__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Multiple Choice",
                            command=lambda: controller.show_frame("MakeMC"))
        button2 = tk.Button(self, text="Numerical",
                            command=lambda: controller.show_frame("MakeNumerical"))
        button3 = tk.Button(self, text="Export Quiz",
                            command=lambda: controller.show_frame("ExportXML"))
        button1.pack()
        button2.pack()
        button3.pack()


class MakeMC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class MakeNumerical(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

class ExportXML(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 3", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()

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

app = QuizApp()
app.mainloop()