
# coding: utf-8

# In[2]:


import nltk


# In[3]:


from nltk.stem import PorterStemmer


# In[4]:


from nltk.stem import LancasterStemmer


# In[5]:


porter=PorterStemmer()


# In[6]:


lancaster=LancasterStemmer()


# In[7]:


print("PorterStemmer")


# In[8]:


print(porter.stem("cats"))


# In[9]:


print(porter.stem("trouble"))
print(porter.stem("troubling"))
print(porter.stem("troubled"))


# In[10]:


print("LancasterStemmer")
print(lancaster.stem("trouble"))
print(lancaster.stem("troubling"))
print(lancaster.stem("troubled"))


# In[11]:


print(lancaster.stem("apple"))


# In[12]:


print(lancaster.stem("happiness"))


# In[29]:


print(lancaster.stem("dying"))


# In[14]:


print(lancaster.stem("manger"))


# In[15]:


print(porter.stem("Dying"))
print(porter.stem("dying"))


# In[16]:


print(lancaster.stem("unorganized"))


# In[17]:


print(porter.stem("unorganized"))


# In[18]:


from nltk.stem import SnowballStemmer


# In[19]:


print(porter.stem("brownie"))


# In[20]:


print(lancaster.stem("brownie"))


# In[21]:


print(lancaster.stem("colleague"))


# In[22]:


print(porter.stem("colleague"))


# In[23]:


print(lancaster.stem("Colleague"))


# In[24]:


print(porter.stem("Colleague"))


# In[25]:


print(porter.stem('employment'))


# In[26]:


print(lancaster.stem('employment'))


# In[27]:


print(lancaster.stem("crying"))


# In[28]:


print(porter.stem("crying"))

