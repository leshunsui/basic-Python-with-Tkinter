import tkinter

def Yourgrade():
    score = int(entry_score.get())
    grades = {
        (0, 50): "F",
        (50, 60): "D",
        (60, 70): "C",
        (70, 80): "B",
        (80, 100): "A"
    }

    for ranges, grade in grades.items():
        if score in ranges:
            label_result.configure(text=f"You Got Grade {grade}")
            break
    else:
        label_result.configure(text="Error: Score must be between 0 and 100")

window = tkinter.Tk()
window.title("Grade Calculator")
window.geometry("400x200")
window.resizable(False ,False )

label1 = tkinter.Label(text="Enter your score")
label1.place(relx=0.5, rely=0.3, anchor='center')

entry_score = tkinter.Entry()
entry_score.place(relx=0.5, rely=0.5, anchor='center')

btn1 = tkinter.Button(text="Calculate", command=Yourgrade)
btn1.place(relx=0.5, rely=0.7, anchor='center')

label_result = tkinter.Label(text="")
label_result.place(relx=0.5, rely=0.9, anchor='center')

window.mainloop()