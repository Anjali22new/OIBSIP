# Task 1 · EDA on Retail Sales Data

## Objective
Performed exploratory data analysis on the Superstore Sales dataset to uncover 
sales trends, customer patterns, and actionable business insights.

## Dataset
[Superstore Sales Dataset (Kaggle)](https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting) 
— 9,800 rows, 18 columns of order-level retail sales data (2015–2018).

## Tech Stack
Python, pandas, matplotlib, seaborn, Google Colab

## Approach
- Inspected data structure, handled missing Postal Code values, and fixed a 
  date-parsing issue (dates were in DD/MM/YYYY format, not the default MM/DD/YYYY)
- Analyzed monthly sales trends, category/sub-category performance, 
  customer segments, and regional sales
- Built a correlation heatmap and discussed its limitations given the dataset's 
  mostly categorical structure

## Key Insights
- Sales show strong year-over-year growth with clear seasonality — peaks every 
  November, dips every January
- Technology leads by category, but Phones and Chairs are the strongest 
  sub-categories overall — more reliable than single-product spikes like the 
  top-selling Canon copier
- Consumer segment drives ~2x more orders than Corporate
- West and East regions significantly outperform Central and South

## Business Recommendations
1. Plan inventory and marketing around the Nov–Dec peak and Jan slump
2. Invest in Phones and Chairs sub-categories for sustainable growth
3. Target Central and South regions for expansion

## How to Run
1. Open `EDA_RetailSales.ipynb` in Google Colab
2. Upload the Superstore dataset CSV when prompted
3. Run all cells
