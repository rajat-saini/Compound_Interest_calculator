from tkinter import *


tk = Tk()
tk.resizable(0,0)
tk.title("Compound Interest")
tk.geometry("550x300+250+250")

p = StringVar()
r = StringVar()
t = StringVar()

def calculation():
    a=float(p.get())
    b=float(r.get())
    c=float(t.get())
    CI=a*((1+(b/100))**c)
    e4.insert(0,CI)

def reset():
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

#Principal Value
l1=Label(text="Enter Principal value", font=100)
l1.place(x=200,y=10)
e1=Entry(textvariable=p)
e1.place(x=360,y=15)

#Rate of interest
l2=Label(text="Enter Rate of interest",font=100)
l2.place(x=200,y=40)
e2=Entry(textvariable = r)
e2.place(x=360, y=45)

#Time duration
l3=Label(text="Time duration",font=100)
l3.place(x=200,y=70)
e3=Entry(textvariable = t)
e3.place(x=360, y=75)

b1=Button(text="CALCULATE",bg="light green",command=calculation,width=15)
b1.place(x=200,y=110)
b2=Button(text="RESET",bg="yellow",command=reset, width=15)
b2.place(x=350, y=110)
l4=Label(text="Compound Interest",fg="purple", font=('Arial', 11,'bold'))
l4.place(x=200,y=180)
e4 = Entry(bg="pink")
e4.place(x=350, y=180)

tk.mainloop()


