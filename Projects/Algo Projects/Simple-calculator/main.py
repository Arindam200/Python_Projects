from tkinter import *
from tkinter.font import Font

root = Tk()
root.title("simple calculator")

myEntry = Entry(root,width=40,borderwidth=3,font=(20))
myEntry.grid(row=0,column=0,columnspan=4,ipady=10)

# functions
def button_click(number):
    #myEntry.delete(0,END)
    current = myEntry.get()
    myEntry.delete(0,END)
    myEntry.insert(0,str(current)+str(number))

def button_clear():
    myEntry.delete(0,END)

def evaluvate():
    x=myEntry.get()
    ans = eval(x)
    myEntry.delete(0,END)
    myEntry.insert(0,ans)

# creating buttons
button_1 = Button(root,text="1",pady=20,padx=40,command=lambda:button_click(1))
button_2 = Button(root,text="2",pady=20,padx=40,command=lambda:button_click(2))
button_3 = Button(root,text="3",pady=20,padx=40,command=lambda:button_click(3))
button_4 = Button(root,text="4",pady=20,padx=40,command=lambda:button_click(4))
button_5 = Button(root,text="5",pady=20,padx=40,command=lambda:button_click(5))
button_6 = Button(root,text="6",pady=20,padx=40,command=lambda:button_click(6))
button_7 = Button(root,text="7",pady=20,padx=40,command=lambda:button_click(7))
button_8 = Button(root,text="8",pady=20,padx=40,command=lambda:button_click(8))
button_9 = Button(root,text="9",pady=20,padx=40,command=lambda:button_click(9))
button_0 = Button(root,text="0",pady=20,padx=40,command=lambda:button_click(0))
button_00 = Button(root,text="00",pady=20,padx=37,command=lambda:button_click("00"))
button_dot = Button(root,text=".",pady=20,padx=41,command=lambda:button_click("."))
button_add = Button(root,text="+",pady=20,padx=37,command=lambda:button_click("+"))
button_sub = Button(root,text="-",pady=20,padx=39,command=lambda:button_click("-"))
button_mul = Button(root,text="x",pady=20,padx=39,command=lambda:button_click("*"))
button_div = Button(root,text="/",pady=20,padx=39,command=lambda:button_click("/"))
button_equal = Button(root,text="=",pady=20,padx=135,bg='#99c2ff',command=evaluvate)
button_clear = Button(root,text="AC",pady=20,padx=33,bg='#ff4d4d',command=button_clear)


# put buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=1)
button_00.grid(row=4,column=0)
button_dot.grid(row=4,column=2)

button_add.grid(row=2,column=3)
button_sub.grid(row=3,column=3)
button_mul.grid(row=4,column=3)
button_div.grid(row=5,column=3)

button_equal.grid(row=5,column=0,columnspan=3)
button_clear.grid(row=1,column=3)


root.mainloop()