#!/usr/bin/env python


# the alphabet
alet = 'abcdefghijklmnopqrstuvwxyz'


# establish a dict
aDict = {}


# assign the characters in the alphabet
n = 1
m = 0


for i in alet:
    aDict[i] = n
    n += 1


# get the word entered and get the numercial value
enter = raw_input('>').lower()
for i in enter:
    if i in alet:
        m += aDict[i]
    else:
        pass

print m