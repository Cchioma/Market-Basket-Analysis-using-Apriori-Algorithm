# Market Basket Analysis 
## Background
Market Basket Analysis (MBA), also known as association analysis or affinity analysis, is a data mining technique used in the field of retail and e-commerce to discover associations between products that are frequently purchased together. The analysis is based on the concept of a "market basket," which refers to a collection of items that a customer buys during a single shopping trip.
## About the Data
The dataset is a CSV file that contains one table, consisting of 38765 rows and 3 columns. The dataset can be found [here](Groceries_dataset.csv).
## Business Problems
1. Analyze the distribution of purchases over different dates or time periods.
2. Identify the most frequently purchased item descriptions.
3. Determine which items are commonly bought together (association analysis).

## Skills/ Concepts Applied
1. Data Preparation
2. Exploratory Data Analysis (EDA)
3. Market Basket Analysis
4. Visualization
5. Interpretation and Insights

## Data Transformation / Cleaning
1. I installed the pandas and MLXtend libraries into jupyter notebook.
```
pip install mlxtend 
pip install apyori
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori, association_rules
```

2. I loaded the dataset and viewed the first 5 rows.

   ```
   groceries_data = pd.read_csv('groceries_dataset.csv')
   groceries_data.head()
   ```

