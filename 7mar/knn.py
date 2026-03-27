import numpy as np
from sklearn.neighbors import NearestNeighbors

# Movie rating dataset
users = np.array([
    [5,1,1],  # User A
    [4,1,2],  # User B
    [1,5,4],  # User C
    [5,2,1]   # User D
])

# New user
new_user = np.array([[5,1,1]])

# KNN model
knn = NearestNeighbors(n_neighbors=2)
knn.fit(users)

distances, indices = knn.kneighbors(new_user)

print("Nearest neighbors:", indices)
print("Distances:", distances)