#!/usr/bin/env python
# coding: utf-8

# In[8]:


def savings_account(balance,years,interest=4):
    new_balance = balance*((1+(interest/100))**years)
    return new_balance

input_bal = int(input("Enter your current account balance : "))
input_yrs = int(input("How long are you keeping the money for?  : "))

print(f"After {input_yrs} years ,the account balance will be {savings_account(input_bal,input_yrs):.2f}")


# In[ ]:





# In[ ]:




