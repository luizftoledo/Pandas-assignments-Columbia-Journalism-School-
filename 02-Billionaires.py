#!/usr/bin/env python
# coding: utf-8

# # Homework 5, Part 2: Answer questions with pandas
# 
# **Use the Excel file to answer the following questions.** This is a little more typical of what your data exploration will look like with pandas.

# ## 0) Setup
# 
# Import pandas **with the correct name** .

# In[2]:


import pandas as pd


# ## 1) Reading in an Excel file
# 
# Use pandas to read in the `richpeople.xlsx` Excel file, saving it as a variable with the name we'll always use for a dataframe.
# 
# > **TIP:** You will use `read_excel` instead of `read_csv`. Trying `read_excel` the first time will probably not work, you'll get an error message. Be sure to read the error carefully: *you probably need to install a new library before it will work, and the error tells you what the library is named*.

# In[3]:


df = pd.read_excel('richpeople.xlsx')


# ## 2) Checking your data
# 
# Display the number of rows and columns in your data. Also display the names and data types of each column.

# In[4]:


df.shape


# In[ ]:





# In[ ]:





# ## 3) Who are the top 10 richest billionaires? Use the `networthusbillion` column.

# In[5]:


df.sort_values(by='networthusbillion', ascending=False).head(10)


# ## 4) How many male billionaires are there compared to the number of female billionares? What percent is that? Do they have a different average wealth?
# 
# > **TIP:** The last part uses `groupby`, but the count/percent part does not.
# > **TIP:** When I say "average," you can pick what kind of average you use.

# In[6]:


# a dataframe with the total of men and women in the billionaires list
gen_count_df = df.gender.value_counts().rename_axis('gender').reset_index(name='total')


total_billionaires = len(df)
total_men = gen_count_df.total[0]
total_women = gen_count_df.total[1]
men_share = round(total_men / total_billionaires * 100, 1)
women_share = round(total_women / total_billionaires * 100, 1)

#print

print(f'There are {total_men} men and {total_women} women in the list. Men account for {men_share}% of the total, while women account for {women_share}%')

#define averages divided by gender

print('------')
print('NETWORTH IN US DOLLARS BY GENDER')
df.groupby('gender').networthusbillion.mean()



# In[ ]:





# In[ ]:





# ## 5) What is the most common source/type of wealth? Is it different between males and females?
# 
# > **TIP:** You know how to `groupby` and you know how to count how many times a value is in a column. Can you put them together???
# > **TIP:** Use percentages for this, it makes it a lot more readable.

# In[44]:


#Most common source or type of wealth

df.typeofwealth.value_counts().head(1)




# In[8]:


#Most common source or type of wealth BY GENDER

df.groupby('gender').typeofwealth.value_counts()


# ## 6) What companies have the most billionaires? Graph the top 5 as a horizontal bar graph.
# 
# > **TIP:** First find the answer to the question, then just try to throw `.plot()` on the end
# >
# > **TIP:** You can use `.head()` on *anything*, not just your basic `df`
# >
# > **TIP:** You might feel like you should use `groupby`, but don't! There's an easier way to count.
# >
# > **TIP:** Make the largest bar be at the top of the graph
# >
# > **TIP:** If your chart seems... weird, think about where in the process you're sorting vs using `head`

# In[52]:


#listofcompanies
companies_most = df.company.value_counts().head(5).sort_values().rename_axis('company_name').reset_index(name='total')


#plot

companies = companies_most['company_name']
billionaires = companies_most['total']

plt.barh(companies, billionaires)
plt.title('Companies with the most billionaires')
plt.ylabel('company_most')
plt.xlabel('total')
plt.show()




# the_richest = df.sort_values(by='networthusbillion', ascending=False).head(10)

# #plot

# name = the_richest['name']
# amount = the_richest['networthusbillion']

# plt.barh(name, amount)
# plt.title('Richest people')
# plt.ylabel('name')
# plt.xlabel('amount')
# plt.show()

    


# ## 7) How much money do these billionaires have in total?

# In[10]:


money = round(df.networthusbillion.sum(),1)
print(f'{money} billions in US dollars')


# ## 8) What are the top 10 countries with the most money held by billionaires?
# 
# I am **not** asking which country has the most billionaires - this is **total amount of money per country.**
# 
# > **TIP:** Think about it in steps - "I want them organized by country," "I want their net worth," "I want to add it all up," and "I want 10 of them." Just chain it all together.

# In[11]:


billionaire_per_country = df.groupby('countrycode').networthusbillion.sum().rename_axis('country').reset_index(name='total')

billionaire_per_country.sort_values(by='total', ascending=False).head(10)


# ## 9) How old is an average billionaire? How old are self-made billionaires  vs. non self-made billionaires? 

# In[12]:


round(df.age.mean(),1)


# In[13]:


df.groupby('selfmade').age.mean()


# ## 10) Who are the youngest billionaires? Who are the oldest? Make a graph of the distribution of ages.
# 
# > **TIP:** You use `.plot()` to graph values in a column independently, but `.hist()` to draw a [histogram](https://www.mathsisfun.com/data/histograms.html) of the distribution of their values

# In[14]:


#top 5 youngest

df.sort_values(by='age').head(5)


# In[15]:


#top 5 oldest

df.sort_values(by='age', ascending=False).head(5)


# In[16]:


#age histogram

df.age.hist()


# ## 11) Make a scatterplot of net worth compared to age

# In[17]:


#networthusbillion
age_money = df.groupby(by='age').networthusbillion.sum().rename_axis('age').reset_index(name='billions')


import matplotlib.pyplot as plt
import numpy as np

x = np.array(age_money.age)
y = np.array(age_money.billions)

plt.scatter(x, y)
plt.show()


# ## 13) Make a bar graph of the wealth of the top 10 richest billionaires
# 
# > **TIP:** When you make your plot, you'll need to set the `x` and `y` or else your chart will look _crazy_
# >
# > **TIP:** x and y might be the opposite of what you expect them to be

# In[63]:


the_richest = df.sort_values(by='networthusbillion', ascending=False).head(10)

#plot

name = the_richest['name']
amount = the_richest['networthusbillion']

plt.barh(name, amount)
plt.title('Richest people')
plt.ylabel('name')
plt.xlabel('amount')
plt.show()

    


# In[ ]:




