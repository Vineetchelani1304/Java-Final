# from cgitb import text
from fileinput import filename
from tkinter import*

from setuptools import Command
from tkinter import filedialog,Toplevel

import freqtowave
from play_csv2 import play
root = Tk()

root.geometry("533x463")
f1=Frame(root,borderwidth=3,padx=3,pady=2,relief=SUNKEN, bg="pink")
f1.pack(side=TOP, anchor="nw",pady=100,padx=5,fill=X)
l1=Label(f1,text="OCTAVE",pady=2)
l1.pack(pady=4)
b1 = Button(f1,text="SA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4,bg="white")
b1.pack(side=LEFT, padx=90,pady=6)
b2 = Button(f1,text="RE",borderwidth=2, relief=SUNKEN, fg="grey", padx=4,bg="white")
b2.pack(side=LEFT, padx=90,pady=2)
b3 = Button(f1,text="GA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4,bg="white")
b3.pack(side=LEFT, padx=90,pady=2)
b4 = Button(f1,text="MA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b4.pack(side=LEFT, padx=90,pady=2)
b5 = Button(f1,text="PA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b5.pack(side=LEFT, padx=90,pady=2)
b6 = Button(f1,text="DHA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b6.pack(side=LEFT, padx=90,pady=2)
b7 = Button(f1,text="NI",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b7.pack(side=LEFT, padx=90,pady=2)
e=Entry(root,text="hello")
e.pack()
e.insert(0,"enter frequency")
def playf():
    freqtowave.generate(int(e.get()))
playcsv= Button(root,text="play frequency",command=playf)

playcsv.pack()
def make():
    top = Toplevel(root)

    def open():
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(("Wav", "*.wav"),("Mp3","*.mp3"), ("All files", "*.*")))
        if file_path:
            print("Selected file:", file_path)

    bt1 = Button(top, text="Select File", command=open)
    bt1.pack()
new_windoe=Button(root,text="convole signals", command=make)
new_windoe.pack()

root.mainloop()