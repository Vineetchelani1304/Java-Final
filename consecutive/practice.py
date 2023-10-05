from tkinter import *
root = Tk()

def printing():
    print("my name is Vineet")
def getvals():
    print(f"{uservalue.get(), Passvalue.get()}")
    with open("userlogin.txt","a") as f:
        f.write(f"{uservalue.get(), Passvalue.get()}\n")

root.geometry("499x599")
root.minsize(75,30)
frame = Frame( root, borderwidth=6,bg="pink" ,relief=SUNKEN)
frame.pack(side=TOP,fill=X)
# b1 = Button(frame,fg="BLACK",text="print now", borderwidth=3, relief=SUNKEN,command=printing)
# b1.pack(side=LEFT, anchor="nw", padx=5, pady=3)
b1=Button(frame,text="Print Now",fg="grey",borderwidth=3,relief=SUNKEN,command=printing)
b1.pack(side=LEFT,anchor="nw", padx=5,pady=3)
l = Label(frame,text="Login Page",font="comicsansms  13 bold", fg="blue", borderwidth=3)
l.pack( side=LEFT,padx=120)

frame2 = Frame(root, borderwidth=3, relief=SUNKEN)
frame2.pack(fill=X,side=TOP, anchor = "nw")
user = Label(frame2, text="User Name")
user.grid()
Password = Label(frame2, text="Password")
Password.grid(row=1)
uservalue=StringVar()
Passvalue=StringVar()
userentry=Entry(frame2, textvariable=uservalue)
Passentry=Entry(frame2, textvariable=Passvalue)
userentry.grid(row=0, column=1)
Passentry.grid(row=1, column=1)
Button(frame2, text="Submit", fg="grey", padx=2, pady=2, command=getvals).grid()
c1=Checkbutton(frame2, text="Save The Credentials", command=getvals).grid(row=2,column=2)


root.mainloop()