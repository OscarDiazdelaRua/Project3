# This project is made by Oscar Diaz de la Rua, Sebastian Valdes, and Enrique Montanez

# PROJECT 3 - ARTIST RECOMMENDATION USING CLUSTERING

#Runs main.py
from equations import *
from HomePage import *
import pandas as pd



if __name__ == '__main__':
    
    home.resizable(False, False)
    window_width = 700
    window_height = 550



    screen_width = home.winfo_screenwidth()
    screen_height = home.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    home.title("MusicZone")
    home.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    welcomeLabel = Label(home, text="Welcome to the MusicZone!", font = "Consolas 16 bold italic")
    prefButton = Button(home, text="Select Preferences", font = "Consolas 12 bold italic", width = 20, padx=40, pady=30, command=selectPref1)
    algorithm1Button = Button(home, text="Use Algorithm 1", font = "Consolas 12 bold italic",width = 20, padx=40, pady=30, command=loadingScreen)
    algorithm2Button = Button(home, text="Use Algorithm 2", font = "Consolas 12 bold italic",width = 20, padx=40, pady=30)
    exitButton = Button(home, text="Exit", font = "Consolas 12 bold italic",width = 17, pady=20, command=home.destroy)
    questionButton = Button(home, text="?", font = "Consolas 12 bold italic",width = 7, pady=20, command=displayImage)
    
    welcomeLabel.pack()
    prefButton.pack(pady = 10)
    algorithm1Button.pack(pady = 25)
    algorithm2Button.pack(pady = 10)
    exitButton.pack(padx = (215,0),pady = 15, side= "left")
    questionButton.pack(padx =(0,215),pady = 15,side= "right")
    
    home.mainloop()

    # print("Input danceability")
    # danceability = float(input())
    # print("Input energy")
    # energy = float(input())
    # print("Input instrumentalness")
    # instrumentalness = float(input())

    # print("KMeans or closest songs? (K or C)")
    # choice = input()

    # if choice == "K":
    #     five_songs = KMeans(danceability, energy, instrumentalness)
    # elif choice == "C":
    #     five_songs = findClosestSongs(danceability, energy, instrumentalness)

    # print(five_songs)




