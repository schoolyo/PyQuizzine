import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import pandas as pd
import tkinter as tk
from tkinter import font as tkfont


class Results:
    """
    Structure the quiz csv results data
    ...
    Attributes:
    data : DataFrame representation of the quiz csv file
    numRows : integer number of rows in data
    numCols : integer number of columns in data
    """
    def __init__(self, csv_file):
        """
        Inits Results with a csv file and creates attributes data, numRows, and numCols
        Args:
            csv_file: String name of the csv file that holds the quiz data
        """
        self.data = pd.read_csv(csv_file)
        self.numRows = len(self.data.axes[0])
        self.numCols = len(self.data.axes[1])
        self.names = self.data.iloc[:, 0]
        self.times = self.data.iloc[:, 1]
        self.scores = self.data.iloc[:, 2]

    def avg_time(self):
        """
        Gets the average time the quiz was taken in
        Returns:
            A float representing the average time in seconds
        """
        return sum([i for i in self.data.iloc[:, 1] if i > 0]) / self.numRows

    def avg_score(self):
        """
        Gets the average score of all students who took the quiz
        Returns:
            A float representing the average score as a percentage
        """
        return sum([i for i in self.data.iloc[:, 2]]) / self.numRows

    def question_stats(self, num):
        """
        Gets the amount of correct and incorrect answers for a specific question
        Args:
            num: An integer for the question number wanted. num=1 would be the first question.
        Returns:
            A tuple in (percent correct, percent incorrect) format, where both are rounded to 2 decimal places
        """
        correct = round(sum([i for i in self.data.iloc[:, (num+2)] if i == 1]) / self.numRows * 100, 2)
        incorrect = 100.0 - correct
        return [correct, incorrect]


class QuizApp(tk.Tk):
    """
    Controller class for frames of the PyQuizzine application
    ...
    Attributes:
        title_font : Font attributes for titles
        font : Font attributes for regular text
        frames : array of the page names
        results : instance of Results class based off of csv file
    """
    def __init__(self, csv="csv_quiz_example_format.csv", *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold", slant="italic")
        self.font = tkfont.Font(family="Helvetica", size=11)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        self.frames = {}
        self.results = Results(csv_file=csv)
        for F in (Initialize, StartPage, QuizStats, QuestionStats):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Initialize")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


class Initialize(tk.Frame):
    """
    First page of application, asks for the name of the csv file to load
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def open_file(fname):
            """
            Initializes the results class with inputted csv file
            Arg:
                fname: a str for the name of the csv file to be read
            """
            controller.results = Results(fname)
            controller.show_frame("StartPage")
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        # Create visual elements
        label1 = tk.Label(self, text="Load File", font=controller.title_font)
        l1 = tk.Label(self, text="csv file name", font=controller.font)
        e1 = tk.Entry(self)
        button1 = tk.Button(self, text="Open File", font=controller.font,
                            command=lambda: open_file(e1.get()))
        # Arrange visual elements
        label1.grid(row=0, column=1, rowspan=2)
        l1.grid(row=2, column=1, sticky="E")
        e1.grid(row=2, column=2, sticky="W")
        button1.grid(row=3, column=1)


class StartPage(tk.Frame):
    """
    Main page of the application that has navigation to other pages
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        # Creating visual elements
        label1 = tk.Label(self, text="Start Page", font=controller.title_font)
        button1 = tk.Button(self, text="Quiz Statistics", font=controller.font,
                            command=lambda: controller.show_frame("QuizStats"))
        button2 = tk.Button(self, text="Question Statistics", font=controller.font,
                            command=lambda: controller.show_frame("QuestionStats"))
        button3 = tk.Button(self, text="Exit", font=controller.font,
                            command=lambda: controller.destroy())
        # Arranging visual elements
        label1.grid(row=0, column=1, rowspan=2)
        button1.grid(row=2, column=0, sticky="E")
        button2.grid(row=2, column=2, sticky="W")
        button3.grid(row=0, column=0, sticky="NW")


class QuizStats(tk.Frame):
    """
    Application page that displays general statistics about the entire quiz
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        # Creating visual elements
        label1 = tk.Label(self, text="Quiz Statistics", font=controller.title_font)
        l1 = tk.Label(self, text=f"Average time: {controller.results.avg_time() / 60:.2f} minutes", font=controller.font)
        l2 = tk.Label(self, text=f"Average score: {controller.results.avg_score():.2f}%", font=controller.font)
        button1 = tk.Button(self, text="Start Page", font=controller.font,
                            command=lambda: controller.show_frame("StartPage"))
        # Arranging visual elements
        label1.grid(row=0, column=1, rowspan=2)
        l1.grid(row=2, column=1)
        l2.grid(row=3, column=1)
        button1.grid(row=0, column=0, sticky="NW")


class QuestionStats(tk.Frame):
    """
    Application page that displays a graph for statistics of a user-specified question
    ...
    Attributes:
        canvas : tkinter Canvas object that contains the graph
        stats : tuple of the (correct, incorrect) percentages on the specified question
    """
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.canvas = None

        def ex():
            """
            Destroys the chart Canvas when exiting the page
            """
            try:
                self.canvas.get_tk_widget().delete("all")
                self.canvas.get_tk_widget().destroy()
            except AttributeError:
                pass
            controller.show_frame("StartPage")

        def show_stats(num):
            """
            Creates a pie chart, if doesn't already exist, of the stats for the user-inputted question number
            Args:
                num: an int that represents the question number to display data for
            """
            if self.canvas is None:
                self.stats = controller.results.question_stats(int(num))
                fig = Figure(figsize=(5, 5), dpi=100)
                fig, ax = plt.subplots()
                ax.pie([self.stats[0], self.stats[1]], labels=["Correct", "Incorrect"], colors=["blue", "red"])
                print(self.stats)
                self.canvas = FigureCanvasTkAgg(fig, master=controller)
                self.canvas.draw()
                self.canvas.get_tk_widget().pack()
                self.canvas.get_tk_widget().pack()
            else:
                self.canvas.get_tk_widget().delete("all")
                self.canvas.get_tk_widget().destroy()
                self.canvas = None
                show_stats(num)
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
            self.grid_columnconfigure(i, weight=1)
        # Create visual elements
        label1 = tk.Label(self, text="Question Statistics", font=controller.title_font)
        l1 = tk.Label(self, text="Question Number", font=controller.font)
        e1 = tk.Entry(self)
        button1 = tk.Button(self, text="View Stats", font=controller.font,
                            command=lambda: show_stats(e1.get()))
        button2 = tk.Button(self, text="Start Page", font=controller.font,
                            command=lambda: ex())
        # Arrange visual elements
        label1.grid(row=0, column=1, rowspan=2)
        l1.grid(row=3, column=1, sticky="E")
        e1.grid(row=3, column=2, sticky="W")
        button1.grid(row=4, column=0)
        button2.grid(row=0, column=0, sticky="NW")


app = QuizApp(className="PyQuizzine", csv="csv_quiz_example_format.csv")
app.geometry("500x500")
app.mainloop()

