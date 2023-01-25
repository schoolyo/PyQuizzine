import xml.etree.ElementTree as ET
mytree = ET.parse('example_quiz.xml')
myroot = mytree.getroot()
print(myroot[0].tag)