#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?
# ==>No, the Python Standard Library is separate from PyInputPlus. The Python Standard Library is a collection of modules and packages that are included with Python by default. These modules cover a wide range of tasks, such as working with files, networking, data manipulation, and more.
# 
# On the other hand, PyInputPlus is not a part of the Python Standard Library. It is a third-party library developed by Al Sweigart. PyInputPlus provides additional functionality for taking user input in a more controlled and user-friendly manner compared to the built-in input() function.
# 
# To use PyInputPlus, you need to install it separately. You can do this using the Python package manager, pip:
# 
# pip install PyInputPlus
# 

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
# 
# ==> cPyInputPlus is commonly imported with the alias pypi to make it easier and more convenient to use in your code. This alias is just a convention and can be any valid Python identifier.
# 
# By importing PyInputPlus as pypi, you can type shorter and more readable code when calling functions or using features from the library. For example:
#  
# import pyinputplus as pypi
# 
# response = pypi.inputChoice(['yes', 'no'], prompt='Enter yes or no: ')
# Using pypi as an alias provides a shorter prefix for the library's functions, making your code more concise and easier to read. It also helps prevent potential conflicts with other modules or functions with similar names. This practice is especially useful when you're working with libraries that have long or commonly used names.

# 3. How do you distinguish between inputInt() and inputFloat()?
# ==>
# inputInt() and inputFloat() are both functions provided by the PyInputPlus library for handling user input. They differ in the type of input they expect and the type of value they return:
# 
# inputInt(prompt=None, default=None, limit=None):
# 
# This function is used to get an integer input from the user.
# It will keep prompting the user until a valid integer is provided.
# If a default value is specified and the user presses Enter without entering anything, the default value will be returned.
# If a limit is provided, the input will be validated to ensure it falls within the specified range.
# Example:

# In[6]:


import pyinputplus as pypi

age = pypi.inputInt(prompt='Enter your age: ', min=0, max=120)


# In[ ]:


inputFloat(prompt=None, default=None, limit=None):

This function is used to get a floating-point number input from the user.
It will keep prompting the user until a valid float is provided.
If a default value is specified and the user presses Enter without entering anything, the default value will be returned.
If a limit is provided, the input will be validated to ensure it falls within the specified range.
Example:


# In[ ]:


import pyinputplus as pypi

height = pypi.inputFloat(prompt='Enter your height (in meters): ', min=0.1, max=2.5)


# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
# ==>
# You can use the inputInt() function from PyInputPlus with the min and max arguments to ensure that the user enters a whole number between 0 and 99. Here's an example:
# 
# 
# import pyinputplus as pypi
# 
# number = pypi.inputInt(prompt='Enter a whole number between 0 and 99: ', min=0, max=99)
# 
# In this example, inputInt() prompts the user to enter a whole number. The min argument is set to 0 and the max argument is set to 99, which enforces the range of valid inputs. The function will keep prompting the user until a valid input within the specified range is provided.
# 
# If the user enters a number outside of the specified range, PyInputPlus will display an error message and prompt the user again. If a non-integer value is provided, PyInputPlus will also display an error message and continue prompting until a valid integer is entered.

# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
# ==>In PyInputPlus, the keyword arguments allowRegexes and blockRegexes are used to specify regular expressions that define patterns of allowed or blocked input.
# 
# Here's what each argument does:
# 
# allowRegexes:
# 
# This argument allows you to specify a list of regular expressions. If the user's input matches any of the regular expressions in allowRegexes, it will be considered valid.
# If allowRegexes is provided, only inputs that match one of the specified regular expressions will be accepted.
# Example:
# 
# python
# Copy code
# import pyinputplus as pypi
# 
# number = pypi.inputNum(prompt='Enter a number (even or multiple of 5): ', allowRegexes=[r'^[02468]$', r'^[05]$'])
# In this example, the user will only be allowed to enter even numbers or multiples of 5.
# 
# blockRegexes:
# 
# This argument allows you to specify a list of regular expressions. If the user's input matches any of the regular expressions in blockRegexes, it will be considered invalid.
# If blockRegexes is provided, any input that matches one of the specified regular expressions will be rejected.
# Example:
# 
# import pyinputplus as pypi
# 
# number = pypi.inputNum(prompt='Enter a number (not divisible by 3): ', blockRegexes=[r'^\d*[13579]$', r'^[3]$'])
# In this example, the user will not be allowed to enter numbers that are divisible by 3.
# 
# Both allowRegexes and blockRegexes accept lists of regular expressions. They provide a powerful way to customize and control the type of input that is accepted by PyInputPlus. Keep in mind that these regular expressions should be in string format (hence the r prefix) and follow Python's regular expression syntax.

# In[ ]:





# In[ ]:


get_ipython().set_next_input('6. If a blank input is entered three times, what does inputStr(limit=3) do');get_ipython().run_line_magic('pinfo', 'do')
==>If a blank input is entered three times while using inputStr(limit=3), PyInputPlus will raise a ValidationException.

Here's an example:


# In[ ]:


import pyinputplus as pypi

try:
    user_input = pypi.inputStr(prompt='Enter something: ', limit=3)
    print(f'You entered: {user_input}')
except pypi.exceptions.ValidationException as ve:
    print(f'ValidationException: {ve}')


# 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
# ==>If blank input is entered three times while using inputStr(limit=3, default='hello'), PyInputPlus will return the default value 'hello'.
# 
# Here's an example:

# In[7]:


import pyinputplus as pypi

user_input = pypi.inputStr(prompt='Enter something: ', limit=3, default='hello')
print(f'You entered: {user_input}')


# In[ ]:




