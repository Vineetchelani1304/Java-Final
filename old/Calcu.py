from tkinter import*
from PIL import Image, ImageTk
root = Tk()
root.geometry("1233x1563")
root.title("vineet chelani")

# image = Image.open("photo.jpg")
# photo=ImageTk.PhotoImage(image)
# label = Label(image=photo)
# label.pack()
vineet=Label(text="vineet is a good boy ",bg="blue", fg="white", padx=33, pady=84,font=("bold", 20), borderwidth=8,relief=SUNKEN)
vineet.pack( side=BOTTOM, anchor="se", fill=X)
vineet.pack()

root.mainloop()