
# coding: utf-8

# In[1]:



from sklearn.feature_extraction.text import CountVectorizer
2
#from sklearn.feature_extraction.text import TfidfVectorizer
vect=CountVectorizer(binary=True) #explore other parameters to
corpus=["Tesseract is good optical character recognition engine","optical character rcognition is different"]
vect.fit(corpus)
print(vect.transform(["Today is good optical"]).toarray())
#print(vect.transform(corpus).toarray())

