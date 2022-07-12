from tkinter import *
import math

root=Tk()
root.title("Simple Calculator")
root.configure(bg='#94B49F')
e = Entry(root,width=60,border=5)
e.grid(row=0,column=0,columnspan=3)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)
          
def button_add():
    first_number = e.get()
    global f_num
    global math
    math="addition"
    f_num=float(first_number)
    e.delete(0,END)
    
def button_sub():
    first_number = e.get()
    global f_num
    global math
    math="subtraction"
    f_num=float(first_number)
    e.delete(0,END)
    
def button_mul():
    first_number = e.get()
    global f_num
    global math
    math="multiplication"
    f_num=float(first_number)
    e.delete(0,END)
   
def button_div():
    first_number = e.get()
    global f_num
    global math
    math="division"
    f_num=float(first_number)
    e.delete(0,END)
    
def button_square():
    first_number = e.get()
    e.delete(0,END) 
    e.insert(0,float(first_number)*float(first_number))
    
def button_dot():
    first_number=e.get()
    dot="."
    e.insert(first_number,str(dot)) 
    
def button_squareRoot():
    first_number=e.get()
    e.insert(0,int(first_number)**0.5)
    
         
def button_equal():
    second_number=e.get()
    e.delete(0,END)
    if math == "addition":
        e.insert(0,f_num+int(second_number))
    if math == "subtraction":
        e.insert(0,f_num-int(second_number))
    if math == "multiplication":
        e.insert(0,f_num*int(second_number))
    if math == "division":
        e.insert(0,f_num/int(second_number))

#define buttons

b1=Button(root,text='1',padx=40,pady=20,command=lambda:button_click(1))
b2=Button(root,text='2',padx=40,pady=20,command=lambda:button_click(2))
b3=Button(root,text='3',padx=40,pady=20,command=lambda:button_click(3))
b4=Button(root,text='4',padx=40,pady=20,command=lambda:button_click(4),bg='orange')
b5=Button(root,text='5',padx=40,pady=20,command=lambda:button_click(5),bg='orange')
b6=Button(root,text='6',padx=40,pady=20,command=lambda:button_click(6),bg='orange')
b7=Button(root,text='7',padx=40,pady=20,command=lambda:button_click(7),bg='orange')
b8=Button(root,text='8',padx=40,pady=20,command=lambda:button_click(8),bg='orange')
b9=Button(root,text='9',padx=40,pady=20,command=lambda:button_click(9),bg='orange')
b0=Button(root,text='0',padx=40,pady=20,command=lambda:button_click(0))

button_equals=Button(root,text='=',padx=80,pady=20,command=button_equal)
button_add=Button(root,text='+',padx=40,pady=20,command=button_add)
button_sub=Button(root,text='-',padx=40,pady=20,command=button_sub,bg="green")
button_mul=Button(root,text="x",padx=40,pady=20,command=button_mul)
button_div=Button(root,text="/",padx=40,pady=20,command=button_div,bg="green")

button_clear=Button(root,text="C",padx=40,pady=20,command=button_clear,bg="green")
button_square=Button(root,text="X²",padx=40,pady=20,command=button_square,bg="green")
button_dot=Button(root,text=".",padx=40,pady=20,command=button_dot,bg="green")
button_squareRoot=Button(root,text="√2",padx=30,pady=20,command=button_squareRoot,bg="green")

# put the buttons on the screen
b1.grid(row= 3,column=0)
b2.grid(row= 3,column=1)
b3.grid(row= 3,column=2)

b4.grid(row= 2,column=0)
b5.grid(row=2 ,column=1)
b6.grid(row= 2,column=2)

b7.grid(row=1 ,column=0)
b8.grid(row= 1,column=1)
b9.grid(row= 1,column=2)

b0.grid(row=4 ,column=0)


button_add.grid(row=4,column=2)
button_sub.grid(row=5,column=2)
button_div.grid(row=5,column=1)
button_mul.grid(row=4,column=1)

button_equals.grid(row=7,column=1)
button_clear.grid(row=5,column=0)
button_square.grid(row=6,column=0)
button_dot.grid(row=6,column=1)
button_squareRoot.grid(row=6,column=2)

root.mainloop()
