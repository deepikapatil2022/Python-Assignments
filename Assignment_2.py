#!/usr/bin/env python
# coding: utf-8
1.What are the two values of the Boolean data type? How do you write them?
--->The two value of boolean data type are 
1. True 2. False

# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')

-->1.AND(&) 
2. OR (|)
3.NOT (!)

3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).
# In[ ]:


-->Truth table for Boolean operators are as follows:-
    1. AND-  T  F = F
             F  T = F
             F  F = F
             T  T = T
                
    2. OR    T  F = T
             F  T = T
             F  F = F
             T  T = T
    3. NOT   T->F
             F->T   


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)
not (5 > 4)

(True and True) and (True == False)-->False
(not False) or (not True)-->True


# In[2]:


(5 > 4) and (3 == 5)


# In[3]:


not (5 > 4)


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')
-->

1. ==     Equals to
2. >=     Greater than or equals to
3. <=     Less than or equals to
4. !=     Not equals to 
5. >      Greater than
6. <      Less than 

6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
# In[ ]:


--->
a==3 here eqaul to operator is checking that weather the value of a and 3 are equal or not.
Assignment operator is assigning a value to the operator e.g a=3 means the value of a is 3.


# In[10]:


#7. Identify the three blocks in this code:
spam = 0
if spam == 10:
    print('eggs')
    if spam > 5:
        print('bacon')
    else:
        print('ham')
    print('spam')
print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
# In[13]:


spam=1
if spam==1:
    print('Hello')
    if spam==2:
        print('Howdy')
else:print('Greetings')


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')
---> interrupt the kernel


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')
---> break will stop the execution of the programm. continue will pass the control to the main loop.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
---> No difference. The output is same.

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
# In[22]:


# Program to using for loop
for i in range(1,11):
    print(i)


# In[5]:


#program using while loop
i=1
while(i!=11):
    print(i)
    i+=1


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
-->
import spam
spam.bacon()


# In[17]:


for i in range(10):
    print(i)


# In[19]:


for i in range(0,10,1):
    print(i)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




