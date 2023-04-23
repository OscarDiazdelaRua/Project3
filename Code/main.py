# This project is made by Oscar Diaz de la Rua, Sebastian Valdes, and Enrique Montanez

# PROJECT 3 - ARTIST RECOMMENDATION USING CLUSTERING

#Runs main.py
from equations import *
from HomePage import *
import pandas as pd

if __name__ == '__main__':
    
    homePage()



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




