# Store Math Data here
import pandas as pd
import numpy as np
import random

def KMeans(danceability, energy, instrumentalness):
    """
    Runs the KMeans algorithm to find the closest songs to the user's preferences
    """


    # Get data
    data = pd.read_csv("Data/artist_data.csv")

    # Get the raw number data
    X = data[['danceability','energy','instrumentalness']]

    # Create K centroids, 30 iterations
    K = 80
    iterations = 30

    # Use 80 random points to set the centroids first position

    centroids = X.sample(K) 

    # For as many iterations
    for i in range(iterations):

        # Calculate the distance from each point to each centroid
        distances = []
        for j in range(K):
            distances.append(np.sqrt(np.sum((X - centroids.iloc[j])**2, axis=1)))

        # Assign each point to the closest centroid
        labels = np.argmin(distances, axis = 0)
        # Update the centroid position to the mean of closest points
        for j in range(K):
            centroids.iloc[j] = X.loc[labels == j].mean()

    # Find the closest centroid to the user's input
    target = [danceability, energy, instrumentalness]
    distances = np.sqrt(np.sum((centroids - target)**2, axis=1))
    closest_centroid = distances.argmin()



    # Second round to narrow the search to around 100 songs, instead of thousands 

    # Get the data of the closest centroid, and get the raw number data
    centroid_songs = data.loc[labels == closest_centroid]
    centroid_data = centroid_songs[['danceability','energy','instrumentalness']]

    # Create K centroids again, with k random points
    second_centroids = centroid_data.sample(K)

    # For as many iterations
    for i in range(iterations):

        # Calculate the distance from each point to each centroid
        second_distances = []
        for j in range(K):
            second_distances.append(np.sqrt(np.sum((centroid_data - second_centroids.iloc[j])**2, axis=1)))
            
        # Assign each point to the closest centroid
        second_labels = np.argmin(second_distances, axis = 0)
        for j in range(K):
            second_centroids.iloc[j] = centroid_data.loc[second_labels == j].mean()

    # Find the closest centroid to the user's input again
    second_distances = np.sqrt(np.sum((second_centroids - target)**2, axis=1))

    second_closest_centroid = second_distances.argmin()

    second_centroid_songs = centroid_data.loc[second_labels == second_closest_centroid]

    sample_5_songs = data.loc[data.index.isin(second_centroid_songs.index)].sample(5)

    # Return the 5 songs
    return sample_5_songs



   
def findClosestSongs(danceability, energy, instrumentalness):
    """
    Finds the closest songs to the user's using the euclidean distance
    """
    
    # Get data
    data = pd.read_csv("Data/artist_data.csv")

    # Get the raw number data
    X = data[['danceability','energy','instrumentalness']]
    
    # Find the closest songs to the user's input
    target = [danceability, energy, instrumentalness]
    distances = np.sqrt(np.sum((X - target)**2, axis=1))

    # Get the 5 closest songs
    closest_rows_indices = distances.argsort()[:5]
    closest_rows = data.iloc[closest_rows_indices]

    # Return the 5 songs
    return closest_rows


