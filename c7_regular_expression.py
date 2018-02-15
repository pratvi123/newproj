# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 18:11:42 2017

@author: DELL
"""

import re

str1 = 'an example word:bat!!'
match = re.search(r'word:\w\w\w', str1)
print  (match.group()) 

match=re.search(r'exa.*',str1)
print(match.group())
match=re.search(r'^an.*',str1)
print(match.group())

match = re.search(r'iii', 'riiing') 
print(match.group())

match = re.search(r'igs', 'riiigs')
print(match.group())

## . = any char but \n
match = re.search(r'..g', 'riiig')
print(match.group())
## \d = digit char, \w = word char

match = re.search(r'\d\d\d', 'p123g')
print(match.group())

match = re.search(r'\w\w\w', '@@abcd!!')
print(match.group())

#Repetition Examples
match = re.search(r'ri+', 'riiig') 
print(match.group())


match = re.search(r'[rgi]+', 'riiiggggg') 
print(match.group())

match = re.search(r'i+', 'riigiiii')
print(match.group())

match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx')
print(match.group())



match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx')
print(match.group())
match = re.search(r'^f\w+', 'foobar')
print(match.group())
 

S='real time rat10000023'
ptr=r'[a-z]+[\d]+'
match=re.search(ptr,S)
print(match.group())

S='real time skalwa404@gmail.com'
ptr=r'[a-z0-9A-Z]+@[\w]+.[\w]+'
match=re.search(ptr,S)
print(match.group())


S1="Mohammed Akthar kazi aktharkazi@realtimesig.com 10254850"
ptr=r'[a-z]+@[a-z]+.[a-z]+'
match=re.search(ptr,S1)
print(match.group())




S1="Mohammed Akthar kazi aktharkazi@realtimesig.com 10254850"
ptr=r'([a-z]+)@([a-z]+).([a-z]+)'
match=re.findall(ptr,S1)
print(match)
'''



str1 = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
## re.sub(pat, replacement, str) -- returns new string with all replacements,
## \1 is group(1), \2 group(2) in the replacement
print re.sub(r'([\w\.-]+)@([\w\.-]+)', r'\1@yo-yo-dyne.com', str)
## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher
'''
