from create import exportXML, makeQuestions
import tkinter as tk
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("PyQuizzine")
myapp.master.maxsize(1000, 400)

tk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


# start the program
myapp.mainloop()

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
    quizName = input("Input the name of your quiz: ")
    exportXML(makeQuestions(), quizName)
else:
    import visual
