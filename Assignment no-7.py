#!/usr/bin/env python
# coding: utf-8

# 1. What is the name of the feature responsible for generating Regex objects?
# ==>The feature responsible for generating regular expression (regex) objects in Python is the re module. This module provides a powerful set of tools for working with regular expressions in Python. The re module allows you to create, manipulate, and apply regular expressions to strings, enabling tasks like pattern matching, search, and substitution.

# 2. Why do raw strings often appear in Regex objects?
# ==>Raw strings (strings prefixed with r or R) are often used in regular expressions (regex) because they prevent backslashes from being treated as escape characters. In regex patterns, backslashes are commonly used to introduce special metacharacters that have special meanings.
# 
# For example, consider the regex pattern \d which matches any digit. In a regular string, you would need to escape the backslash, like this: '\\d'. However, in a raw string, you can write it as r'\d', which is more readable and less error-prone.
# 
# Here's an example to illustrate the difference:

# In[1]:


import re

# Using a regular string
pattern1 = '\\d'

# Using a raw string
pattern2 = r'\d'

text = '123'

result1 = re.search(pattern1, text)
result2 = re.search(pattern2, text)

print(result1)  # Output: <re.Match object; span=(0, 1), match='1'>
print(result2)  # Output: <re.Match object; span=(0, 1), match='1'>


# 3. What is the return value of the search() method?
# ==>The search() method in Python's re module returns a special match object if a match is found, and None if no match is found.
# 
# If a match is found, you can use methods like .group() or attributes like .start() and .end() on the match object to retrieve information about the matched portion of the string.
# 
# Here's an example:
# 

# In[2]:


import re

pattern = r'\d+'
text = 'Hello 123 World'

match = re.search(pattern, text)

if match:
    print(f'Match found: {match.group()}')
else:
    print('No match found')


# 4. From a Match item, how do you get the actual strings that match the pattern?
# ==>To get the actual strings that match the pattern from a Match object, you can use the .group() method. This method returns the portion of the string that matches the pattern.
# 
# If you pass 0 as an argument to group(), it will return the entire matched substring. You can also pass an integer argument to get specific captured groups if your pattern contains parentheses for grouping.
# 
# Here's an example:
# 

# In[3]:


import re

pattern = r'(\d+)-(\d+)'
text = 'Match: 123-456'

match = re.search(pattern, text)

if match:
    whole_match = match.group(0)  # Returns the entire matched substring
    first_group = match.group(1)  # Returns the first captured group
    second_group = match.group(2)  # Returns the second captured group

    print(f'Whole match: {whole_match}')
    print(f'First group: {first_group}')
    print(f'Second group: {second_group}')
else:
    print('No match found')


# 5. In the regex which created from the r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group zero cover? Group 2? Group 1?
# ==>Group 0:
# 
# Group 0 (also known as the whole match) covers the entire matched substring. In this case, it includes the full phone number pattern, which is three digits, a hyphen, three digits, another hyphen, and four digits.
# It represents the entire matched pattern.
# 
# Group 1:
# 
# Group 1 corresponds to the first set of parentheses (\d\d\d) in the regular expression. This group captures three consecutive digits.
# In a phone number, it represents the area code.
# 
# Group 2:
# Group 2 corresponds to the second set of parentheses (\d\d\d-\d\d\d\d) in the regular expression. This group captures three digits, a hyphen, and four digits.
# In a phone number, it represents the local part of the number (excluding the area code).
# Here's an example of how to extract these groups using re.search():
# 

# In[4]:


import re

pattern = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'
text = 'Phone number: 123-456-7890'

match = re.search(pattern, text)

if match:
    group_0 = match.group(0)  # Entire matched substring
    group_1 = match.group(1)  # Area code
    group_2 = match.group(2)  # Local part of the number

    print(f'Group 0 (Entire match): {group_0}')
    print(f'Group 1 (Area code): {group_1}')
    print(f'Group 2 (Local part): {group_2}')
else:
    print('No match found')


# 6. In standard expression syntax, parentheses and intervals have distinct meanings. How can you tell a regex that you want it to fit real parentheses and periods?
# ==>
# In regular expression syntax, parentheses ( and ) are used for grouping and creating capturing groups, while periods . have a special meaning and match any character (except for a newline).
# 
# If you want to match literal parentheses or periods, you need to escape them using a backslash \.
# 
# To match a literal parenthesis, use \( to match an opening parenthesis and \) to match a closing parenthesis.
# 
# To match a literal period, use \..
# 
# Here's an example:

# In[5]:


import re

pattern = r'\(123\)\.456'
text = '(123).456'

match = re.search(pattern, text)

if match:
    print('Match found')
else:
    print('No match found')


# 7. The findall() method returns a string list or a list of string tuples. What causes it to return one of the two options?
# ==>The findall() method in Python's re module returns a list of strings when there are no capturing groups in the regular expression pattern. It returns a list of tuples of strings when there are one or more capturing groups in the pattern.
# 
# Here's the distinction:
# 
# No Capturing Groups:
# 
# When the regular expression pattern used in findall() does not contain any capturing groups (parentheses ()), it will return a list of strings. This means that it's looking for a specific pattern, but not capturing any specific parts of it.
# Example:
# 

# In[7]:


import re

pattern = r'(\d+)-(\d+)'
text = 'Phone numbers: 123-456 789-012'

matches = re.findall(pattern, text)
print(matches)  # Output: [('123', '456'), ('789', '012')]


# In[ ]:


get_ipython().set_next_input('8. In standard expressions, what does the | character mean');get_ipython().run_line_magic('pinfo', 'mean')
==>
In regular expressions, the vertical bar | is used as a logical OR operator. It allows you to specify multiple alternative patterns to match.

For example, if you have two patterns A and B, you can use A | B to indicate that you want to match either A or B.

Here's an example:


# In[8]:


import re

pattern = r'dog|cat'
text = 'I have a cat and a dog.'

matches = re.findall(pattern, text)
print(matches)  # Output: ['cat', 'dog']


# 9. In regular expressions, what does the character stand for?
# ==>Regular expressions use various metacharacters, each with its own special meaning. Here are some common metacharacters and their meanings in regular expressions:
# 
# . (Dot):
# 
# Matches any character except a newline.
# ^ (Caret):
# 
# Anchors the regex at the start of a line.
# $ (Dollar):
# 
# Anchors the regex at the end of a line.
# * (Asterisk):
# 
# Matches 0 or more occurrences of the preceding character or group.
# + (Plus):
# 
# Matches 1 or more occurrences of the preceding character or group.
# ? (Question Mark):
# 
# Matches 0 or 1 occurrence of the preceding character or group.
# \ (Backslash):
# 
# Escapes a metacharacter, allowing you to match it literally.
# [] (Square Brackets):
# 
# Matches any single character within the brackets.
# | (Vertical Bar):
# 
# Acts as a logical OR operator, allowing you to specify alternatives.
# () (Parentheses):
# 
# Groups together expressions, allowing you to apply quantifiers or alternatives to a group of characters.
# {} (Curly Braces):
# 
# Specifies a specific number of occurrences of the preceding character or group.
# () (Parentheses) with ?:
# 
# Makes the group non-capturing.
# \d, \w, \s:
# 
# Shorthand character classes for digit, word character, and whitespace character, respectively.
# \D, \W, \S:
# 
# Negated shorthand character classes (opposite of \d, \w, \s).
# 

# In[ ]:


get_ipython().set_next_input('10.In regular expressions, what is the difference between the + and * characters');get_ipython().run_line_magic('pinfo', 'characters')
==>
Anchors the regex at the end of a line.
* (Asterisk):

Matches 0 or more occurrences of the preceding character or group.
+ (Plus):


# 11. What is the difference between {4} and {4,5} in regular expression?
# ==>In regular expressions, {4} and {4,5} are both quantifiers that specify the exact number of occurrences of the preceding character or group.
# 
# Here's the difference between them:
# 
# {4}:
# 
# Matches exactly 4 occurrences of the preceding character or group.
# Example:
# 
# Pattern: \d{4}
# Matches: "1234", "5678", but not "12" (because it doesn't have exactly 4 digits).
# {4,5}:
# 
# Matches between 4 and 5 occurrences of the preceding character or group. It's a range.
# Example:
# 
# Pattern: \d{4,5}
# Matches: "1234", "56789", but not "123" (because it doesn't have between 4 and 5 digits) and not "12345" (because it has more than 5 digits).
# So, {4} specifies an exact count, while {4,5} specifies a range of counts.

# 12. What do you mean by the \d, \w, and \s shorthand character classes signify in regular expressions?
# ==>In regular expressions, the \d, \w, and \s are shorthand character classes that represent certain common types of characters:
# 
# \d:
# 
# \d matches any digit (0-9).
# It is equivalent to the character class [0-9].
# Example:
# 
# Pattern: \d
# Matches: "1", "9", "0", but not "A" (because it's not a digit).
# \w:
# 
# \w matches any word character.
# A word character is defined as a character that can be used in a word. It includes alphanumeric characters (letters and digits) and underscores (_).
# Example:
# 
# Pattern: \w
# Matches: "a", "Z", "5", "_", but not " " (space).
# \s:
# 
# \s matches any whitespace character.
# Whitespace characters include spaces, tabs, and newline characters.
# Example:
# 
# Pattern: \s
# Matches: " ", "\t" (tab), "\n" (newline), but not "A" (because it's not whitespace).
# These shorthand character classes are convenient ways to match specific types of characters commonly used in various patterns. They can be particularly useful when you want to create regular expressions for tasks like extracting digits, matching words, or identifying whitespace.

# 13. What do means by \D, \W, and \S shorthand character classes signify in regular expressions?
# ==>In regular expressions, the \D, \W, and \S are negated or inverse shorthand character classes. They represent characters that are not of a certain type:
# 
# \D:
# 
# \D matches any non-digit character.
# It is equivalent to the character class [^0-9].
# Example:
# 
# Pattern: \D
# Matches: "A", " ", "&", but not "5" (because it's a digit).
# \W:
# 
# \W matches any non-word character.
# It matches any character that is not a word character (i.e., not a letter, digit, or underscore).
# Example:
# 
# Pattern: \W
# Matches: "#", "$", "*", but not "A" (because it's a word character).
# \S:
# 
# \S matches any non-whitespace character.
# It matches any character that is not whitespace (i.e., not a space, tab, or newline).
# Example:
# 
# Pattern: \S
# Matches: "A", "5", "&", but not " " (because it's whitespace).
# These negated shorthand character classes are useful when you want to match characters that are not of a certain type. For example, \D can be used to match non-digit characters, and \W can be used to match non-word characters. This can be especially helpful when you want to exclude specific types of characters from a pattern.
# 

# 14. What is the difference between .*? and .*?==>
# ==>
# In regular expressions, .*? and .* are both quantifiers used to match zero or more occurrences of any character (except for a newline). However, they differ in their behavior:
# 
# .*? (Lazy Match):
# 
# .*? is a non-greedy quantifier, meaning it matches as few characters as possible to satisfy the pattern.
# It will try to match the smallest possible substring that still allows the overall pattern to match.
# Example:
# 
# Pattern: a.*?b
# Matches: "ab", "axb" in the string "axbybz".
# .* (Greedy Match):
# 
# .* is a greedy quantifier, meaning it matches as many characters as possible to satisfy the pattern.
# It will try to match the largest possible substring.
# Example:
# 
# Pattern: a.*b
# Matches: "axbyb" in the string "axbybz".

# 15. What is the syntax for matching both numbers and lowercase letters with a character class?
# ==>To match both numbers and lowercase letters with a character class in a regular expression, you can use the following syntax:
# 
# 
# [0-9a-z]
# This character class [0-9a-z] will match any single character that is a digit (0-9) or a lowercase letter (a-z).
# 
# Here's an example pattern that uses this character class:
# 
# import re
# 
# pattern = r'[0-9a-z]+'
# text = 'abc123DEF456'
# 
# matches = re.findall(pattern, text)
# print(matches)  # Output: ['abc123', '456']

# 16. What is the procedure for making a normal expression in regax case insensitive?
# ==>To make a regular expression case-insensitive in Python, you can use the re.IGNORECASE or re.I flag. This flag allows the regex pattern to match characters regardless of their case.
# 
# Here's how you can use it:
# 
# import re
# 
# pattern = r'apple'
# text = 'I have an Apple and an APPLE'
# 
# matches = re.findall(pattern, text, re.IGNORECASE)
# print(matches)  # Output: ['Apple', 'APPLE']

# 17. What does the . character normally match? What does it match if re.DOTALL is passed as 2nd argument in re.compile()?
# ==>The . (dot) character in a regular expression normally matches any character except for a newline (\n).
# 
# However, if you pass re.DOTALL (or re.S) as the second argument in re.compile(), it changes the behavior of the dot. In this mode, the dot will match any character, including a newline.
# 
# Here's an example to illustrate this:

# In[9]:


import re

pattern = r'.+'
text = 'Line 1\nLine 2'

# Without re.DOTALL
matches_without_dotall = re.findall(pattern, text)
print(matches_without_dotall)
# Output: ['Line 1', 'Line 2']

# With re.DOTALL
pattern_with_dotall = re.compile(pattern, re.DOTALL)
matches_with_dotall = pattern_with_dotall.findall(text)
print(matches_with_dotall)
# Output: ['Line 1\nLine 2']


# 18. If numReg = re.compile(r'\d+'), what will numRegex.sub('X', '11 drummers, 10 pipers, five rings, 4 hen') return?
# ==>
# 'X drummers, X pipers, five rings, X hen'

# In[11]:


numReg = re.compile(r'\d+')
numReg.sub('X', '11 drummers, 10 pipers, five rings, 4 hen')


# 19. What does passing re.VERBOSE as the 2nd argument to re.compile() allow to do?
# ==>Passing re.VERBOSE as the second argument to re.compile() in Python allows you to write regular expressions in a more human-readable and organized manner. It enables "verbose mode" for the regular expression pattern.
# 
# In verbose mode, you can add comments and whitespace to your regular expression pattern to make it more understandable. This is especially useful for complex patterns that might be difficult to read at a glance.
# 
# For example, consider a regular expression pattern like this:
# 
# 
# pattern = r'\d{3}-\d{2}-\d{4}'
# In verbose mode, you can rewrite it like this:
# 
# 
# pattern = r'''
#     \d{3}   # Match three digits
#     -       # Match a hyphen
#     \d{2}   # Match two digits
#     -       # Match a hyphen
#     \d{4}   # Match four digits
# '''
# In the verbose pattern, comments (lines starting with #) are allowed, as well as extra whitespace, which is ignored. This can make complex regular expressions much easier to read and understand.
# 
# Here's an example of how you would use re.VERBOSE:
# 
# import re
# 
# pattern = re.compile(r'''
#     \d{3}   # Match three digits
#     -       # Match a hyphen
#     \d{2}   # Match two digits
#     -       # Match a hyphen
#     \d{4}   # Match four digits
# ''', re.VERBOSE)
# 
# text = '123-45-6789'
# 
# match = pattern.match(text)
# 
# if match:
#     print('Match found')
# else:
#     print('No match found')
# In this example, the regular expression pattern is written in verbose mode. The re.VERBOSE flag allows the pattern to span multiple lines and include comments. The regular expression is used to match a Social Security Number pattern.
# 
# 
# 
# 
# 
# 

# 20. How would you write a regex that match a number with comma for every three digits? It must match the given following:
# 
# 
# '42'
# '1,234'
# '6,368,745'
# but not the following:
# '12,34,567' (which has only two digits between the commas)
# '1234' (which lacks commas)
# 
# 
# ==>You can use the following regular expression to match numbers with commas for every three digits:
# 
# 
# import re
# 
# pattern = r'^\d{1,3}(,\d{3})*$'
# Explanation of the pattern:
# 
# ^: Matches the start of the string.
# \d{1,3}: Matches one to three digits.
# (,\d{3})*: Matches zero or more occurrences of a comma followed by exactly three digits.
# $: Matches the end of the string.
# Here's an example of how you can use this pattern:
# 

# In[12]:


import re

pattern = r'^\d{1,3}(,\d{3})*$'

# Test cases
test_cases = ['42', '1,234', '6,368,745', '12,34,567', '1234']

for test_case in test_cases:
    match = re.match(pattern, test_case)
    if match:
        print(f"'{test_case}' is a valid match")
    else:
        print(f"'{test_case}' is not a valid match")


# 21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:
# 'Haruto Watanabe'
# 'Alice Watanabe'
# 'RoboCop Watanabe'
# but not the following:
# 'haruto Watanabe' (where the first name is not capitalized)
# 'Mr. Watanabe' (where the preceding word has a nonletter character)
# 'Watanabe' (which has no first name)
# 'Haruto watanabe' (where Watanabe is not capitalized)
# 
# ==>You can use the following regular expression to match the full name of someone whose last name is "Watanabe":
# 
# import re
# 
# pattern = r'^[A-Z][a-zA-Z]* Watanabe$'
# Explanation of the pattern:
# 
# ^: Matches the start of the string.
# [A-Z]: Matches an uppercase letter (the first letter of the first name).
# [a-zA-Z]*: Matches zero or more lowercase or uppercase letters (the rest of the first name).
# ' ': Matches a space.
# 'Watanabe': Matches the last name "Watanabe".
# $: Matches the end of the string.
# Here's an example of how you can use this pattern:
# 
# 

# In[13]:



import re

pattern = r'^[A-Z][a-zA-Z]* Watanabe$'

# Test cases
test_cases = ['Haruto Watanabe', 'Alice Watanabe', 'RoboCop Watanabe', 'haruto Watanabe', 'Mr. Watanabe', 'Watanabe', 'Haruto watanabe']

for test_case in test_cases:
    match = re.match(pattern, test_case)
    if match:
        print(f"'{test_case}' is a valid match")
    else:
        print(f"'{test_case}' is not a valid match")


# 22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:
# 'Alice eats apples.'
# 'Bob pets cats.'
# 'Carol throws baseballs.'
# 'Alice throws Apples.'
# 'BOB EATS CATS.'
# but not the following:
# 'RoboCop eats apples.'
# 'ALICE THROWS FOOTBALLS.'
# 'Carol eats 7 cats.'
# ==>
# You can use the following regular expression to match the described pattern:
# 
# python
# Copy code
# import re
# 
# pattern = r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$'
# Explanation of the pattern:
# 
# ^: Matches the start of the string.
# (Alice|Bob|Carol): Matches one of the options within the parentheses (case-insensitive).
# : Matches a space.
# (eats|pets|throws): Matches one of the options within the parentheses (case-insensitive).
# : Matches a space.
# (apples|cats|baseballs): Matches one of the options within the parentheses (case-insensitive).
# \.: Matches a period.
# $: Matches the end of the string.
# Here's an example of how you can use this pattern:
# 
# 

# In[14]:



import re

pattern = r'^(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.$'

# Test cases
test_cases = [
    'Alice eats apples.',
    'Bob pets cats.',
    'Carol throws baseballs.',
    'Alice throws Apples.',
    'BOB EATS CATS.',
    'RoboCop eats apples.',
    'ALICE THROWS FOOTBALLS.',
    'Carol eats 7 cats.'
]

for test_case in test_cases:
    match = re.match(pattern, test_case, re.IGNORECASE)
    if match:
        print(f"'{test_case}' is a valid match")
    else:
        print(f"'{test_case}' is not a valid match")


# In[ ]:




