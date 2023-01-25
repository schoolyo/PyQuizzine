from quizpy import *
from bs4 import BeautifulSoup
file = open("example_quiz.xml", "r")
contents = file.read()
soup = BeautifulSoup(contents, 'xml')

