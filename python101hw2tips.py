#!/usr/bin/env python
# encoding: utf-8

"""
Python101: Programming for Linguists
HSE Linguistics, Fall 2018
Daria Popova

Assignment 2 Tips

Distributed 2018-09-24
"""

import math
import pprint

"""===================================================================
1

Complete the function mean for calculating the mean (average) of a 
list of numeric values.  Your function should take a  list vals as its 
argument and return a float.  Keep in mind that vals might contain int 
values.

Consider doing it with the in-line function sum, which facilitates a fast and readable one-line version of the function.
"""

def mean(vals):
    """Return the mean of the values in vals, presupposed to be 
    numeric (float, int, or long)."""

    return float(sum(vals)) / len(vals) if len(vals) > 0 else print('n/a')

"""===================================================================
2   
Complete the function sd for calculating the standard deviation of a 
list of numeric values.  Your function should take a list vals as its 
value and return a float.  Keep in mind that vals might contain int 
values.

For details on calculating the standard deviation, see
http://en.wikipedia.org/wiki/Standard_deviation

I suggest using float(len(vals)-1) for the denominator, but 
float(len(vals)) is fine.

To get the square root of a float x, using math.sqrt(x)
"""

def sd(vals):
    """Return the standard deviation of the values in vals, 
    presupposed to be numeric (float, int, or long)."""

    sum = 0.0
    for x in vals:
        sum += (x - mean(vals))**2
    return math.sqrt(sum/float(len(vals)-1)) if len(vals) > 1 else print('n/a')

"""===================================================================
4.1  [3 points]

Basic CSV parser. Complete the following function for turning the str 
myspreadsheet into a 10x3 matrix of data.  I should emphasize that the 
top line of myspreadsheet is not part of the data.  It's just there to 
help us out.

Column 0 of your data should be int values.

Column 1 of your data should be float values.
"""

myspreadsheet ="""Subject,Height,Occupation
1,74.37000326528938,Psychologist
2,67.49686206937491,Psychologist
3,74.92356434760966,Psychologist
4,64.62372198999978,Psychologist
5,67.76787900026083,Linguist
6,61.50397707923559,Psychologist
7,62.73680961908566,Psychologist
8,68.60803984763902,Linguist
9,70.16090500135535,Psychologist
10,76.81144438287173,Linguist"""

def csv_parser(s):
    """Parses the string s into lines, and then parses those lines by
    splitting on the comma and converting the numerical data to int.
    The output is a list of lists of subject data."""

    # Data is our output. It will be a list of lists.
    data = []    

    # Split csv into lines and store them in a list called 'lines'.
    lines = s.splitlines()
    
    # Remove the first element from lines, so that you have only the data lines left.
    lines = lines[1: ]
    
    # At this stage, we loop through the list called lines.
    # As you loop
    #     i. split each line on the commas;
    #    ii. convert the Subject variable to int.
    #   iii. convert the Height variable to float.
    #    iv. add to data a list consisting of this line's Subject, Height, and Occupation values 
    for line in lines:
        l = line.strip().split(",")
        l[0] = int(l[0])
        l[1] = float(l[1])
        data.append(l)
    return data

if __name__ == '__main__':

    print(mean([1,2,3,4,5,6,7,8,9,10]))
    print(sd([0,1,2]))
    print(csv_parser(myspreadsheet))


