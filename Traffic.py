import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

#Assuming you have a dataset with traffic-related features (e.g., time of day, traffic volume)
#Replace 'your_dataset.csv' with the actual path or URL of your dataset
data pd.read_csv('traffic_flow.csv')

#Assuming 'hour' and 'traffic_volume' are relevant features for analysis
features data [['hour', 'traffic_volume']]

# Standardise the features (important for k-means)
features_standardized (features features.mean()) / features.std()

#Determine the optimal number of clusters (k) using the elbow method
WCSS = [ ]
for i in range(1,21):
kmeans KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
kmeans.fit(features_standardized)
wcss.append(kmeans.inertia_)

#Plot the elbow curve
plt.plot(range(1,21), wcss)
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Within-Cluster Sum of Squares (WCSS)')
plt.show()

#Based on the elbow method, choose an optimal value for k
optimal_k 3

#Apply k-means clustering with the chosen k
kmeans KMeans(n_clusters optimal_k, init='k-means++', max_iter=300, n_init=10, random_state=0)
features['cluster'] = kmeans.fit_predict(features_standardized)

# Visualise the clusters
plt.scatter(features['hour'], features['traffic_volume'], c=features['cluster'], cmap='viridis')
plt.title('Traffic Pattern Clusters')
plt.xlabel('Hour of Day')
plt.ylabel('Traffic Volume')
plt.show()