#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello")


# In[5]:


i = 0
k = 0 
sum1 = 6 #input("Please enter number to get it sum upto ")
while i <= sum1:
    k = k + sum1
    sum1 = sum1 - 1

print("Sum of all numbers in", k)


# ## Prime 
# 

# In[19]:


flag = 0
i = 2
n = int(input("please enter positive number greater than 1 : "))
if n == 1 :
    print("1 is not a prime number")
else :
    for x in range(2, n):
        if n % x == 0:
            flag = 1;
            break;
            i = i+ 1
if flag == 0 :
    print(f"{n} is a prime number ")
else :
    print(f"{n} is not a prime number ")
    


# In[ ]:




