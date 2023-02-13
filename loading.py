import xml.etree.ElementTree as ET
import time
tree = ET.parse(input("Input XML file name of quiz: ").strip() + ".xml")
root = tree.getroot()

# Goal: test efficiency of algorithm on other quiz xml files
# Figure out how to print certain questions for each
score = 0
questions = []
answers = []

# Gets all questions in xml file
for questiontext in root.iter('questiontext'):
    questions.append(questiontext[0].text.strip())

# Gets all correct answers for corresponding questions in xml file
for answer in root.iter('answer'):
    answers.append(answer[0].text.strip())

print("This quiz is scored 0 out of " + str(len(answers) - 1) + "\n")


# Starts multi choice
start = time.time()
for k in range(0, len(answers) - 1):
    print(questions[k])
    
    for j in range(0, len(answers)):
        print(answers[j])
    userAns = input()
    if userAns == answers[k]:
        score += 1
        print("\nCorrect!")
    else:
        print("\nIncorrect!")

print("\nYour score is " + str(score))
print("You took " + str(time.time() - start)  + " seconds")
