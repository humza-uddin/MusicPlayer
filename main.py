from tkinter import filedialog
from tkinter import * 
import customtkinter
import pygame
import os

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

window = customtkinter.CTk()
window.title('Music Player')
window.geometry("620x420")

pygame.mixer.init()

menubar= Menu(window)
window.config(menu=menubar)

songs = []
current_song = ""
pause = False

def load_music():
    global current_song
    window.directory = filedialog.askdirectory()
    
    for song in os.listdir(window.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]] 

def play_music():
    global current_song, pause

    if not pause:
        pygame.mixer.music.load(os.path.join(window.directory, current_song))
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        pause = False

def pause_music():
    global pause
    pygame.mixer.music.pause()
    pause = True
    

def next_music():
    global current_song, pause

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs(songlist.curselection()[0])
        play_music()
    except:
        pass


def previous_music():
    global current_song, pause

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs(songlist.curselection()[0])
        play_music()
    except:
        pass

browse_menu = Menu(menubar,tearoff=False)
browse_menu.add_command(label='Select Folder', command= load_music)
menubar.add_cascade(label='Browse',menu=browse_menu)

songlist = Listbox(window, bg= "black" , fg= "white" , width=100, height= 22)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
previous_btn_image = PhotoImage(file='previous.png')

control_frame = customtkinter.CTkFrame(window)
control_frame.pack(pady=0, padx=0, fill="both", expand=True)

play_btn = customtkinter.CTkButton(control_frame, image=play_btn_image, text='', command=play_music)
play_btn.grid(row=0, column=0, padx=7, pady=10)

pause_btn = customtkinter.CTkButton(control_frame, image=pause_btn_image, text='', command=pause_music)
pause_btn.grid(row=0, column=2, padx=7, pady=10)

next_btn = customtkinter.CTkButton(control_frame, image=next_btn_image, text='', command=next_music)
next_btn.grid(row=0, column=3, padx=7, pady=10)

previous_btn = customtkinter.CTkButton(control_frame, image=previous_btn_image, text='', command=previous_music)
previous_btn.grid(row=0, column=1, padx=7, pady=10)

window.mainloop()
