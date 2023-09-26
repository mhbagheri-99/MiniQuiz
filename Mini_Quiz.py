from tkinter import *
from tkinter import messagebox
import random
import time

# global variables
score = 0
name = ""
q1 = ["What product did Amazon first start out selling?",["Books","Music","Food","Clothes"],1]
q2 = ["What was eBay.com originally called?",["AuctionBay","ElectroBay","ElectronBay","AuctionWeb"],4]
q3 = ["What was the name of the first social networking site in 1994?",["Facebook","GeoCities","friend-zone","G+"],2]
q4 = ["In 2002, what company acquired PayPal?",["Microsoft","Google","eBay","Amazon"],3]
q5 = ["Introduced in 1993, what was Apple's first tablet computer?",["Newton MessagePad","iPad","Apple Pad","Tablet"],1]
q6 = ["How many characters did Twitter originally restrict users to?",["128","64","140","256"],3]
q7 = ["How many bytes are there in 4 kilobytes of memory?",["2048","4096","1024","4000"],2]
q = [q1,q2,q3,q4,q5,q6,q7]
questions = random.sample(q, 5)
key = questions[0][2]
color=[0,0,0,0]
color[key-1] = 1
i = 0

# welcome window
window = Tk()

window.title("Trivia")

window.geometry('300x200')

lbl3 = Label(window, text="")
lbl3.pack()

lbl = Label(window, text="This is a 5-question multiple choice trivia...")
lbl.pack()

lbl1 = Label(window, text="")
lbl1.pack()

lbl2 = Label(window, text="Enter Your Name: ")
lbl2.pack()

txt = Entry(window,width=20)
txt.pack()
txt.focus()

def clicked():
    global name 
    name = txt.get()
    messagebox.showinfo("Welcome","Welcome to Trivia " + name + " !")
    window.destroy()

sub_name = Button(window, text="Continue", command=clicked)
sub_name.pack()

window.mainloop()


# questions
window_q = Tk()

window_q.geometry('400x300')

window_q.title("Question")

lbl = Label(window_q, text="")
lbl.pack()

question = Label(window_q, text=questions[0][0])
question.pack()

lbl1 = Label(window_q, text="")
lbl1.pack()


def answer1(key):
    if key == 1:
        global score
        score += 20
    else:
        color[0] = -1
    color_btn(color)
    window_q.update()
    time.sleep(5)
    global i
    i += 1
    next_question(i)

def answer2(key):
    if key == 2:
        global score
        score += 20
    else:
        color[1] = -1
    color_btn(color)
    window_q.update()
    time.sleep(5)
    global i
    i += 1
    next_question(i)

def answer3(key):
    if key == 3:
        global score
        score += 20
    else:
        color[2] = -1
    color_btn(color)
    window_q.update()
    time.sleep(5)
    global i
    i += 1
    next_question(i)

def answer4(key):
    if key == 4:
        global score
        score += 20
    else:
        color[3] = -1
    color_btn(color)
    window_q.update()
    time.sleep(5)
    global i
    i += 1
    next_question(i)


choice1 = Button(window_q, text=questions[0][1][0])
choice1.pack()
lbl2 = Label(window_q, text="")
lbl2.pack()
choice2 = Button(window_q, text=questions[0][1][1])
choice2.pack()
lbl3 = Label(window_q, text="")
lbl3.pack()
choice3 = Button(window_q, text=questions[0][1][2])
choice3.pack()
lbl4 = Label(window_q, text="")
lbl4.pack()
choice4 = Button(window_q, text=questions[0][1][3])
choice4.pack()

choice1.configure(command= lambda: answer1(key))
choice2.configure(command= lambda: answer2(key))
choice3.configure(command= lambda: answer3(key))
choice4.configure(command= lambda: answer4(key))

def color_btn (color):
    for i in range(4):
        if color[i] == 1:
            if i == 0:
                choice1.configure(bg="green")
            if i == 1:
                choice2.configure(bg="green")
            if i == 2:
                choice3.configure(bg="green")
            if i == 3:
                choice4.configure(bg="green")
        elif color[i] == -1:
            if i == 0:
                choice1.configure(bg="red")
            if i == 1:
                choice2.configure(bg="red")
            if i == 2:
                choice3.configure(bg="red")
            if i == 3:
                choice4.configure(bg="red")
   
def next_question(i):
    if i < 5:
        global key
        key = questions[i][2]
        global color
        color = [0,0,0,0]
        color[key-1] = 1
        choice1.configure(text=questions[i][1][0], bg="SystemButtonFace")
        choice2.configure(text=questions[i][1][1], bg="SystemButtonFace")
        choice3.configure(text=questions[i][1][2], bg="SystemButtonFace")
        choice4.configure(text=questions[i][1][3], bg="SystemButtonFace")
        question.configure(text=questions[i][0])
    else:
        window_q.destroy()

window_q.mainloop()

# Score
window_s = Tk()

window_s.title("Score")

window_s.geometry('300x100')

lbl = Label(window_s, text="")
lbl.pack()

tnx = Label(window_s, text="Thanks for playing " + name + " :)")
tnx.pack()

lbl1 = Label(window_s, text="")
lbl1.pack()

s = Label(window_s, text="You scored " + str(score) + "% !")
s.pack()

window_s.mainloop()