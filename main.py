from create import exportXML, makeQuestions
while True:
    try:
        choice = int(input("""What action would you like to perform?:
            1) Loading
            2) Creating
            3) Visualizing
            """))
        break
    except:
        print("You need a valid integer")

if choice == 1:
    import loading

elif choice == 2:
    quizName = input("Input the name of your quiz")
    exportXML(makeQuestions(), quizName)
else:
    import visual
