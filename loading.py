import xml.etree.ElementTree as ET
import time
tree = ET.parse(input("Input XML file name of quiz: ").strip() + ".xml")
root = tree.getroot()
file1 = open('data.csv', 'w')
file1.write("\n")
questCount = 0

name = input("What is your name?: ")
file1.write(name + ",")
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
for k in range(0, len(questions) / 4):
    count = 1

    print(questions[k])
    for i in range(i, k + 4):
        if "_" in answers[i]:
            print(str(count) + ")" + " " + str(answers[i][:-1])
        else: # What the hell man!
            print(str(count) + ")" + " " + answers[i])
    count += 1 
    userAns = input()

for i in range(0, len(answers)):
        if userAns.lower() + "_" in answers.lower():
            score += 1
            print("\nCorrect!")
            file1.write("1,")
        else:
            file1.write("0,")
print("\nYour score is " + str(score))
time = time.time() - start
print("You took " + str(round(time))  + " seconds")
file1.write(str(round(time)) + ",")
file1.write(str(len(questions - 1) / score) + "%")
file1.close()
