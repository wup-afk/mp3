import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
import tkinter
from tkinter import *



root = Tk()
root.minsize(300,300)

songslist = []

v = StringVar()
songlabel = Label(root,textvariable=v, width=35)

index = 0

def nextsong(event):
    global index
    index += 1
    pygame.mixer.music.load(songslist[index])
    pygame.mixer.music.play()
    updatelabel()

def previoussong(event):
    global index
    index -= 1
    pygame.mixer.music.load(songslist[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):
    pygame.mixer.music.stop()
    v.set("Song is not playing atm")
    return songname

def updatelabel():
    global index
    global songname
    v.set(songslist[index])
    return songname


def directorychooser():

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            songslist.append(files)
            print(files)
    pygame.mixer.init()
    pygame.mixer.music.load(songslist[0])
    pygame.mixer.music.play()



label = Label(root,text="Mp3 player")
label.pack()
listbox = Listbox(root)
listbox.pack()

directorychooser()


songslist.reverse()

for items in songslist:
    listbox.insert(0,items)

nextbutton = Button(root,text = "Next song")
nextbutton.pack()

previousbutton = Button(root,text = "Previous song")
previousbutton.pack()

stopbutton = Button(root,text= "Stop music")
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",previoussong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()



root.mainloop()