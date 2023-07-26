from tkinter import *
from tkcalendar import*
n=Tk()
n.geometry("300x300")
n.minsize(300,400)
n.maxsize(300,1000)
n.title("My GUI")
f1=Frame(n,bg="#78C1F3",borderwidth=2,relief=SUNKEN)
f1.pack(side=TOP,fill="x")
l=Label(f1,text="Calendar",font="Helvetica 16 bold",fg="BLACK")
l.pack(pady=10)
def k():
    a=cal.get_date()
    k=Label(text=a)
    k.pack(padx=5,pady=5)
cal=Calendar()
cal.pack(padx=25,pady=25)
b=Button(n,text="Select Date",command=k)
b.pack(pady=5)
n.configure(bg="#9BE8D8")
n.mainloop()
 