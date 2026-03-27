import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample mall dataset
data = {
    "Income": [15,16,17,18,19,40,42,45,48,50,70,72,75,78,80],
    "Spending": [39,35,40,42,38,60,65,63,70,68,20,18,15,22,25]
}

df = pd.DataFrame(data)

X = df[['Income','Spending']]

kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

plt.scatter(df['Income'], df['Spending'], c=df['Cluster'])
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation")
plt.show()