import matplotlib.pyplot as plt
import csv
import pandas as pd
import tkinter as tk
from tkinter import *


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
        return sum([i for i in self.data.iloc[:, "time"] if i > 0]) / self.numRows

    def avg_score(self):
        """
        Gets the average score of all students who took the quiz
        Returns:
            A float representing the average score as a percentage
        """
        return sum([i for i in self.data.iloc[:, "percent score"]]) / self.numRows

    def question_stats(self, num):
        """
        Gets the amount of correct and incorrect answers for a specific question
        Args:
            num: An integer for the question number wanted. num=1 would be the first question.
        Returns:
            A tuple in (percent correct, percent incorrect) format, where both are rounded to 2 decimal places
        """
        correct = round(sum([i for i in self.data.iloc[:, (num+2)] if i == 1]) / self.numRows * 100, 2)
        incorrect = round(sum([i for i in self.data.iloc[:, (num+2)] if i == 0]) / self.numRows * 100, 2)
        return correct, incorrect


class Page(tk.Frame):


def show_data():
    window = Tk()
    window.title("PyQuizzine")
    window.geometry("500x500")
