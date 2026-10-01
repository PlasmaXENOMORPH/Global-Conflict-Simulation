import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os
from tkinter import PhotoImage

window = tk.Tk()
window.title("CON-SEM v1.0.0.0");

window.iconbitmap("C:/Users/temmy/OneDrive/Desktop/CONSEM/ICON/ICONIC.ico")

#Close Window
def handle_button_press(event):
    window.destroy()

#button.pack(anchor=tk.NW)



DesktopImage = ImageTk.PhotoImage(Image.open("C:/Users/temmy/OneDrive/Documents/102237.jpg"))
panel = Label(window, image = DesktopImage)
panel.pack(side = "bottom", fill = "both", expand = "yes")



twitterIcon = PhotoImage(file = "C:/Users/temmy/OneDrive/Desktop/CONSEM/TWIT.png") 
chatIcon = PhotoImage(file = "C:/Users/temmy/OneDrive/Desktop/CONSEM/CHAT.png") 
adminToolIcon = PhotoImage(file= "C:/Users/temmy/OneDrive/Desktop/CONSEM/TOOL.png")
animatedBackgroundTest = PhotoImage(file ="C:/Users/temmy/OneDrive/Desktop/CONSEM/giphy.gif")

button = tk.Button(text=" ", image=twitterIcon)
button.bind("<Button-1>", handle_button_press)
button.place(x=50, y=50, width=150, height=150)

button = tk.Button(text=" ", image=chatIcon)
button.bind("<Button-1>", handle_button_press)
button.place(x=50, y=250, width=150, height=150)

button = tk.Button(text=" ", image=adminToolIcon)
button.bind("<Button-1>", handle_button_press)
button.place(x=50, y=450, width=150, height=150)






#
#
#
#Display animated Gif
#
#
#

















# Start the event loop.
window.mainloop()

