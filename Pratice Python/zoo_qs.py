#!/usr/bin/env python
# coding: utf-8

# In[9]:


print("Provide the ages of the members in a group. Press enter once you reached the end of the list")
price = 0
member_list = []

while True:
    input_age = input("Enter the age:")
    if input_age == '':
        break
    member_list.append(input_age)

print("All members in the group have the following ages: ", member_list)

for age in member_list:
    if int(age) <= 2:
        price += 0
    elif int(age) >= 3 and int(age) <= 12:
        price += 14
    elif int(age) >= 65:
        price += 18
    else:
        price += 23

print(f"The total ticket price is: ${price:.2f}")


# In[ ]:




