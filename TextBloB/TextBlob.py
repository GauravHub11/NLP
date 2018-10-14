
# coding: utf-8

# In[ ]:


from textblob import TextBlob


# In[5]:


p=0
n=0
for i in range(1,5):
    text=input("Enter your Response about Python  ")
    obj=TextBlob(text)
    sentiment=obj.sentiment.polarity
    if sentiment>=0:
        p=p+1
    else:
        n=n+1
print("{} Positive Response".format(p))
print("{} Negative Response".format(n))
     
        
    

