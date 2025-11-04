from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def segmenta_clienti(data):
    """
    Segmenta i clienti con K-Means in base a Quantità e SpesaTot.
    """
    features = data[['Quantità', 'SpesaTot']]
    X_scaled = StandardScaler().fit_transform(features)

    kmeans = KMeans(n_clusters=4, random_state=42)
    labels = kmeans.fit_predict(X_scaled)

    data['Cluster'] = labels
    silhouette = silhouette_score(X_scaled, labels)

    print(f"Silhouette Score: {silhouette:.3f}")
    return data, kmeans
