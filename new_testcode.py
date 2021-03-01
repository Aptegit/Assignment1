#!/usr/bin/env python
# coding: utf-8

# In[1]:


obill =float(input('How much is your original bill?  ')) #input string


# In[2]:


print(type(obill))  #to check the data type of variable


# In[3]:


tip = int(input('What percentage is your tip?')) #input string


# In[4]:


print(type(tip))   #to check the data type of variable


# In[5]:


f1 = obill*tip                           #calculating percentage using standard percentage formula
ftip= float("{:.2f}".format(f1/100))
print (ftip)
print('Your tip based on ' + str(tip) + ' % is ' + str(ftip) + ' $ . ')


# In[6]:


fbill = obill + ftip         #adding tip percent value to the original bill
#print(type(obill))
#print(type(ftip))
print('Your total bill is : ' + str(fbill) + ' $ . ')

