# This project is made by Oscar Diaz de la Rua, Sebastian Valdes, and Enrique Montanez

# PROJECT 3 - ARTIST RECOMMENDATION USING CLUSTERING

#Runs main.py
from equations import *
import pandas as pd

if __name__ == '__main__':
    
    # print("Input danceability")
    # danceability = float(input())
    # print("Input energy")
    # energy = float(input())
    # print("Input instrumentalness")
    # instrumentalness = float(input())

    danceability = 0.5
    energy = 0.5
    instrumentalness = 0.5

    KMeans(danceability, energy, instrumentalness)
    # findClosestSongs(danceability, energy, instrumentalness)
    # def DBSCAN(danceability, energy, instrumentalness):


