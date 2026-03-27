# ----------------------------------------
# Customer Segmentation using K-Means
# ----------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Example dataset (Annual Income vs Spending Score)
data = {
    "Annual_Income": [15,16,17,18,19,40,42,45,48,50,70,72,75,78,80],
    "Spending_Score": [39,35,40,42,38,60,65,63,70,68,20,18,15,22,25]
}

df = pd.DataFrame(data)

# Select features
X = df[['Annual_Income','Spending_Score']]

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=42)

# Train model
df['Cluster'] = kmeans.fit_predict(X)

# Plot clusters
plt.scatter(df['Annual_Income'], df['Spending_Score'], c=df['Cluster'])
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation (K-Means)")
plt.show()