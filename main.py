from tkinter import filedialog
from tkinter import * 
import pygame
import os

window = Tk()
window.title('Music Player')
window.geometry("600x400")

pygame.mixer.init()

menubar= Menu(window)
window.config(menu=menubar)

organise_menu = Menu(menubar)
organise_menu.add_command(label='Select Folder')
menubar.add_cascade(label='Organise',menu=organise_menu)

def browser_button():
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

folder_path = StringVar()
lbl1 = Label(master=window, textvariable = folder_path)
button2 = Button(text="Browse", command=browser_button)

songlist = Listbox(window, bg= "black" , fg= "white" , width=100, height= 22)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
previous_btn_image = PhotoImage(file='previous.png')

control_frame =  Frame(window)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0)
play_btn.grid(row=0, column=0, padx=7, pady=10)

pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0)
pause_btn.grid(row=0, column=2, padx=7, pady=10)

next_btn = Button(control_frame, image=next_btn_image, borderwidth=0)
next_btn.grid(row=0, column=3, padx=7, pady=10)

previous_btn = Button(control_frame, image=previous_btn_image, borderwidth=0)
previous_btn.grid(row=0, column=1, padx=7, pady=10)

pygame.mixer.music.load(r"C:\Users\DELL\Music\kyon.mp3")

pygame.mixer.music.play()


window.mainloop()