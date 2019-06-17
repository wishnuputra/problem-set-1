# -*- coding: utf-8 -*-
"""
====================================================
Problem 3:
====================================================

Assume s is a string of lower case characters.

Write a program that prints the longest substring
of s in which the letters occur in alphabetical
order. For example, if s = 'azcbobobegghakl', then
your program should print:

"Longest substring in alphabetical order is: beggh"

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program
should print:

"Longest substring in alphabetical order is: abc"
Created on Sun Jun 16 20:28:41 2019

@author: Wishnuputra
====================================================
"""
s = 'abcbcdazcbobobegghaklgopprrrzzaaabcddddeeef'

temp = ""
temp2 = ""
longest = ""
sLen = len(s)

for i in range(0, sLen-1):    
    if s[i] < s[i+1] or s[i] == s[i+1]:
        temp += s[i]
        if i+1 == sLen-1:
            temp += s[i+1]
            temp2 = temp
    elif s[i] > s[i+1]:
        temp += s[i]
        temp2 = temp
        temp = ""

    if len(temp2) > len(longest):
        longest = temp2
        
print("Longest substring in alphabetical order is:", longest)