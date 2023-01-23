from quizpy import *
from bs4 import BeautifulSoup
filename = input("Input the the filename of the quiz you would like to load:")
soup = BeautifulSoup(filename)
print(soup.prettify(filename))

