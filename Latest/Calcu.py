from tkinter import *

root = Tk()
root.geometry("7666x7000")
f1 = Frame(root, bg="pink", padx=3, pady=3, borderwidth=3, relief=SUNKEN)
f1.pack(fill=BOTH,pady=50)

l1 = Label(f1, text="OCTAVE", pady=2)
l1.pack(pady=4)

b1 = Button(f1, text="SA", borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b1.pack(side=LEFT, padx=90, pady=6)

b2 = Button(f1, text="RE", borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b2.pack(side=LEFT, padx=90, pady=2)

b3 = Button(f1, text="GA", borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b3.pack(side=LEFT, padx=90, pady=2)

b4 = Button(f1, text="MA", borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b4.pack(side=LEFT, padx=90, pady=2)

b5 = Button(f1, text="PA", borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b5.pack(side=LEFT, padx=90, pady=2)

b6 = Button(f1, text="DHA", borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b6.pack(side=LEFT, padx=90, pady=2)

b7 = Button(f1, text="NI", borderwidth=2, relief=SUNKEN, fg="grey", padx=4, bg="white")
b7.pack(side=LEFT, padx=90, pady=2)

Consecutive = Button(f1, text="Consecutive", bg="grey", fg="black", borderwidth=2, relief=SUNKEN,width=25)
Consecutive.pack(side=BOTTOM,anchor="se")

root.mainloop()

# ###################################################
# # from tkinter import *
# # root = Tk()
# # root.title("AI Music Generator")
# #
# # f1=Frame(root,borderwidth=3,padx=3,pady=2,relief=SUNKEN, bg="pink")
# # f1.pack(side=TOP, anchor="nw",pady=100,padx=5,fill=X)
# #
# # consecutive_button = Button(f1, text="Consecutive").grid(row=0, column=0, padx=60, pady=10)
# #
# # successive_button = Button(f1, text="Successive").grid(row=0, column=1, padx=60, pady=10)
# #
# # random_button = Button(f1, text="Random").grid(row=0, column=2, padx=60, pady=10)
# #
# # root.configure(bg="#f2f2f2")
# # root.mainloop()
# ###########################################################################################
# from cgitb import text
# from fileinput import filename
# from logging import PlaceHolder
# from tkinter import *
#
# from tkinter.tix import InputOnly
# from typing import Self
# from numpy import signedinteger
#
# from setuptools import Command
# from tkinter import filedialog, Toplevel
# # import csv_Play
# # import convo_
# # import getfreq
#
# # import freqtowave
#
# root = Tk()
# root.geometry("7733x4463")
#
#
# frame = Frame(root, padx=3, pady=2, bg="grey", borderwidth=2, relief=SUNKEN)
# frame.grid(row=0, column=0, padx=500, pady=100, sticky="nsew", columnspan=2)
#
# #################################
#
#
# def make():
#     top = Toplevel(root)
#     top.geometry("533x463")
#     f1 = Frame(top, padx=3, pady=3, borderwidth=4, relief=SUNKEN, bg="grey")
#     f1.pack(pady=100,anchor="center")
#     l2 = Label(f1, text="Convolution")
#     l2.grid(row=0, column=1,pady=15)
#
#     def pcon():
#         convo_.con(getfreq.get_audio_frequency(fl1.cget("text")), getfreq.get_audio_frequency(fl2.cget("text")))
#
#     # def open(fl):
#     #     # e=Entry(top,text="Enter no. of files to be selected for convolution")
#     #     file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
#     #     ("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*")))
#     #     if file_path:
#     #           Self.text="{}",file_path
#     #         fl.config(text="" + file_path)
#
#     fl1 = Label(f1, text="")
#     fl2 = Label(f1, text="")
#
#     bt1 = Button(f1, text="Select File 1", command=lambda: open(fl1))
#     bt1.grid(row=1, column=0,padx=60)
#     bt2 = Button(f1, text="Select File 2", command=lambda: open(fl2))
#     bt2.grid(row=1, column=1,padx=60)
#     #
#     bt3 = Button(f1, text="Play", command=pcon)
#     bt3.grid(row=1, column=3,padx=60)
#
#
# ######################
# def dropd():
#     csv_Play.inn(var.get())
#
#
# ####################
#
# new_windoe = Button(frame, text="Play selected band" , command=dropd)
# new_windoe.grid()
# l = Label(frame, text="Play the bands by selecting them from the dropdown list", anchor="nw", borderwidth=3, relief=SUNKEN)
# l.grid(row=1, column=0, padx=90, pady=3)
# opt = [
#     "A_band",
#     "B_band",
#     "C_band",
#     "D_band",
#     "E_band",
#     "F_band"
# ]
#
# var = StringVar()
# var.set(opt[0])
# o = OptionMenu(frame, var, *opt)
# o.grid(row=2, column=0)
# ################
#
# # new window
#
# n = Button(frame, text="Convolve audio files", borderwidth=3, relief=SUNKEN, command=make)
# n.grid(row=3, column=0, padx=200, pady=10)
#
# ############

# root.mainloop()