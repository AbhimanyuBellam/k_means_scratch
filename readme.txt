Files:
1. "Workbook1.xlsx" - excel file contains the data of Data Set 4. 
2. "output_file.txt" - coordinates and memberships (4/5 fth part of data set) after running through the data set.
3. "data_set_clusters_image.png" - image of the clusters of the data set
4. "cost_and_iter_vs_k.png" - image of the graph comparing number of iterations and cost vs number of clusters.
5. "test_file.txt" - 1/5 fth part of the data that we extracted
6. "centroid_info.txt" - centroid coordinates generated after clustering
7. "test_data_output_file.txt" - coordinates and memberships of the tested data
8. "test_data_set_clusters_image.png" - image of the clusters of the test set

Code:
All of the code has been done in the jupyter notebook. 
For bad random initilizations of the centroid, the code will not perform as expected, and will prompt the user to run it again. Please run again, when prompted. 

Observations:
1. The output when tested on the test data is very close to as expected, i.e, the shapes of the test data outputs are to a good extent close enough to that of the data set output clusters.
2. For different initial centroids, the best possible number of clusters sometimes changes, but mostly we get 7 clusters. 
3. The cost has been decreasing with increasing number of clusters as expected.
4. The number of iterations varies depending on the initial centroids. 

Team:
1. Asish Potnuru        (16XJ1A0133)
2. Abhimanyu Bellam     (16XJ1A0503)
3. Aadi Jain            (16XJ1A0501)
4. Srija Gurijala       (16XJ1A0550)


