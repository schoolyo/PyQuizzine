import xml.etree.ElementTree as ET
import time
tree = ET.parse(input("Input XML file name of quiz: ").strip() + ".xml")
root = tree.getroot()
from csv import writer
try:
    file1 = open('data.csv', 'a')
except:
    file1 = open('data.csv', 'w')
#file1.write("\n")
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
print("\nYour score is " + str(score))
time = time.time() - start
print("You took " + str(round(time)) + "s")
if score == 0:
    file1.write(name + "," + str(round(time)) + ",0")
    for i in range(0, len(data)):
        file1.write(data[i] + ",")
else:
    file1.write(name + "," + str(round(time)) + "," + str(round((len(questions) / score) * 100)))
    for i in range(0, len(data)):
        file1.write("," + data[i])
file1.write("\n")
file1.close()
