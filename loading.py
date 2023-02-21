import xml.etree.ElementTree as ET
import time
tree = ET.parse(input("Input XML file name of quiz: ").strip() + ".xml")
root = tree.getroot()

# Goal: test efficiency of algorithm on other quiz xml files
# Figure out how to print certain questions for each
count = 1
score = 0
questions = []
answers = []
name = input("What is your name?: ")
# Gets all questions in xml file

for questiontext in root.iter('questiontext'):
    questions.append(questiontext[0].text.strip())

print(questions)
# Gets all correct answers for corresponding questions in xml file



for answer in root.iter('answer'):
    answers.append(answer[0].text.strip())
print(answers)



print("This quiz is scored 0 out of " + str(len(answers) - 1) + "\n")


# Starts multi choice
start = time.time()
for k in range(0, len(questions)):

    print(questions[k])
    for i in range(0, len(answers)):
        if i % 4 != 0 or i == 0:
            print(str(count) + ")" + " " + answers[i])
            count += 1
    userAns = input()
    
    for i in range(0, len(answers)):
        if userAns.lower() == answers[i].lower():
            score += 1
            print("\nCorrect!")

print("\nYour score is " + str(score))
print("You took " + str(round(time.time() - start))  + " seconds")
