# Store Math Data here
import pandas as pd
import numpy as np
import random
import time

def KMeans(danceability, energy, instrumentalness):
    # KMeans
    # algoritrm for k-means clustering

    start_time = time.time()

 # id,name,artists,danceability,energy,instrumentalness
    # read in the data
    data = pd.read_csv("Data/artist_data.csv")

    # determine the data used to 
    X = data[['danceability','energy','instrumentalness']]

    # number of clusters
    K = 10
    iterations = 20
    # initial a new random seed
    random.seed((danceability + energy + instrumentalness)*100)
    # set the centroids to be random points from the data
    centroids = X.sample(K, random_state=random.randint(0, 100)).reset_index(drop = True)   

    for i in range(iterations):

        distances = []
        for j in range(K):
            distances.append(np.sqrt(np.sum((X - centroids.iloc[j])**2, axis=1)))

         # Compute the mean of the data points for each centroid to get the new centroid location
        labels = np.argmin(distances, axis = 0)
        for j in range(K):
            centroids.iloc[j] = X.loc[labels == j].mean()

    target = [danceability, energy, instrumentalness]

    #find closest centroid

    distances = np.sqrt(np.sum((centroids - target)**2, axis=1))

    closest_centroid = distances.argmin()
    
    #create array with centroid songs

    centroid_songs = data.loc[labels == closest_centroid]

    centroid_data = centroid_songs[['danceability','energy','instrumentalness']]

    second_centroids = centroid_data.sample(K, random_state=random.randint(0, 100)).reset_index(drop = True)

    for i in range(iterations):
        second_distances = []
        for j in range(K):
            second_distances.append(np.sqrt(np.sum((centroid_data - second_centroids.iloc[j])**2, axis=1)))

            # Compute the mean of the data points for each centroid to get the new centroid location
        second_labels = np.argmin(second_distances, axis = 0)
        for j in range(K):
            second_centroids.iloc[j] = centroid_data.loc[second_labels == j].mean()
        # run k means again

    second_distances = np.sqrt(np.sum((second_centroids - target)**2, axis=1))

    second_closest_centroid = distances.argmin()

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"The function took {elapsed_time} seconds to run.")
    print("Test")



   
def findClosestSongs(danceability, energy, instrumentalness):
    

    data = pd.read_csv("Data/artist_data.csv")

    X = data[['danceability','energy','instrumentalness']]

    target = [danceability, energy, instrumentalness]

    distances = np.sqrt(np.sum((X - target)**2, axis=1))

    closest_rows_indices = distances.argsort()[:5]

    closest_rows = data.iloc[closest_rows_indices]
    
    return closest_rows

