import tkinter

window = tkinter.Tk()
window.title("TK")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text = "This is a label", font=("Arial", 30, "bold"))
my_label.pack(side="left")

def button_clicked():
    # print("I was clicked")
    # my_label.config(text="Clicked!")
    my_label.config(text=input.get())


button = tkinter.Button(text = "Click me!", command=button_clicked)
button.pack()

input = tkinter.Entry(width=20)
input.pack()

window.mainloop()