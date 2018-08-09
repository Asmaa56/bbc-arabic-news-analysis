
# coding: utf-8

# In[1]:


#import the needed python libraries
import numpy as np
import pandas as pd 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns 


# In[2]:


from youtube_search import youtube_search #call youtube_search fuction


# In[3]:


data = youtube_search('BBC News عربي')


# In[4]:


df = pd.read_csv('video_result.csv')
df.info()


# In[5]:


#from data information it appears that there is no missing data


# In[6]:


# explore data 
df.head()


# In[20]:


df.describe()


# In[7]:


pd.set_option('float_format', '{:f}'.format)
df['viewCount'].describe()


# In[10]:


df['videoId'][df['viewCount']==df['viewCount'].min()]


# In[12]:


#داخل الإطار: عمرو حسن


# In[11]:


df['videoId'][df['viewCount']==df['viewCount'].max()] 


# In[13]:


#فرانس 24 البث المباشر – الأخبار الدولية على مدار الساعة


# In[21]:


df['videoId'][df['likeCount']==df['likeCount'].max()]


# In[25]:


df['videoId'][df['dislikeCount']==df['dislikeCount'].max()]


# In[26]:


df['videoId'][df['commentCount']==df['commentCount'].max()]


# In[14]:


# plot and remove relative shift in matplotlib axis ount_veiw
import  matplotlib.ticker as mt
plt.figure()
ax = plt.gca()
fmt = mt.ScalarFormatter(useOffset=False)
fmt.set_scientific(False)
ax.xaxis.set_major_formatter(fmt)
hist_1,edges_1  = np.histogram(df['viewCount'])
plt.bar(edges_1[:-1], hist_1,width =edges_1[1:]-edges_1[:-1])
plt.show()


# In[28]:


plt.figure(figsize = (6,6))
ax = plt.gca()
fmt = mt.ScalarFormatter(useOffset=False)
fmt.set_scientific(False)
ax.xaxis.set_major_formatter(fmt)
sns.distplot(df['viewCount'],bins =50, hist_kws={'alpha': 0.4})


# In[29]:


plt.figure(figsize = (6,6))
sns.distplot(df['likeCount'],bins =50, hist_kws={'alpha': 0.4})


# In[30]:


plt.figure(figsize = (6,6))
sns.distplot(df['dislikeCount'],bins =50, hist_kws={'alpha': 0.4})


# In[31]:


plt.figure(figsize = (6,6))
sns.distplot(df['commentCount'],bins =50, hist_kws={'alpha': 0.4})


# In[33]:


# exploraing the correlation between variables
plt.figure(figsize = (7,7))
sns.heatmap(df.corr(), cmap="YlGnBu")


# In[14]:


df.corr()


# In[68]:


plt.figure(figsize = (7,6))
ax = plt.gca()
fmt = mt.ScalarFormatter(useOffset=False)
fmt.set_scientific(False)
ax.xaxis.set_major_formatter(fmt)
plt.scatter(df['viewCount'],df['likeCount'])


# In[16]:


import statsmodels.api as sm
x = df['viewCount']
y = df['likeCount']
x = sm.add_constant(x)


# In[17]:


lr_model = sm.OLS(y,x).fit()
lr_model.summary()

