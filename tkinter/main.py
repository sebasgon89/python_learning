import tkinter

window = tkinter.Tk()
window.title("TK")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text = "This is a label", font=("Arial", 30, "bold"))
my_label.pack(side="left")


window.mainloop()