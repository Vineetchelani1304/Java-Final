# from tkinter import*
# root = Tk()
# root.geometry("533x463")
# # l1=Label(f1,text="OCTAVE",pady=2)
# # l1.pack(pady=4)
# # b1 = Button(f1,text="SA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4,bg="white")
# # b1.pack(side=LEFT, padx=90,pady=6)
# # b2 = Button(f1,text="RE",borderwidth=2, relief=SUNKEN, fg="grey", padx=4,bg="white")
# # b2.pack(side=LEFT, padx=90,pady=2)
# # b3 = Button(f1,text="GA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4,bg="white")
# # b3.pack(side=LEFT, padx=90,pady=2)
# # b4 = Button(f1,text="MA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
# # b4.pack(side=LEFT, padx=90,pady=2)
# # b5 = Button(f1,text="PA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
# # b5.pack(side=LEFT, padx=90,pady=2)
# # b6 = Button(f1,text="DHA",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
# # b6.pack(side=LEFT, padx=90,pady=2)
# # b7 = Button(f1,text="NI",borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
# # b7.pack(side=LEFT, padx=90,pady=2)
# Consecutive = Button(f1,text="Consecutive",bg="grey",fg="black",borderwidth=2,relief=SUNKEN).pack()
# root.mainloop()

from tkinter import *
root = Tk()
root.title("AI Music Generator")

f1=Frame(root,borderwidth=3,padx=3,pady=2,relief=SUNKEN, bg="pink")
f1.pack(side=TOP, anchor="nw",pady=100,padx=5,fill=X)

consecutive_button = Button(f1, text="Consecutive").grid(row=0, column=0, padx=60, pady=10)

successive_button = Button(f1, text="Successive").grid(row=0, column=1, padx=60, pady=10)

random_button = Button(f1, text="Random").grid(row=0, column=2, padx=60, pady=10)

root.configure(bg="#f2f2f2")
root.mainloop()
