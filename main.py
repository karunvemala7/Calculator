#package imports
import tkinter as tk
from tkinter import RIDGE, Button, Entry

#create root for your application
app = tk.Tk()   

#define size of your application and define app name
app.geometry("170x230")
app.title("python-calculator")

app.maxsize(170,230)
app.minsize(170,230)


#create entry box to enter numbers
ent = Entry(app, width=16, borderwidth=3, relief=RIDGE)
ent.grid(pady=10,row=0,sticky="w",padx=15) #this style of a box grid

#define delete method to delete numbers
def delete():
        a = ent.get()
        ent.delete(first=len(a)-1,last="end")


#define show results function
def fresult():
        if ent.get() == "":
                pass
        elif ent.get()[0] == "0":
                ent.delete(0,"end")
        else:
                c_res = ent.get()
                c_res = eval(c_res)
                clearf()
                ent.insert("end",c_res)


#deine clear function
def clearf():
        ent.delete(0,"end")


#define buttons and text and size
#clear button
clean = Button(app,text="Clr",width=2,command=clearf,bg="green",fg="white",relief=RIDGE)
clean.grid(row=0,sticky="w",padx=125)

#9 character
Char_nine = Button(text="9",width=2,command=lambda : ent.insert("end","9"),borderwidth=3,relief=RIDGE)
Char_nine.grid(row=1,sticky="w",padx=15)

#8 character
Char_eight = Button(text="8",width=2,command=lambda : ent.insert("end","8"),borderwidth=3,relief=RIDGE)
Char_eight.grid(row=1,sticky="w",padx=45)

#add remaining numbers
Char_seven = Button(app,text="7",width=2,command=lambda : ent.insert("end","7"),borderwidth=3,relief=RIDGE)
Char_seven.grid(row=1,sticky="w",padx=75)

Char_plus = Button(app,text="+",width=2,command=lambda : ent.insert("end","+"),borderwidth=3,relief=RIDGE)
Char_plus.grid(row=1,sticky="e",padx=125)

Char_six = Button(text="6",width=2,command=lambda : ent.insert("end","6"),borderwidth=3,relief=RIDGE)
Char_six.grid(row=2,sticky="w",padx=15,pady=5)

Char_five = Button(text="5",width=2,command=lambda : ent.insert("end","5"),borderwidth=3,relief=RIDGE)
Char_five.grid(row=2,sticky="w",padx=45,pady=5)

Char_four = Button(app,text="4",width=2,command=lambda : ent.insert("end","4"),borderwidth=3,relief=RIDGE)
Char_four.grid(row=2,sticky="w",padx=75,pady=5)

Char_minus = Button(app,text="-",width=2,command=lambda : ent.insert("end","-"),borderwidth=3,relief=RIDGE)
Char_minus.grid(row=2,sticky="e",padx=125,pady=5)

Char_three = Button(text="3",width=2,command=lambda : ent.insert("end","3"),borderwidth=3,relief=RIDGE)
Char_three.grid(row=3,sticky="w",padx=15,pady=5)

Char_two = Button(text="2",width=2,command=lambda : ent.insert("end","2"),borderwidth=3,relief=RIDGE)
Char_two.grid(row=3,sticky="w",padx=45,pady=5)

Char_one = Button(app,text="1",width=2,command=lambda : ent.insert("end","1"),borderwidth=3,relief=RIDGE)
Char_one.grid(row=3,sticky="w",padx=75,pady=5)

#multiplication
Char_multiply = Button(app,text="*",width=2,command=lambda : ent.insert("end","*"),borderwidth=3,relief=RIDGE)
Char_multiply.grid(row=3,sticky="e",padx=125,pady=5)

Char_zero = Button(text="0",width=2,command=lambda : ent.insert("end","0"),borderwidth=3,relief=RIDGE)
Char_zero.grid(row=4,sticky="w",padx=15,pady=5)

#add rest of the calcs and operators
Char_double_zero = Button(text="00",width=2,command=lambda : ent.insert("end","00"),borderwidth=3,relief=RIDGE)
Char_double_zero.grid(row=4,sticky="w",padx=45,pady=5)

Char_dot = Button(app,text=".",width=2,command=lambda : ent.insert("end","."),borderwidth=3,relief=RIDGE)
Char_dot.grid(row=4,sticky="w",padx=75,pady=5)

Char_divide = Button(app,text="/",width=2,command=lambda : ent.insert("end","/"),borderwidth=3,relief=RIDGE)
Char_divide.grid(row=4,sticky="e",padx=125,pady=5)

result = Button(app,text="=",width=10,command=fresult,bg="green",fg="white",borderwidth=3,relief=RIDGE)
result.grid(row=5,sticky="w",padx=15,pady=5)

Char_modulus = Button(app,text="%",width=2,command=lambda : ent.insert("end","%"),borderwidth=3,relief=RIDGE)
Char_modulus.grid(row=5,sticky="e",padx=125,pady=5)

delete = Button(app,text="del",width=2,command=delete,borderwidth=3,relief=RIDGE)
delete.grid(row=5,sticky="w",padx=80,pady=5)

# keep the window displaying
app.mainloop()


#Thanks for Watching

































