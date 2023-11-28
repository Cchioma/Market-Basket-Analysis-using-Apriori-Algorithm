#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install mlxtend 


# In[2]:


pip install apyori


# In[3]:


#Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori, association_rules


# In[4]:


#Loading the dataset
groceries_data = pd.read_csv('groceries_dataset.csv')


# In[5]:


#Reading the dataset
groceries_data.head()


# In[6]:


#checking for data type
groceries_data.info()


# In[7]:


#checking for null values
groceries_data.isnull().sum().sort_values(ascending = False)


# In[8]:



#converting Date column from object to date type
groceries_data['date'] = pd.to_datetime(groceries_data['Date'])
groceries_data.info()


# In[9]:


#checking dataset for changes
groceries_data.head()


# In[10]:


#checking distribution of items
item_Distribution = groceries_data.groupby(by = 'itemDescription').size().reset_index(name = 'Frequency').sort_values(by  = 'Frequency', ascending = False)


# In[11]:


item_Distribution.head(10)


# In[12]:


#creating a bar chart showing the top ten sold items
item_Distribution = groceries_data.groupby(by = 'itemDescription').size().reset_index(name = 'Frequency').sort_values(by  = 'Frequency', ascending = False).head(10)


bars = item_Distribution['itemDescription']
height = item_Distribution['Frequency']
x_pos = np.arange(len(bars))

plt.figure(figsize = (16,9))

plt.bar(x_pos, height,color = (0.2, 0.3, 0.5, 0.5))

plt.title('Top 10 sold items')
plt.xlabel('item names')
plt.ylabel('number of quantity sold')

plt.xticks(x_pos, bars)

plt.show()


# In[13]:



# Assuming 'groceries_data' is your DataFrame with 'Date' column
# Ensure 'Date' is in datetime format
groceries_data['Date'] = pd.to_datetime(groceries_data['Date'])

# Create new columns for Month and Year
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
groceries_data['Month'] = pd.Categorical(groceries_data['Date'].dt.strftime('%B'), categories=months_order, ordered=True)
groceries_data['Year'] = groceries_data['Date'].dt.year

# Group by Year and Month, and count the number of purchases
purchase_distribution = groceries_data.groupby(['Year', 'Month']).size().reset_index(name='Number_of_Purchases')

# Create a line chart with a separate line for each year
plt.figure(figsize=(12, 6))

for year in purchase_distribution['Year'].unique():
    year_data = purchase_distribution[purchase_distribution['Year'] == year]
    plt.plot(year_data['Month'], year_data['Number_of_Purchases'], label=str(year), marker='o', linestyle='-')

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Number of Purchases')
plt.title('Distribution of Purchases Over Different Months')
plt.legend(title='Year', loc='upper right')

# Show the plot
plt.show()


# In[14]:


#Select 'Member_number' and 'itemDescription' columns from the DataFrame and sort by 'Member_number' column in descending order.
cust_level = groceries_data[['Member_number', 'itemDescription']].sort_values(by = 'Member_number', ascending =False)

#Srip leading and trailing whitespaces from the 'itemDescription' column and display the result
cust_level['itemDescription'] = cust_level['itemDescription'].str.strip()
cust_level


# In[15]:


transactions = [a[1]['itemDescription'].tolist() for a in list(cust_level.groupby(['Member_number']))]


# In[16]:


from apyori import apriori
rules = apriori(transactions = transactions, min_support =0.002, min_confidence = 0.05,min_lift = 3, min_length = 2)


# In[17]:


results  = list(rules)


# In[18]:


results


# In[19]:


def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs,supports,confidences, lifts))
resultsindataframe = pd.DataFrame(inspect(results),columns = ['Left hand side', 'Right hand side', 'Supports', 'Confidences', 'Lift'])


# In[20]:


resultsindataframe['Lift'] = pd.to_numeric(resultsindataframe['Lift'])


# In[24]:


resultsindataframe.nlargest(n = 10, columns  = 'Lift')


# In[ ]:




