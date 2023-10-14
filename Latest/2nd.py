from optparse import Option
import tkinter as tk
import csv_Play
from tkinter import filedialog, Toplevel
import la
import convo_
import getfreq
import consec
import mixing
import m_random
import succesive
import mix_random
import band_mix

root = tk.Tk()
root.geometry("7500x6400")


def deleteframes():
    for frame in main_frame.winfo_children():
        frame.destroy()


##############
def mi():
    deleteframes()
    l2 = tk.Label(main_frame, text="Mixing")
    l2.grid(row=0, column=2, pady=15)

    def mix():
        # mi()
        mixing.mix(fl1.cget("text"), fl2.cget("text"))

    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
            ("WAV files", "*.wav"), ("MP3 files", "*.mp3"), ("All files", "*.*")))
        if file_path:
            # Self.text="{}",file_path
            fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0, padx=60)
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1, padx=60)
    #
    bt4 = tk.Button(main_frame, text="play mixed signal", command=mix)
    bt4.grid(row=1, column=4, padx=60)
    #
    bt5 = tk.Button(main_frame,text="mix randomly",command=band_mix.r)
    bt5.grid(row=2,column=1,padx=60)

    l = tk.Label(main_frame, text="mix the band freq by selecting them from the dropdown list", anchor="nw", borderwidth=3)
    l.grid(row=3, column=0, padx=90, pady=3)
    opt = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var = tk.StringVar()
    var.set(opt[0])
    o = tk.OptionMenu(main_frame, var, *opt)
    o.grid(row=4, column=0)
###############################
    #l = tk.Label(main_frame, text="Play the bands by selecting them from the dropdown list", anchor="nw", borderwidth=3)
    #l.grid(row=1, column=0, padx=90, pady=3)
    opt = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var = tk.StringVar()
    var.set(opt[0])
    o2 = tk.OptionMenu(main_frame, var, *opt)
    o2.grid(row=4, column=1)



####################
def con():
    deleteframes()
    l2 = tk.Label(main_frame, text="Convolution")
    l2.grid(row=0, column=2, pady=15)

    def pcon():
        convo_.con(getfreq.get_audio_frequency(fl1.cget("text")), getfreq.get_audio_frequency(fl2.cget("text")))

    def open(fl):
        # e=Entry(top,text="Enter no. of files to be selected for convolution")
        file_path = filedialog.askopenfilename(initialdir="Downloads", title="Select a file", filetypes=(
          ("WAV files", "*.wav"),("MP3 files", "*.mp3"),  ("All files", "*.*")))
        if file_path:
            # Self.text="{}",file_path
            fl.config(text="" + file_path)

    fl1 = tk.Label(main_frame, text="")
    fl2 = tk.Label(main_frame, text="")

    bt1 = tk.Button(main_frame, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0, padx=60)
    bt2 = tk.Button(main_frame, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1, padx=60)
    # 
    bt3 = tk.Button(main_frame, text="play convolved signal", command=pcon)
    bt3.grid(row=1, column=3, padx=60)


###################
def band():
    deleteframes()

    def randomsound():
        m_random.m()

    def conse():
        consec.play(var.get())

    def s():
        succesive.successive(var.get())

    def dropd():
        csv_Play.inn(var.get())

    new_windoe = tk.Button(main_frame, text="Play selected band", command=dropd)

    l = tk.Label(main_frame, text="Play the bands by selecting them from the dropdown list", anchor="nw", borderwidth=3)
    l.grid(row=1, column=0, padx=90, pady=3)
    opt = [
        "A_band",
        "B_band",
        "C_band",
        "D_band",
        "E_band",
        "F_band"
    ]

    var = tk.StringVar()
    var.set(opt[0])
    o = tk.OptionMenu(main_frame, var, *opt)
    o.grid(row=2, column=0)
    new_windoe.grid(row=2, column=1)
    consecutive = tk.Button(main_frame, text="Play consecutive", command=conse, padx=15, pady=10)
    consecutive.grid(row=3, column=0)
    succes = tk.Button(main_frame, text="Play Successive", padx=15, pady=10,command=s)
    succes.grid(row=3, column=1)
    ra = tk.Button(main_frame, text="Play Random", padx=15, pady=10,command=randomsound)
    ra.grid(row=3, column=2)


Option_frame = tk.Frame(root, bg="#ADD8E6", relief="sunken", borderwidth=2)


def about():
    tk.Frame(root, bg="#ffb6c1", relief="sunken", borderwidth=2)
    #main_frame.label.text          


home_btn = tk.Button(Option_frame, text="ABOUT", fg="#158aff", padx=20, pady=10, command=about)
home_btn.place(x=10, y=50)
home_btn.pack(pady=20)

#aboutus= Label(text="")

playband = tk.Button(Option_frame, text="Play bands", fg="#158aff", padx=20, pady=10, command=band)
playband.place(x=10, y=100)
playband.pack(pady=20)

convobtn = tk.Button(Option_frame, text="Convolution", fg="#158aff", command=con, padx=20, pady=10)
convobtn.place(x=10, y=150)
convobtn.pack(pady=20)

mix = tk.Button(Option_frame, text="Mixing", fg="#158aff", command=mi, padx=20, pady=10)
mix.place(x=10, y=200)
mix.pack(pady=20)
Option_frame.pack_propagate(False)
Option_frame.configure(width=150, height=400)
Option_frame.pack(side="left", fill="y")

main_frame = tk.Frame(root, bg="#ffb6c1", relief="sunken", borderwidth=2)
main_frame.pack_propagate(False)
main_frame.configure(width=400, height=400)
main_frame.pack(side="left", fill="both", expand=True)

#
# main_frame.pack_propagate(False)
# main_frame.configure(width=400, height=400)
# main_frame.pack(side="top",fill="y")

root.mainloop()
