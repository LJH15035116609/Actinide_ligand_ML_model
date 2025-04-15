import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN, SpectralClustering, Birch, MeanShift, AffinityPropagation, OPTICS, MiniBatchKMeans
from sklearn.metrics import silhouette_score

# Load ECFP6 fingerprints and SMILES from file
data = pd.read_csv('unique_smiles_ECFP6.csv')
fingerprints = data.iloc[:, 1:].values

# Reduce dimensionality using PCA
pca = PCA(n_components=2, random_state=42)
fingerprints_pca = pca.fit_transform(fingerprints)

# Define a dictionary of clustering algorithms
clustering_algorithms = {
    'KMeans': KMeans(),
    'AgglomerativeClustering': AgglomerativeClustering(),
    'DBSCAN': DBSCAN(eps=1.5),
    'SpectralClustering': SpectralClustering(random_state=42),
    'Birch': Birch(),
    'MiniBatchKMeans': MiniBatchKMeans()
}

# Define range of n_clusters
n_clusters_range = range(2, 8)

# Calculate silhouette score for each clustering algorithm and n_clusters
silhouette_scores = {}
for name, algorithm in clustering_algorithms.items():
    silhouette_scores[name] = []
    for n_clusters in n_clusters_range:
        if name in ['DBSCAN']:
            # Clustering algorithms that don't require predefined number of clusters
            cluster_labels = algorithm.fit_predict(fingerprints)
            if len(np.unique(cluster_labels)) < 2:
                # Skip if only one cluster is found
                silhouette_scores[name].append(np.nan)
                continue
        else:
            cluster_labels = algorithm.set_params(n_clusters=n_clusters).fit_predict(fingerprints_pca)
        silhouette_avg = silhouette_score(fingerprints_pca, cluster_labels)
        silhouette_scores[name].append(silhouette_avg)

# Plot silhouette scores for each clustering algorithm
plt.figure(figsize=(12, 8))
for name, scores in silhouette_scores.items():
    plt.plot(n_clusters_range, scores, label=name)
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.title('Silhouette Score vs. Number of Clusters for Different Clustering Algorithms')
plt.legend()
plt.show()

# Save silhouette scores to CSV file
silhouette_df = pd.DataFrame(silhouette_scores, index=n_clusters_range)
silhouette_df.index.name = 'Number_of_Clusters'
silhouette_df.to_csv('PCA_clustering_silhouette_scores.csv')
