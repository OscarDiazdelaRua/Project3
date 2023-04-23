# This project is made by Oscar Diaz de la Rua, Sebastian Valdes, and Enrique Montanez

# PROJECT 3 - ARTIST RECOMMENDATION USING CLUSTERING

#Runs main.py
from equations import *
from HomePage import *
import pandas as pd

if __name__ == '__main__':
    
    # homePage()

    prefWindow = Tk()

    prefWindow.title("Example")
    prefWindow.geometry("500x500")
    img = Image.open("Data/Algovisualcomparison.PNG")
    img = img.resize((500, 500), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    
    panel = Label(prefWindow, image = img)

    panel.pack(side = "bottom", fill = "both", expand = "yes")

    print("Input danceability")
    danceability = float(input())
    print("Input energy")
    energy = float(input())
    print("Input instrumentalness")
    instrumentalness = float(input())

    print("KMeans or closest songs? (K or C)")
    choice = input()

    if choice == "K":
        five_songs = KMeans(danceability, energy, instrumentalness)
    elif choice == "C":
        five_songs = findClosestSongs(danceability, energy, instrumentalness)

    print(five_songs)




