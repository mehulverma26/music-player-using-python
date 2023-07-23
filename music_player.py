# Importing Required Modules & libraries
from tkinter import *
import pygame
import os


# Defining MusicPlayer Class
class MusicPlayer:
    # Defining Constructor
    def __init__(self, root):
        self.root = root
        # Title of the window
        self.root.title("Music Player")
        # Window Geometry
        self.root.geometry("1000x200")
        # Initiating Pygame
        pygame.init()
        # Initiating Pygame Mixer
        pygame.mixer.init()
        # Declaring track Variable
        self.track = StringVar()
        # Declaring Status Variable
        self.status = StringVar()
        # Creating Track Frame for Song label & status label
        trackframe = LabelFrame(
            self.root,
            text="Song Track",
            font=("times new roman", 15, "bold"),
            bg="grey",
            fg="white",
            bd=5,
            relief=GROOVE,
        )
        trackframe.place(x=0, y=0, width=700, height=100)
        # Inserting Song Track Label
        songtrack = Label(
            trackframe,
            textvariable=self.track,
            width=20,
            font=("times new roman", 24, "bold"),
            bg="grey",
            fg="gold",
        ).grid(row=0, column=0, padx=10, pady=5)
        # Inserting Status Label
        trackstatus = Label(
            trackframe,
            textvariable=self.status,
            font=("times new roman", 24, "bold"),
            bg="grey",
            fg="gold",
        ).grid(row=0, column=1, padx=10, pady=5)
        # Creating Button Frame
        buttonframe = LabelFrame(
            self.root,
            text="Control Panel",
            font=("times new roman", 15, "bold"),
            bg="grey",
            fg="white",
            bd=5,
            relief=GROOVE,
        )
        buttonframe.place(x=0, y=100, width=700, height=100)
        # Inserting Play Button
        playbtn = Button(
            buttonframe,
            text="PLAY",
            command=self.playsong,
            width=6,
            height=1,
            font=("times new roman", 16, "bold"),
            fg="navyblue",
            bg="gold",
        ).grid(row=0, column=0, padx=10, pady=5)
        # Inserting Pause Button
        playbtn = Button(
            buttonframe,
            text="PAUSE",
            command=self.pausesong,
            width=8,
            height=1,
            font=("times new roman", 16, "bold"),
            fg="navyblue",
            bg="gold",
        ).grid(row=0, column=1, padx=10, pady=5)
        # Inserting Unpause Button
        playbtn = Button(
            buttonframe,
            text="UNPAUSE",
            command=self.unpausesong,
            width=10,
            height=1,
            font=("times new roman", 16, "bold"),
            fg="navyblue",
            bg="gold",
        ).grid(row=0, column=2, padx=10, pady=5)
        # Inserting Stop Button
        playbtn = Button(
            buttonframe,
            text="STOP",
            command=self.stopsong,
            width=6,
            height=1,
            font=("times new roman", 16, "bold"),
            fg="navyblue",
            bg="gold",
        ).grid(row=0, column=3, padx=10, pady=5)
        playbtn = Button(
            buttonframe,
            text="REPEAT",
            command=self.repeat,
            width=8,
            height=1,
            font=("times new roman", 16, "bold"),
            fg="navyblue",
            bg="gold",
        ).grid(row=0, column=4, padx=10, pady=5)
        # playbtn = Button(buttonframe,text="PLAY ALL",command=self.play_all,width=9,height=1,font=("times new roman",16,"bold"),fg="navyblue",bg="gold").grid(row=1,column=0,padx=10,pady=5)
        # Creating Playlist Frame
        songsframe = LabelFrame(
            self.root,
            text="Song Playlist",
            font=("times new roman", 15, "bold"),
            bg="grey",
            fg="white",
            bd=5,
            relief=GROOVE,
        )
        songsframe.place(x=700, y=0, width=300, height=200)
        # Inserting scrollbar
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        # Inserting Playlist listbox
        self.playlist = Listbox(
            songsframe,
            yscrollcommand=scrol_y.set,
            selectbackground="gold",
            selectmode=SINGLE,
            font=("times new roman", 12, "bold"),
            bg="silver",
            fg="navyblue",
            bd=5,
            relief=GROOVE,
        )
        # Applying Scrollbar to listbox
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        # Changing Directory for fetching Songs
        os.chdir("D:/FRIDAY/music player/music")  # path of the folder for music
        # Fetching Songs
        songtracks = os.listdir()
        # Inserting Songs into Playlist
        for track in songtracks:
            self.playlist.insert(END, track)

    # Defining Play Song Function
    def playsong(self):
        # Displaying Selected Song title
        self.track.set(self.playlist.get(ACTIVE))
        # Displaying Status
        self.status.set("-Playing")
        # Loading Selected Song
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        # Playing Selected Song
        pygame.mixer.music.play()

    def stopsong(self):
        # Displaying Status
        self.status.set("-Stopped")
        # Stopped Song
        pygame.mixer.music.stop()

    def pausesong(self):
        # Displaying Status
        self.status.set("-Paused")
        # Paused Song
        pygame.mixer.music.pause()

    def unpausesong(self):
        # Displaying Status
        self.status.set("-Playing")
        # Playing back Song
        pygame.mixer.music.unpause()

    def repeat(self):
        self.status.set("-On Loop")
        pygame.mixer.music.play(-1)

    def play_all(self):
        self.track = StringVar()
        self.status.set("-Playing All Music")
        lists_of_songs = os.listdir(
            "D:/FRIDAY/music player/music/"
        )  # path of the folder for music
        for song in lists_of_songs:
            if song.endswith(".mp3"):
                file_path = (
                    "D:/FRIDAY/music player/music/" + song
                )  # path of the folder for music + song
                pygame.mixer.music.load(str(file_path))
                pygame.mixer.music.play()
                # print("Playing::::: " + song)
                while pygame.mixer.music.get_busy() == True:
                    continue


# Creating TK Container
root = Tk()
# Passing Root to MusicPlayer Class
MusicPlayer(root)
# Root Window Looping
root.mainloop()
