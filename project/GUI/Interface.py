import tkinter as tk
from tkinter import filedialog

from project.GUI.Main import inteGratedSolve


def btnClick(event=None):
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("all files", "*"), ("all files", "*.*")))
    print(filename)
    T.delete('1.0', tk.END)
    T.insert(tk.END, "Processing Question at:" + filename + "\n")
    T.delete('1.0', tk.END)
    if(isComplex.get() == True):
        output = inteGratedSolve(filename,True)
    else:
        output = inteGratedSolve(filename, False)
    for i in output:
        T.insert(tk.INSERT, i)
        T.insert(tk.INSERT, "\n")
        T.insert(tk.INSERT, "\n")
    return output


def onclick():
    pass


def sel():
    selection = "You selected the option is Complex : " + str(isComplex.get())
    label.config(text=selection)


r = tk.Tk()
r.title('Question Processing')
Display = tk.Text(r, height=2, width=100)
Display.insert(tk.INSERT, "TEAM 789 - AUTOMATED ALGEBRIC EQUATION GENERATION AND EVALUATION FROM SINHALA MATH WORD PROBLEMS")
Display.pack()

isComplex = tk.BooleanVar()
R1 = tk.Radiobutton(r, text="Complex Problem", variable=isComplex, value=True,
                    command=sel)
R1.pack()
R2 = tk.Radiobutton(r, text="Simple Problem", variable=isComplex, value=False,
                    command=sel)
R2.pack()
label = tk.Label(r)
label.pack()

button = tk.Button(r, text='Upload Question', width=25, command=btnClick)
button.pack()
S = tk.Scrollbar(r)
T = tk.Text(r, height=50, width=100)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)

r.mainloop()
