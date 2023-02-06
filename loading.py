from quizpy import *
import xml.etree.ElementTree as ET
import time
tree = ET.parse('example_quiz.xml')
root = tree.getroot()

for child in root:
    if child.attrib == {'type': 'multichoice'}:
        print("ok")
        p = tree.find("name")
        print(p)
print(root[1][1][0].text)
userAnswer = input()
if (userAnswer.lower() == root[1][10][0].text.lower()):
    print("Correct!")
else:
    print("Incorrect")


