import xml.etree.ElementTree as ET
import time

fileName = input("Input XML file name of quiz: ").strip()
tree = ET.parse(fileName + ".xml")
root = tree.getroot()

try:
    file1 = open(fileName + ".csv", 'a')
except:
    file1 = open(fileName + ".csv", 'w')
questCount = 0
data = []
name = input("What is your name?: ")

# create CSV file, student name, quiz time, percent, 1 or 0 for questions correct


count = 1
score = 0
questions = []
answers = []
# Gets all questions in xml file

for questiontext in root.iter('questiontext'):
    questions.append(questiontext[0].text.strip())

# Gets all correct answers for corresponding questions in xml file


for answer in root.iter('answer'):
    answers.append(answer[0].text.strip())
    questCount += 1


print("This quiz is scored 0 out of " + str(round(len(answers) / 4)) + "\n")


# Starts multi choice
start = time.time()
for k in range(0, len(questions)):
    count = 1

    print(questions[k])
    for i in range(0, len(answers)):
        if "_" in answers[i]:
            print(str(str(answers[i][:-1])))
        else: 
            print(str(answers[i]))
    count += 1 
    userAns = input()

for i in range(0, len(questions)):
        if userAns.lower() + "_" in answers:
            score += 1
            print("\nCorrect!")
            data.append("1") 
        else:
            data.append("0")
try:
    score = str(round((len(questions) / score) * 100))
except ZeroDivisionError:
    score = "0"
print("\nYour score is " + score + "%")
time = time.time() - start
print("You took " + str(round(time)) + "s")
"""if score == 0:
    file1.write(name + "," + str(round(time)) + ",0")
    for i in range(0, len(data)):
        file1.write("," + data[i])
else:
    file1.write(name + "," + str(round(time)) + "," + str(round((len(questions) / score) * 100)))
    for i in range(0, len(data)):
        file1.write("," + data[i])"""
file1.write(f"{name},{round(time)},{score}")
for i in range(0, len(data)):
    file1.write(f",{data[i]}")
file1.write("\n")
file1.close()
