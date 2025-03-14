#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
df=pd.read_csv('netflix_data.csv')
ty=df[(df['type']=='Movie')]
movies_20=ty[(ty['release_year']>=1990) & (ty['release_year']<=1999)]
plt.hist(movies_20['duration'])
plt.xlabel('Duration')
plt.ylabel('Movies')
plt.title('Analyzing 90_s movies on Netflix ')
plt.show()
duration=100
short_action=movies_20[(movies_20['genre']=='Action')]
short_movie_count=0
for index,val in short_action.iterrows():
    if val['duration']<90:
        short_movie_count=short_movie_count+1
print(short_movie_count)

