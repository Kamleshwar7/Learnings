#!/usr/bin/env python
# coding: utf-8

# In[1]:


# 1 mile per gallon is equal to 235.214583 liters per 100 km.
def mpg_to_lp100km(mpg):
    lp100km = 235.214583 / mpg
    return lp100km

mpg_value = float(input("Enter the value:"))
print(f"{mpg_value} miles per gallon is {mpg_to_lp100km(mpg_value):.2f} litres per 100 km")


# In[ ]:




