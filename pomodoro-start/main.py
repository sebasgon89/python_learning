import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    print(count)
    if count > 0:
        window.after(1000, count_down(count - 1))
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


count_down(5)

title_label = tkinter.Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=200, height=224, bg = YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text = "00.00", fill = "white", font = (FONT_NAME, 36, "bold"))
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text="Start", highlightthickness=0)
start_button.grid(column=0, row=2)

restart_button = tkinter.Button(text="Restart", highlightthickness=0)
restart_button.grid(column=2, row=2)

check_marks = tkinter.Label(text="✓", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()