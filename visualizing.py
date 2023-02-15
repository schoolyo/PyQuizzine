import matplotlib.pyplot as plt
import csv
import pandas as pd

data = pd.read_csv("csv_quiz_example_format.csv")
numRows = len(data.axes[0])
numCols = len(data.axes[1])
percent = sum([i for i in data.iloc[:, 4] if i == 1]) / numRows * 100 # list comprehension to find percent of students correct
print(f"{percent:.2f}% got the question correct") # print the percentage to 2 decimals places

