""""AIRLINES""""
import pandas as pd
import matplotlib.pylab as plt 
airline = pd.read_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Clustering\\EastWestAirlines_1.csv")
airline.head()

airline.head(5)
def norm_func(i):
    x = (i-i.mean())/(i.std())
    return (x)

# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(airline.iloc[:,1:])
df_norm.head(10)
k = list(range(2,15))
k
TWSS = [] # variable for storing total within sum of squares for each kmeans 
for i in k:
    kmeans = KMeans(n_clusters = i)
    kmeans.fit(df_norm)
    WSS = [] # variable for storing within sum of squares for each cluster 
    for j in range(i):
        WSS.append(sum(cdist(df_norm.iloc[kmeans.labels_==j,:],kmeans.cluster_centers_[j].reshape(1,df_norm.shape[1]),"euclidean")))
    TWSS.append(sum(WSS))



# Scree plot 
plt.plot(k,TWSS, 'ro-');plt.xlabel("No_of_Clusters");plt.ylabel("total_within_SS");plt.xticks(k)

# Selecting 5 clusters from the above scree plot which is the optimum number of clusters 
model=KMeans(n_clusters=6) 
model.fit(df_norm)

model.labels_ # getting the labels of clusters assigned to each row 
md=pd.Series(model.labels_)  # converting numpy array into pandas series object 
airline['clust']=md # creating a  new column and assigning it to new column 
airline.head()
import os
cwd = os.getcwd()
airline = airline.iloc[:,[12,0,1,2,3,4,5,6,7,8,9,10,11,]]

airline.iloc[:,1:7].groupby(airline.clust).mean()

airline.to_csv("C:\\EXCELR\\NOTES WRITTEN\\SOLVING_ASSIGNMENTS\\Clustering\\CLUSTERED_K_MEAN_Univsersity.csv")
