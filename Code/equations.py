# Store Math Data here
import pandas as pd
import numpy as np
import random
def KMeans(danceability, energy, instrumentalness):
    # KMeans
    # algoritrm for k-means clustering

 # id,name,artists,danceability,energy,instrumentalness
    # read in the data
    data = pd.read_csv("Data/artist_data.csv")

    # determine the data used to 
    X = data[['danceability','energy','instrumentalness']]

    # number of clusters
    K = 10
    it = 20
    # initial a new random seed
    random.seed((danceability + energy + instrumentalness)*100)
    # set the centroids to be random points from the data
    centroids = X.sample(K, random_state=random.randint(0, 100)).reset_index(drop = True)   

 
   
    
    for i in range(it):
    # calculate distance using distance formula, use argmin to find the closest centroid
        distances = np.sqrt(((X - centroids.iloc[0])**2).sum(axis=1))
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



   
def DBSCAN(danceability, energy, instrumentalness):
    # DBSCAN
    pass
