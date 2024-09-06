Overview
This project focuses on analyzing user engagement metrics within a telecom dataset. The primary objective is to group users into distinct engagement clusters using K-means clustering. By leveraging various engagement metrics, we aim to derive insights that can inform marketing strategies, resource allocation, and service improvements.

Key Steps
Data Aggregation: User engagement metrics, such as session frequency, total session duration, and total traffic, are aggregated for each user based on their unique identifier.
K-means Clustering: The K-means clustering algorithm is applied to classify users into engagement clusters. The optimal number of clusters (
k
k) is determined using the elbow method, which helps identify the point where additional clusters provide diminishing returns in terms of inertia.
Visualization: The results of the clustering process are visualized through various plots, including the elbow curve, to illustrate the relationship between the number of clusters and the compactness of the clusters.
Analysis and Interpretation: Insights from the clustering results are analyzed to understand user behavior and engagement patterns, which can guide future business decisions.
