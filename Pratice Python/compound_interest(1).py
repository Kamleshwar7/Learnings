#!/usr/bin/env python
# coding: utf-8

# In[14]:


def savings_account(balance,years,interest=4):
    new_balance = balance*((1+(interest/100))**years)
    return new_balance

input_bal = int(input("Enter your current account balance : "))

for years in range(1,4):
    print(f"After {years} years, the account balance will be {savings_account(input_bal,years):.2f}")


# In[ ]:





# In[ ]:




