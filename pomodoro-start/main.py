
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
from tkinter import *
import os
import math



# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps # imports a global variable defined and changes that specific variable , does not create local
  work_sec = WORK_MIN * 60
  short_break = SHORT_BREAK_MIN * 60
  long_break = LONG_BREAK_MIN * 60
  reps += 1
  if reps in [1,3,5,7]:
    count_down(work_sec)
    title.config(text="Work", fg=RED)
  elif reps in [2,4,6]:
    count_down(short_break)
    title.config(text="Break", fg=PINK)
  elif reps in [8]:
    count_down(long_break)
    title.config(text="Break", fg=PINK)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
  seconds = count % 60
  minutes = math.floor(count / 60)
  if seconds ==0 or len(str(seconds)) == 1:
    seconds = "0" + str(seconds)

  canvas.itemconfig(timer,text=f'{minutes}:{seconds}')
  if count>0:
    
    window.after(1000,count_down,count-1)
    print(count)
  else:

    start_timer()
    



  


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=-20,pady=10,bg=YELLOW)



base_dir= os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(base_dir,"tomato.png")
label1 = Label(text="✔",fg=GREEN, bg=YELLOW)
label1.grid(column=1,row=3)
reset = Button(text="Reset",font=(FONT_NAME,12))
reset.grid(column=2,row=2)
start = Button(text="Start",font=(FONT_NAME,12),command=start_timer)
start.grid(column=0,row=2)
title = Label(text="Timer", font=(FONT_NAME,50,"bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1,row=0)
canvas = Canvas(width=250,height=285,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file=image_path)
canvas.create_image(140,95,image=tomato_img)
timer = canvas.create_text(135,110,text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
canvas.grid(column=1,row=1)

start_timer()
window.mainloop()


