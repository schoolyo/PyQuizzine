from create import exportXML, makeQuestions
import tkinter as tk
def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = tk.Tk()

tk.Label(master, text="Which option would you like to perform?").grid(row=0)
tk.Label(master, text="First Name").grid(row=1)
tk.Label(master, text="Last Name").grid(row=3)

e1 = tk.Entry(master)
e2 = tk.Entry(master)

e1.grid(row=2, column=0)
e2.grid(row=4, column=0)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=4)
tk.Label(text=e1.get()).grid(column=0, row=5)
master.mainloop()

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
