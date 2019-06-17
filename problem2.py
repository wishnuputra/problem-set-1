# -*- coding: utf-8 -*-
"""
===================================================
Problem 2:
===================================================

Assume s is a string of lower case characters.

Write a program that prints the number of times the
string 'bob' occurs in s. For example,
if s = 'azcbobobegghakl', then your program should
print:

"Number of times bob occurs is: 2"

Created on Sun Jun 16 17:55:52 2019

@author: Wishnuputra
===================================================
"""

s = "azcbobobegghakl"

numBob = 0

for i in range(len(s)):
    if s[i:i+3] == "bob":
        numBob += 1

print("Number of times bob occurs is:", numBob)