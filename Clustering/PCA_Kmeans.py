import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Load ECFP6 fingerprints and SMILES from file
data = pd.read_csv('unique_smiles_ECFP6.csv')
fingerprints = data.iloc[:, 1:].values
smiles_list = data['smiles'].tolist()

# Reduce dimensionality using PCA
pca = PCA(n_components=2, random_state=42)
fingerprints_pca = pca.fit_transform(fingerprints)

# Calculate distortion (inertia) and silhouette score for different values of k
distortions = []
silhouette_scores = []
K = range(2, 12)  # Fix range to include 2 to 11
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    cluster_labels = kmeans.fit_predict(fingerprints_pca)
    distortions.append(kmeans.inertia_)
    silhouette_avg = silhouette_score(fingerprints_pca, cluster_labels)
    silhouette_scores.append(silhouette_avg)

# Find optimal k using the elbow method (max silhouette score)
optimal_k = K[np.argmax(silhouette_scores)]

# Perform k-means clustering with optimal k
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
cluster_labels = kmeans.fit_predict(fingerprints_pca)

# Visualize clustering results
plt.figure(figsize=(10, 8))
for i in range(optimal_k):
    cluster_members = np.where(cluster_labels == i)[0]
    plt.scatter(fingerprints_pca[cluster_members, 0], fingerprints_pca[cluster_members, 1], label=f'Cluster {i+1}')
plt.title('K-means Clustering of Molecule Data')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend()
plt.show()

# Save DataFrame with K-means clustering results and other metrics to CSV file
cluster_data = pd.DataFrame({
    'SMILES': smiles_list,
    'Cluster_Label': cluster_labels,
    'PCA_Component_1': fingerprints_pca[:, 0],
    'PCA_Component_2': fingerprints_pca[:, 1],
})
cluster_data.to_csv('clustering_results.csv', index=False)

# Save DataFrame with clustering metrics to CSV file
cluster_metrics = pd.DataFrame({
    'Number_of_Clusters': K,
    'Distortion': distortions,
    'Silhouette_Score': silhouette_scores
})
cluster_metrics['Optimal_K'] = optimal_k
cluster_metrics.to_csv('clustering_metrics.csv', index=False)
