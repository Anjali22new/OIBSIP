# Task 2 · Customer Segmentation Analysis

## Objective
Applied RFM analysis and K-Means clustering to segment customers based on 
purchasing behaviour, enabling targeted marketing strategies.

## Dataset
[Online Retail II (UCI, via Kaggle)](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
— 1,067,371 transactions, cleaned to 805,620 valid rows across 5,881 unique customers.

## Tech Stack
Python, pandas, scikit-learn (K-Means, StandardScaler), matplotlib

## Approach
- Built RFM (Recency, Frequency, Monetary) features per customer from ~805K transactions
- Standardized features using StandardScaler before clustering
- Used the Elbow Method to determine optimal cluster count (K=4)
- Applied K-Means clustering and profiled each segment
- Visualized clusters using scatter plots (linear and log scale) and cluster size distribution

## Key Insights
- **Cluster 0 (n=3,842) — Regular Customers:** moderate recency/frequency, average spend ~₹3,000
- **Cluster 1 (n=2,000) — Lapsed Customers:** haven't purchased in ~463 days on average
- **Cluster 2 (n=35) — High-Value Loyal Customers:** frequent buyers, high spend (~₹83K avg)
- **Cluster 3 (n=4) — Extreme Outliers:** likely wholesale/B2B accounts — 200+ orders, ~₹437K avg spend
- 99%+ of customers fall into just 2 of the 4 segments, while a tiny high-value group drives disproportionate revenue — a classic 80/20 pattern

## Marketing Recommendations
1. Protect high-value/wholesale accounts (Clusters 2 & 3) with dedicated retention efforts
2. Standard engagement campaigns for regular customers (Cluster 0) to grow frequency
3. Win-back campaigns targeting lapsed customers (Cluster 1)

## How to Run
1. Open `CustomerSegmentation.ipynb` in Google Colab
2. Upload `online_retail_II.csv` when prompted
3. Run all cells
