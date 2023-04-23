# Store Math Data here
import pandas as pd
import numpy as np
import random
def KMeans(danceability, energy, instrumentalness):
    # KMeans
    # algoritrm for k-means clustering
    danceability = 0.5
    energy = 0.5
    instrumentalness = 0.5

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
    # calculate distance using distance formula, use argmin to find the closest centroid
        distances = np.sqrt(((X - centroids)**2).sum(axis=1))
        print(centroids.iloc[0])
        labels = np.argmin(distances, axis = 0)
        # update centroids by setting them as the mean of all points assigned to that centroid 
        for j in range(K):
            # j corresponds to the centriod
            # TODO: update the centroids 
            # placeholder causing key error
            print(j)
    for i in range(K):
        print(f'Cluster {j+1}:')
        print(data[['artist', 'song']].loc[labels == j])
        print('\n')# number each cluster from one to ten



   
def findClosestSongs(danceability, energy, instrumentalness):
    

    data = pd.read_csv("Data/artist_data.csv")

    X = data[['danceability','energy','instrumentalness']]

    target = [danceability, energy, instrumentalness]

    distances = np.sqrt(np.sum((X - target)**2, axis=1))

    closest_rows_indices = distances.argsort()[:5]

    closest_rows = data.iloc[closest_rows_indices]
    
    return closest_rows

