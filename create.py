from quizpy import Quiz, Category, MultipleChoice, ShortAnswer, Numerical
import re
import tkinter as tk
from tkinter import font as tkfont


class QuizApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.quiz = Quiz()
        self.count = 1

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
            controller.qName = controller.quiz.add_category(name)
            controller.show_frame("StartPage")
            controller.count += 1
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
        button.grid(row=2, column=1)


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
            self.mc = MultipleChoice(f"q{controller.count}", e5.get(), e6.get())
            self.mc.add_choice(e1.get(), 100.0, "Correct!")
            for entry in (e2, e3, e4):
                if entry:
                    self.mc.add_choice(entry.get(), 0.0, "Incorrect!")
            controller.qName.questions.append(self.mc)
            controller.show_frame("StartPage")
            controller.count += 1

        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="MakeMC", font=controller.title_font)
        l5 = tk.Label(self, text="Question")
        e5 = tk.Entry(self)
        e1 = tk.Entry(self)
        l1 = tk.Label(self, text="Correct Answer")
        e2 = tk.Entry(self)
        l2 = tk.Label(self, text="Incorrect Answer")
        e3 = tk.Entry(self)
        l3 = tk.Label(self, text="Incorrect Answer")
        e4 = tk.Entry(self)
        l4 = tk.Label(self, text="Incorrect Answer")
        e6 = tk.Entry(self)
        l6 = tk.Label(self, text="Points for getting the question correct")
        button2 = tk.Button(self, text="Save Question",
                            command=lambda: save())
        button1 = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        label.grid(row=0, column=2, pady=10)
        button1.grid(row=0, column=0, pady=2)
        l5.grid(row=1, column=1, sticky="E")
        e5.grid(row=1, column=2, sticky="W")
        l1.grid(row=2, column=1, sticky="E")
        e1.grid(row=2, column=2, sticky="W")
        l2.grid(row=3, column=1, sticky="E")
        e2.grid(row=3, column=2, sticky="W")
        l3.grid(row=4, column=1, sticky="E")
        e3.grid(row=4, column=2, sticky="W")
        l4.grid(row=5, column=1, sticky="E")
        e4.grid(row=5, column=2, sticky="W")
        l6.grid(row=7, column=1, sticky="W")
        e6.grid(row=7, column=2, sticky="E")
        button2.grid(row=8, column=2, pady=2)


class MakeNumerical(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def save():
            self.num = Numerical(f"q{controller.count}", e1.get(), e3.get())
            self.num.add_answer(e2.get(), 100.0, "Correct!")
            controller.qName.questions.append(self.num)
            controller.show_frame("StartPage")
            controller.count += 1
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="Make Numerical", font=controller.title_font)
        button1 = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        l1 = tk.Label(self, text="Question")
        e1 = tk.Entry(self)
        l2 = tk.Label(self, text="Correct numerical answer")
        e2 = tk.Entry(self)
        l3 = tk.Label(self, text="Points for correct answer")
        e3 = tk.Entry(self)
        button2 = tk.Button(self, text="Save Question", command=lambda: save())
        label.grid(row=0, column=1, columnspan=2, pady=10)
        button1.grid(row=0, column=0, sticky="NW")
        l1.grid(row=2, column=1, sticky="E")
        e1.grid(row=2, column=2, sticky="W")
        l2.grid(row=3, column=1, sticky="E")
        e2.grid(row=3, column=2, sticky="W")
        l3.grid(row=4, column=1, sticky="E")
        e3.grid(row=4, column=2, sticky="W")
        button2.grid(row=5, column=0, sticky="W")


class ExportXML(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def save(fname):
            fname = re.sub(" ", "_", fname.lower())
            for char in fname:
                if re.match(r"\W", char):
                    fname = fname.replace(char, "", 1)
                else:
                    break
            fname += ".xml"
            controller.quiz.export(fname)
            controller.destroy()
        for i in range(5):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
        label = tk.Label(self, text="Export XML", font=controller.title_font)
        button1 = tk.Button(self, text="Go to the start page",
                            command=lambda: controller.show_frame("StartPage"))
        l1 = tk.Label(self, text="Filename")
        e1 = tk.Entry(self)
        button2 = tk.Button(self, text="Save and export quiz",
                            command=lambda: save(e1.get()))
        label.grid(row=0, column=1, rowspan=2, pady=10)
        button1.grid(row=0, column=0, sticky="NW")
        l1.grid(row=2, column=1, sticky="E")
        e1.grid(row=2, column=2, sticky="W")
        button2.grid(row=0, column=5, sticky="NE")


app = QuizApp(className=" PyQuizzine")
app.geometry("800x600")
app.mainloop()
