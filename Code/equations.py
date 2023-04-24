# Store Math Data here
import pandas as pd
import numpy as np
import random

def KMeans(danceability, energy, instrumentalness):




    data = pd.read_csv("Data/artist_data.csv")


    X = data[['danceability','energy','instrumentalness']]


    K = 50
    iterations = 30

    random.seed((danceability + energy + instrumentalness)*100)

    centroids = X.sample(K) 

    for i in range(iterations):

        distances = []
        for j in range(K):
            distances.append(np.sqrt(np.sum((X - centroids.iloc[j])**2, axis=1)))

        labels = np.argmin(distances, axis = 0)
        for j in range(K):
            centroids.iloc[j] = X.loc[labels == j].mean()

    target = [danceability, energy, instrumentalness]

    distances = np.sqrt(np.sum((centroids - target)**2, axis=1))

    closest_centroid = distances.argmin()
    
    # Second round 

    centroid_songs = data.loc[labels == closest_centroid]

    centroid_data = centroid_songs[['danceability','energy','instrumentalness']]

    # closest_songs = KmeansHelper(danceability, energy, instrumentalness, centroid_data, K, iterations)

    # return closest_songs

    second_centroids = centroid_data.sample(K)

    for i in range(iterations):
        second_distances = []
        for j in range(K):
            second_distances.append(np.sqrt(np.sum((centroid_data - second_centroids.iloc[j])**2, axis=1)))
            
        second_labels = np.argmin(second_distances, axis = 0)
        for j in range(K):
            second_centroids.iloc[j] = centroid_data.loc[second_labels == j].mean()


    second_distances = np.sqrt(np.sum((second_centroids - target)**2, axis=1))

    second_closest_centroid = second_distances.argmin()

    second_centroid_songs = centroid_data.loc[second_labels == second_closest_centroid]

    sample_5_songs = data.loc[data.index.isin(second_centroid_songs.index)].sample(5)


    return sample_5_songs



   
def findClosestSongs(danceability, energy, instrumentalness):
    
    

    data = pd.read_csv("Data/artist_data.csv")

    X = data[['danceability','energy','instrumentalness']]

    target = [danceability, energy, instrumentalness]

    distances = np.sqrt(np.sum((X - target)**2, axis=1))

    closest_rows_indices = distances.argsort()[:5]

    closest_rows = data.iloc[closest_rows_indices]
    
    return closest_rows

