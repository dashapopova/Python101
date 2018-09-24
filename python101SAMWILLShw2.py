#!/usr/bin/env python
# encoding: utf-8

"""
Python101: Programming for Linguists
HSE Linguistics, Fall 2018
Daria Popova

Assignment 2

Distributed 2018-09-15
Due 2018-09-22 by noon

NOTE: Please submit a modified version of this file, including
comments.  Python should be able to run through your file without
errors.
"""

import math
import pprint

"""===================================================================
1   [1.5 point] 

Complete the function mean for calculating the mean (average) of a 
list of numeric values.  Your function should take a  list vals as its 
argument and return a float.  Keep in mind that vals might contain int 
values.

Consider doing it with the in-line function sum, which facilitates a fast and readable one-line version of the function.
"""

def mean(values):
    total = 0
    length = len(values)
    for i in range(length):
        total + values[i]
    total = sum(values)
    average = total/length
    return average
x = [1, 3.6, 12.2, 15.1]

n = mean(x)
print(n)


"""===================================================================
2   [1.5 point]

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

import math

def mean(values):
    return sum(values)*1.0 / len(values)

def stanDev(values):
    length = len(values)

    m = mean(values)

    total_sum = 0

    for i in range(length):

        total_sum += (values[i] - m)**2

    u_rt = total_sum*1.0 / float(length) 

    return math.sqrt(u_rt)

x = [1, 2, 4, 1, 2, 42, 12]
stan_dev = stanDev(x)

print(stanDev(x))

"""===================================================================
3   [1 point]

Complete the function zscore for computing the z-score (normal score) 
of a list of numeric values.  Your function should take a list vals as 
its value and return a list of z-score normed values. Use mean and sd, 
as defined above, for this calculation.

For details on calculating the z-score, see
http://en.wikipedia.org/wiki/Z_score
"""

import math

def mean(values):
    return sum(values)*1.0 / len(values)

def stanDev(values):
    length = len(values)

    m = mean(values)

    total_sum = 0

    for i in range(length):

        total_sum += (values[i] - m)**2

    u_rt = total_sum*1.0 / length

    return math.sqrt(u_rt)

def zscore(values):
    s = stanDev(values)
    if s(values) > 0:
        for x in range(0,len(values)):
            values[x] = (values[x] - m) / s
        return values[x]
    else:
        return 'n/a'

"""===================================================================
4

Intro to comma-separated values.  The string myspreadsheet stores 11 
lines of comma-separated values, with the first line giving the column 
names and the other lines giving the data on 10 imaginary subjects.  
Below are some questions that ask you to write functions for working 
with this data.
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

"""--------------------------------------------------
Random facts: The column of heights, presumably in 
inches, was generated with

import random

and then repeated runs of

random.uniform(60,77)

The column of occupations was generated with

d = {0:'Psychologist',1:'Linguist'}

and then repeated runs of

d[random.randint(0,1)]
--------------------------------------------------"""

"""===================================================================
4.1  [3 points]

Basic CSV parser. Complete the following function for turning the str 
myspreadsheet into a 10x3 matrix of data.  I should emphasize that the 
top line of myspreadsheet is not part of the data.  It's just there to 
help us out.

Column 0 of your data should be int values.

Column 1 of your data should be float values.

To test your parser, call csv_parser_test, which will work with 
no modifications.
"""

def csv_parser(s):
 results = []
with open("names.csv") as csvfile:
    reader = csv.reader(csvfile) 
    for row in reader: 
        results.append(row)
print(results)
            
"""===================================================================
4.2  [1 point]

Complete the following function for computing the mean height of the 
subjects in this data set, using your mean function from above.
"""

def mean_height(data):
    """Return the mean numerical value of column 1 in an list of lists.
    data is the output of csv_parser(myspreadsheet)"""

"""===================================================================
4.3  [2 points]

Occupation distribution. Complete the following function so that it 
returns a dictionary mapping occupation names into the number of times 
they occur in the data.
"""

def occupation_distribution(data):
    """Returns the list of occupations given in column 2 of data.
    data is the output of csv_parser(myspreadsheet)"""

"""==================================================================="""

def proper_title_case(s):
    """
    Try to do a better job of getting title case.  For example,
    "the cat in the hat".title() ==> "The Cat In The Hat",
    but we want "The Cat in the Hat"    
    """
    nocaps = ["the"] # This needs to be extended.
        
######################################################################

if __name__ == '__main__':

    #print proper_title_case("the cat in the hat")
    #print proper_title_case("an ant on a table")
    #print mean([1,2,3,4,5,6,7,8,9,10])
    #print sd([0,1,2])
    #print zscore([0,2,4])
    #print csv_parser_test()
    #print mean_height(myspreadsheet)
    #print occupation_distribution(myspreadsheet)
