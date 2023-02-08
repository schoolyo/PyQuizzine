from quizpy import *
import xml.etree.ElementTree as ET
import time
tree = ET.parse('example_quiz.xml')
root = tree.getroot()
ET.tostring(root, encoding='utf8').decode('utf8')
for child in root:
    print(child.tag, child.attrib)

for name in root.iter('question'):
    print(question.attrib)

print([elem.tag for elem in root.iter()])

"""print(root[1][1][0].text)
userAnswer = input()
if (userAnswer.lower() == root[1][10][0].text.lower()):
    print("Correct!")
else:
    print("Incorrect")
"""

