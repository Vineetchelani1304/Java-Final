import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk

import csv_Play
import convo_
import getfreq
import consec
import la

root = tk.Tk()
root.title("Modern Material GUI")
root.geometry("800x600")

# Load and display the background image
# background_image = Image.open("background_image.png")  # Replace with the path to your image
# background_photo = ImageTk.PhotoImage(background_image)
# background_label = tk.Label(root, image=background_photo)
# background_label.place(relwidth=1, relheight=1)

style = ttk.Style()
style.theme_use("clam")  # Use the "clam" theme for a modern appearance

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

def conse():
    consec.play(var1.get())

fn = ttk.Frame(root)
fn.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

opt = ["A_band", "B_band", "C_band", "D_band", "E_band", "F_band"]
var1 = tk.StringVar()
var1.set(opt[0])
op = ttk.Combobox(fn, textvariable=var1, values=opt)
op.grid(row=0, column=1, padx=10, pady=10)
consecutive_button = ttk.Button(fn, text="Consecutive", command=conse)
consecutive_button.grid(row=1, column=0, padx=10, pady=10)
successive_button = ttk.Button(fn, text="Successive")
successive_button.grid(row=1, column=1, padx=10, pady=10)
random_button = ttk.Button(fn, text="Random")
random_button.grid(row=1, column=2, padx=10, pady=10)

def make():
    top = tk.Toplevel(root)
    top.title("Convolution and Mixing")
    top.geometry("800x600")
    f1 = ttk.Frame(top)
    f1.pack(pady=50, anchor="center")
    l2 = ttk.Label(f1, text="Convolution and Mixing")
    l2.grid(row=0, column=2, pady=15)

    def mix():
        la.mix(fl1.cget("text"), fl2.cget("text"))

    def pcon():
        convo_.con(getfreq.get_audio_frequency(fl1.cget("text")), getfreq.get_audio_frequency(fl2.cget("text")))

    def open(fl):
        file_path = filedialog.askopenfilename(
            initialdir="Downloads",
            title="Select a file",
            filetypes=(("MP3 files", "*.mp3"), ("WAV files", "*.wav"), ("All files", "*.*"))
        )
        if file_path:
            fl.config(text=file_path)

    fl1 = ttk.Label(f1, text="")
    fl2 = ttk.Label(f1, text="")

    bt1 = ttk.Button(f1, text="Select File 1", command=lambda: open(fl1))
    bt1.grid(row=1, column=0, padx=10)
    bt2 = ttk.Button(f1, text="Select File 2", command=lambda: open(fl2))
    bt2.grid(row=1, column=1, padx=10)

    bt3 = ttk.Button(f1, text="Play Convolved Signal", command=pcon)
    bt3.grid(row=1, column=3, padx=10)
    bt4 = ttk.Button(f1, text="Play Mixed Signal", command=mix)
    bt4.grid(row=1, column=4, padx=10)

def dropd():
    csv_Play.inn(var.get())

new_window = ttk.Button(frame, text="Play selected band", command=dropd)
new_window.grid(pady=10)
label = ttk.Label(frame, text="Play the bands by selecting them from the dropdown list")
label.grid(row=1, column=0, padx=10, pady=5)

opt = ["A_band", "B_band", "C_band", "D_band", "E_band", "F_band"]
var = tk.StringVar()
var.set(opt[0])
o = ttk.Combobox(frame, textvariable=var, values=opt)
o.grid(row=2, column=0)

convolve_button = ttk.Button(frame, text="Convolve audio files", command=make)
convolve_button.grid(row=3, column=0, pady=20)

root.mainloop()