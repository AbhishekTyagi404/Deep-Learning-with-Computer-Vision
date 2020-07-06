#!/usr/bin/env python
# coding: utf-8

# #### **Welcome to Assignment 0 on Deep Learning for Computer Vision.**
# In this assignment you will get a chance to understand and work on some of the commonly used functionalities of several Machine Learnign and Data Analysis libraries
# 
# #### **Instructions**
# 1. Use Python 3.x to run this notebook
# 2. Write your code only in between the lines 'YOUR CODE STARTS HERE' and 'YOUR CODE ENDS HERE'.
# 3. Look up the documentation for each of the Python and Numpy function used.
# 4. This Assignment is just to make you understand several commonly used library functions.
# 5. This assignment is **NOT** evaluated

# In[1]:


# DO NOT CHANGE THIS CODE
import numpy as np
np.random.seed(0)


# #### Python Basics
# 

# In[4]:


### Implement recursive fibonacci in the function below
def recursive_fibonacci(n):
    if n<0:
        print("Incorrect Input")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)


# In[5]:


### Test your code using the function call below.
recursive_fibonacci(3)


# #### Lambda function

# In[33]:


def sigmoid(x):
  sigmoid = 1 / (1 + np.exp(-x))
  return sigmoid

## Implement the above sigmoid function using python lambda functions
## YOUR CODE STARTS HERE
sigmoid_lambda = lambda x : sigmoid(x)
## YOUR CODE ENDS HERE


# In[34]:


## Check you implementation by running this cell (should return True)
sigmoid(1) == sigmoid_lambda(1)


# #### List Comprehension

# In[35]:


div_by_four = []
for number in range(200):
    if number%4 == 0:
        div_by_four.append(number)
        
## Implement the above function using list comprehensions
## YOUR CODE STARTS HERE
div_by_four_lc = [div_by_four for number in range(200)]
## YOUR CODE ENDS HERE


# In[36]:


## Check you implementation by running this cell (should return True)
div_by_four == div_by_four_lc


# #### Python map keyword
# Using the lambda functions and python's map keyword apply sigmoid on a list of numbers from 0 to 99. Store the output in a list and print it. 
# 
# **Observe what happens to the value of sigmoid as the value of x increases. Do you see any trend?**

# In[46]:


## YOUR CODE STARTS HERE
out = map(sigmoid_lambda, div_by_four)
## YOUR CODE ENDS HERE
print(list(out))


# # Numpy Basics:
# 

# #### Creating a numpy array with particular value
# 

# In[41]:


# Create a numpy array with size 2*2 with all elements as 8.
# YOUR CODE STARTS HERE
arr = np.array([[2, 4, 6], [6, 8, 10]], np.int32)
# YOUR CODE ENDS HERE


# #### Basic Numpy operations:

# In[48]:


#Create a numpy array of size 3*3 with random values 
rand_arr = np.random.rand(3,3) 
print(rand_arr)
#YOUR CODE STARTS HERE
#YOUR CODE ENDS HERE


# In[61]:


#Find the sum of all the elements, mean, maximum and minimum value of the numpy array defined above

#YOUR CODE STARTS HERE
arr_sum = np.sum([rand_arr])
arr_mean = np.mean([rand_arr])
arr_max = np.max([rand_arr])
arr_min = np.min([rand_arr])
print("Sum =", arr_sum, "\n" , "Mean=", arr_mean, "\n" ,"Max=", arr_max, "\n" ,"Min=", arr_min)
#YOUR CODE ENDS HERE


# #### Reshaping and Indexing of Numpy Array:

# In[92]:


#create a 1D numpy array of shape 35 with values 1,2,3..,35

#YOUR CODE STARTS HERE
y = np.arange(35)
print(y)
#YOUR CODE ENDS HERE


# In[98]:


# Reshape it as 2D array of shape (5,7)

#YOUR CODE STARTS HERE
y = y.reshape(5,7)
#YOUR CODE ENDS HERE
print(y.shape)
print(y)


# In[96]:


# Extract all the elements from 2nd and 3rd row

#YOUR CODE STARTS HERE
y_row = y[2:4,:]
#YOUR CODE ENDS HERE
y_row


# In[108]:


# Extract all the elements from 3rd and 5th and 7th column

#YOUR CODE STARTS HERE
y_column = y[:,2:7:2]
#YOUR CODE ENDS HERE
print(y_column)


# #### Horizontal and vertical stacking of numpy array

# In[111]:


## horizontal and vertical stacking of 1D arrays 
a = np.array([4.,2.])
b = np.array([3.,8.])

#YOUR CODE STARTS HERE
# Horizontal stacking
h_stack = np.hstack((a,b))

# Vertical Stacking
v_stack = np.vstack((a,b))
#YOUR CODE ENDS HERE
print(h_stack)
print(v_stack)


# #### `argmin` and `argmax` in numpy array

# In[112]:


# Define an array
arr = np.array([[5,12,51,25] ,[25,29,2,27]])

# YOUR CODE STARTS HERE
#Find the position of maximum and minimum value of above array
max_idx = np.argmax(arr)
min_idx = np.argmax(arr)
print (max_idx,min_idx)

#Find the indices of maximum and minimum value along each of its columns.
max_col = np.argmax(arr,axis = 0)
min_col = np.argmin(arr,axis = 0)
print (max_col,min_col)

#Find the indices of maximum and minimum value along each of the its rows.
max_row = np.argmax(arr,axis = 1)
min_row = np.argmin(arr,axis = 1)
print (max_row,min_row)
#YOUR CODE ENDS HERE

