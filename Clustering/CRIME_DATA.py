""""CRIME DATA""""
import pandas as pd
import matplotlib.pylab as plt 
crime = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Clustering\\crime_data.csv")
crime.head()

crime.head(5)
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)


# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(crime.iloc[:,1:])# EXCLUDING FIRST COLUMN
df_norm.head(5)
from scipy.cluster.hierarchy import linkage 

import scipy.cluster.hierarchy as sch # for creating dendrogram 

type(df_norm)

 
help(linkage)
z = linkage(df_norm, method="complete",metric="euclidean")

plt.figure(figsize=(15, 5));plt.title('Hierarchical Clustering Dendrogram');plt.xlabel('Index');plt.ylabel('Distance')
sch.dendrogram(
    z,
    leaf_rotation=0.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()


from	sklearn.cluster	import	AgglomerativeClustering 
h_complete	=	AgglomerativeClustering(n_clusters=3,	linkage='complete',affinity = "euclidean").fit(df_norm) 


cluster_labels=pd.Series(h_complete.labels_)

crime['clust']=cluster_labels # creating a  new column and assigning it to new column 
crime = crime.iloc[:,[5,0,1,2,3,4]]
crime.head()


# getting aggregate mean of each cluster
crime.iloc[:,2:].groupby(crime.clust).median()
"""
WHEN IT WAS 4 WE DID NOT GET PROPER CONCLUSION SO MKING IT AS 3 CLUSTERS NOW 

       Murder  Assault  UrbanPop   Rape
clust                                  
0        13.8      254        53  22.35
1         6.0      145        70  18.80
2        11.3      255        80  31.90
3         2.4       82        52  11.25
"""

"""
WHEN IT WAS 3 CLUSTERS WE CAN SAY IT IS PROPER CONCLUSION AS 

       Murder  Assault  UrbanPop   Rape
clust                                  
0         4.9      113        66  16.30
1        13.8      254        53  22.35
2        11.3      255        80  31.90

WHEN THE UrbanPop EVEN WAS CONDUCTED THEN MURDER ARE 11 255 ASSAULT AND RAPES ARE 31
MEANS MORE NUMBER OF TIMES THE EVENT IS CONDUCTD THE MORE OF CRIMES ARE HAPPENING
"""
# creating a csv file 
#Univ.to_csv("University_cluster.csv",encoding="utf-8")


