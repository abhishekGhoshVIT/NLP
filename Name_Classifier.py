#!/usr/bin/env python
# coding: utf-8

# In[2]:


import nltk


# In[3]:


nltk.download()


# In[5]:


import nltk
nltk.download()


# In[17]:


def gender_features(word):
    return {'last_letter':word[-1]}


# In[18]:


from nltk.corpus import names
labeled_names=([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])


# In[19]:


gender_features("sherlock")


# In[21]:


labelled_names=([(name,'male') for name in names.words('male.txt')]+[(name,'female') for name in names.words('female.txt')])


# In[22]:


len(names.words())


# In[23]:


labelled_names


# In[24]:


import random
random.shuffle(labeled_names)


# In[25]:


featuresets=[(gender_features(n),gender) for (n,gender) in labeled_names]


# In[28]:


featuresets


# In[29]:


train_set,test_test=featuresets[500:],featuresets[:500]


# In[30]:


train_set


# In[31]:


import nltk
classifier=nltk.NaiveBayesClassifier.train(train_set)


# In[32]:


classifier.classify(gender_features('David'))


# In[34]:


classifier.classify(gender_features('Michelle'))


# In[35]:


classifier.classify(gender_features('Obama'))


# In[37]:


nltk.classify.accuracy(classifier,test_test)


# In[38]:


print(classifier.prob_classify(gender_features('David')))


# In[ ]:





# In[ ]:




