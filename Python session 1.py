#!/usr/bin/env python
# coding: utf-8

# In[1]:


# This is a comment
num = 100 


# In[2]:


print(num)


# In[3]:


num1 = 5.5 


# In[6]:


str1="My name is VJ"
str2="I love myself"


# In[8]:


print(str1)
print(str2)


# In[9]:


color_list =["red","green","yellow","blue","orange"]


# In[10]:


print(color_list)


# In[15]:


a=10
b=5


# In[20]:


if a>0 or b>10:
    print("all positive")


# In[32]:


a+=10


# In[40]:


print(a)


# In[42]:


if "purple" in color_list:
    print("purple is there")
else:
    print("purple not there")


# In[43]:


my_num1 = input("enter any number")


# In[45]:


print(my_num1)


# In[57]:


mynum1= int(input("enter first number"))
mynum2= int(input("enter second number"))


# In[55]:


def my_function(n1,n2):
    return(n1 * n2)


# In[51]:


my_function(mynum1,mynum2)


# In[58]:


my_function(mynum1,mynum2)


# In[59]:


my_function(5,4)


# In[72]:


str1 = "My, name is, vijayshree"


# In[65]:


str1.lower()


# In[67]:


str1.upper()


# In[66]:


str1.capitalize()


# In[73]:


str1.split(",")


# In[74]:


m1=" Hello "
m1.strip()


# In[77]:


str1 = "python "
str2 = "panda"
str1 + str2


# In[78]:


str1 *10


# In[82]:


str1[::-2]


# In[83]:


fruits =["apple","banana","mango","grapes"]


# In[84]:


fruits.append("cherry")


# In[85]:


fruits


# In[86]:


fruits.insert(2,"papaya")


# In[87]:


fruits


# In[88]:


fruits.len()


# In[89]:


len(fruits)


# In[90]:


fruits.insert(-1,"litchie")


# In[91]:


fruits


# In[92]:


fruits.sort()


# In[93]:


fruits


# In[94]:


fruits[0:4]


# In[95]:


fruits[::-1]


# In[96]:


fruits.head()


# In[97]:


fruits[:-4:-1]


# In[98]:


fruits.pop()


# In[99]:


fruits.pop(4)


# In[100]:


fruits


# In[101]:


fruits.pop()


# In[102]:


fruits


# In[103]:


fruits.extend("litchie")


# In[104]:


fruits


# In[105]:


fruits.append([1,2,3])


# In[106]:


fruits


# In[107]:


fruits.clear()


# In[108]:


fruits


# In[109]:


tuple =(3,4,6,7)


# In[110]:


tuple


# In[111]:


tuple[:2]


# In[112]:


tuple(:)


# In[113]:


tuple[:]


# In[119]:


tuple1 =(3,5,7,9,3,3,2,3)


# In[115]:


tuple1


# In[118]:


print(tuple1[0])


# In[120]:


tuple1.count(3)


# In[121]:


tuple1[1:2]


# In[122]:


sorted(tuple1)


# In[123]:


tuple1[1]


# In[124]:


tuple1


# In[125]:


tuple1[1]=9


# In[126]:


len(tuple1)


# In[127]:


tuple2 =(3,4,7)


# In[128]:


sum(tuple2)


# In[129]:


sum(tuple2,10)


# In[130]:


min(tuple2)


# In[131]:


max(tuple2)


# In[132]:


len(tuple2)


# In[133]:


dict1 ={1:'Python',
        2:'Java',
        3:'C++'}


# In[134]:


dict1


# In[135]:


dict1.keys()


# In[136]:


a = dict1.get(1)


# In[137]:


a


# In[ ]:




