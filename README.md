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
 ![](groceries_head.PNG)
 
3. I checked for null values
   ```
   groceries_data.isnull().sum().sort_values(ascending = False)
   ```
   There were no null values recorded
   ![](is_null.PNG)

4. I converted the data type of the Date column from object to date
   ```
   groceries_data['date'] = pd.to_datetime(groceries_data['Date'])
   groceries_data.info()
   ```
   ![](https://Market-Basket-Analysis-using-Apriori-Algorithm/blob/main/date_time.PNG)

5. I checked for the distribution of items
   ```
   item_Distribution = groceries_data.groupby(by = 
   'itemDescription').size().reset_index(name = 'Frequency').sort_values(by  
   = 'Frequency', ascending = False)
   ```
   ![](item_distribution.PNG)

6. I created a bar chart showing the yop ten sold items
   ```
   # Extracting data for the bar chart
   item_Distribution = groceries_data.groupby(by = 
   'itemDescription').size().reset_index(name = 'Frequency').sort_values(by  
   = 'Frequency', ascending = False).head(10)
   bars = item_Distribution['itemDescription']
   height = item_Distribution['Frequency']
   x_pos = np.arange(len(bars))

   # Plotting the bar chart
   plt.figure(figsize = (16,9))
   plt.bar(x_pos, height,color = (0.2, 0.3, 0.5, 0.5))

   # Adding title and labels
   plt.title('Top 10 sold items')
   plt.xlabel('item names')
   plt.ylabel('number of quantity sold')
   plt.xticks(x_pos, bars)
   
   # Display the chart
   plt.show()
   ```
![](top_sold_items.png)

   

   
   
   

   

