import numpy as np
import math
import random 
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
sns.set()


import pandas as pd
#def main():
data=pd.read_excel('Workbook1.xlsx')
data.columns=["x_coordinates","y_coordinates"]
x_coords=list(data.x_coordinates)
y_coords=list(data.y_coordinates)
points_coordinates=zip(x_coords,y_coords)

print len(points_coordinates)
plt.scatter(x_coords,y_coords)
plt.show()

def find_cost(centroids,points_of_all_clusters): #2 nd argument is list of lists  of points
    cost=0
    #print 'len_centroids=',len(centroids)
    print 'len_cen',len(centroids)
    print 'len_plts',len(points_of_all_clusters)
    for i in range(len(centroids)):
        for j in range(len(points_of_all_clusters[i])):
            cost=cost+(points_of_all_clusters[i][j][0]-centroids[i][0])**2 + (points_of_all_clusters[i][j][1]-centroids[i][1])**2
    #print 'i+j=',i+j
    return cost
#correct

def find_distance(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
#correct


def decide_clusters(cluster_centroids,points_coordinates):
    determined_centroids=[]
    for i in range(len(points_coordinates)):
        distances=[find_distance(points_coordinates[i],centroid) for centroid in cluster_centroids]
        min_index=distances.index(min(distances))
        determined_centroids.append(min_index)
        
    return determined_centroids
#correct

def make_centroid_list_for_each_pt(determined_centroids,points_coordinates):
    points_of_all_clusters=[]
    pres_centroid_nums=list(set(determined_centroids))
    indexes_list=[]
    #print 'pres',pres_centroid_nums
    for unique_centroid in pres_centroid_nums:
        each_cluster_list_indexes=[]
        each_cluster_points=[]
        for j in range(len(determined_centroids)):
            if unique_centroid==determined_centroids[j]:
                each_cluster_list_indexes.append(j)
        each_cluster_points=[points_coordinates[i] for i in each_cluster_list_indexes]
        #print 'e',each_cluster_points
        points_of_all_clusters.append(each_cluster_points)
    
    return points_of_all_clusters
#correct

def compute_clusters_centroids(points_of_all_clusters):
    cluster_centroid_list=[]
    for each_cluster in points_of_all_clusters:
        cluster_centre=None
        x_coords=[point[0] for point in each_cluster]
        y_coords=[point[1] for point in each_cluster]
        x_mean=sum(x_coords)*1.0/len(x_coords)
        y_mean=sum(y_coords)*1.0/len(y_coords)
        cluster_centroid_list.append([x_mean,y_mean])
    return cluster_centroid_list
#correct

def k_means(no_of_clusters,points_coordinates,epsilon): #pts_crds-> list of lists
    
    cluster_centroids=[[random.uniform(-12,12),random.uniform(-12,12)]for i in range(no_of_clusters)]
    #print cluster_centroids
    print 'init_centroids=',cluster_centroids
    determined_centroids=decide_clusters(cluster_centroids,points_coordinates)
    points_of_all_clusters=make_centroid_list_for_each_pt(determined_centroids,points_coordinates)
    #print 'balal',points_of_all_clusters[0][3]
    C_new=find_cost(cluster_centroids,points_of_all_clusters)
    print 'find_cost1',C_new
    new_cluster_centers=None
    C_old=0
    i=0
    while(abs(C_new-C_old) >= epsilon ) :
        i=i+1
        print i
        C_old=C_new
        print C_old,'C_old'
        determined_centroids=decide_clusters(cluster_centroids,points_coordinates)
        points_of_all_clusters=make_centroid_list_for_each_pt(determined_centroids,points_coordinates)
        cluster_centroids=compute_clusters_centroids(points_of_all_clusters)
        C_new=find_cost(cluster_centroids,points_of_all_clusters)
        #print 'clc',cluster_centroids
        #print 'find_cost=',find_cost(new_cluster_centers,points_of_all_clusters)
        print C_new,'C_new'
        
    
    return cluster_centroids,points_of_all_clusters,C_new,determined_centroids

output=k_means(5,points_coordinates,0.001)
print 'centeres=',output[0]
print 'cost=',output[2]

data['Memberships'] = output[3]
sns.scatterplot(data=data, x="x_coordinates", y ="y_coordinates", hue="Memberships", style="Memberships")
plt.show()


