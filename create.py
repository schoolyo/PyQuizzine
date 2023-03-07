from quizpy import Quiz, Category, MultipleChoice, ShortAnswer, Numerical
import os
import re
import tkinter as tk
from tkinter import font as tkfont


class QuizApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.quiz = Quiz()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        for F in (CreateQuiz, StartPage, MakeMC, MakeNumerical, ExportXML):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CreateQuiz")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class CreateQuiz(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def save(name):
            controller.quiz = controller.quiz.add_category(name)
            controller.show_frame("StartPage")
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)

        label = tk.Label(self, text="First, you need to initialize some attributes of your quiz", font=controller.title_font)
        l1 = tk.Label(self, text="Quiz Name")
        e1 = tk.Entry(self)
        button = tk.Button(self, text="Initialize Quiz", command=lambda: save(e1.get()))
        label.grid(row=0, column=1, columnspan=2)
        l1.grid(row=2, column=0, sticky="E")
        e1.grid(row=2, column=1, sticky="W")
        button.grid(row=3, column=1)



class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="What question type do you want to create?", font=controller.title_font)
        button1 = tk.Button(self, text="Multiple Choice",
                            command=lambda: controller.show_frame("MakeMC"))
        button2 = tk.Button(self, text="Numerical",
                            command=lambda: controller.show_frame("MakeNumerical"))
        button3 = tk.Button(self, text="Export Quiz",
                            command=lambda: controller.show_frame("ExportXML"))
        label.grid(row=0, column=2, rowspan=2)
        button1.grid(row=3, column=2)
        button2.grid(row=4, column=2)
        button3.grid(row=5, column=2)


class MakeMC(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def save():
            controller.quiz # need to save the entries to a multiple choice object, then append to quiz object
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="MakeMC", font=controller.title_font)
        e1 = tk.Entry(self)
        l1 = tk.Label(self, text="Correct Answer")
        e2 = tk.Entry(self)
        l2 = tk.Label(self, text="Incorrect Answer")
        e3 = tk.Entry(self)
        l3 = tk.Label(self, text="Incorrect Answer")
        e4 = tk.Entry(self)
        l4 = tk.Label(self, text="Incorrect Answer")
        e5 = tk.Entry(self)
        l5 = tk.Label(self, text="Question")
        e6 = tk.Entry(self)
        l6 = tk.Label(self, text="Points for getting the question correct") # need to add this entry for the points per question
        button1 = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button2 = tk.Button(self, text="Save Question") # need to add command to the submit button
        label.grid(row=0, column=2, pady=10)
        button1.grid(row=0, column=0, pady=2)
        l5.grid(row=0, column=1, sticky="E")
        e5.grid(row=0, column=1, sticky="W")
        l1.grid(row=1, column=1, sticky="E")
        e1.grid(row=1, column=2, sticky="W")
        l2.grid(row=2, column=1, sticky="E")
        e2.grid(row=2, column=2, sticky="W")
        l3.grid(row=3, column=1, sticky="E")
        e3.grid(row=3, column=2, sticky="W")
        l4.grid(row=4, column=1, sticky="E")
        e4.grid(row=4, column=2, sticky="W")




class MakeNumerical(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="Make Numerical", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class ExportXML(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="Export XML", font=controller.title_font)
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

app = QuizApp(className=" PyQuizzine")
app.geometry("800x600")
app.mainloop()