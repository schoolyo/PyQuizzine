import xml.etree.ElementTree as ET
import time
import csv
from tkinter import *
from tkinter import ttk
tree = ET.parse(input("Input XML file name of quiz: ").strip() + ".xml")
root = tree.getroot()
questCount = 0
name = input("What is your name?: ")

with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['student', 'quiz time', 'percent score']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'student': name})


# create CSV file, student name, quiz time, percent, 1 or 0 for questions correct


count = 1
score = 0
questions = []
answers = []
booleanCorrects = []
# Gets all questions in xml file

for questiontext in root.iter('questiontext'):
    questions.append(questiontext[0].text.strip())

# Gets all correct answers for corresponding questions in xml file



for answer in root.iter('answer'):
    answers.append(answer[0].text.strip())
    questCount += 1

for i in range(0, questCount):
    fieldnames.append('q' + str(i))

print("This quiz is scored 0 out of " + str(len(answers) - 1) + "\n")


# Starts multi choice
start = time.time()
for k in range(0, len(questions)):

    print(questions[k])
    for i in range(0, len(answers)):
        if i % 4 != 0 or i == 0: # Iterate through four answers 
            print(str(count) + ")" + " " + answers[i])
            count += 1
            booleanCorrects.append("0")
    userAns = input()
    
    for i in range(0, len(answers)):
        if userAns.lower() == answers[i].lower():
            score += 1
            booleanCorrects.append("1")
            print("\nCorrect!")
        else:
            booleanCorrects.append("0")

print("\nYour score is " + str(score))
time = time.time() - start
print("You took " + str(round(time))  + " seconds")

