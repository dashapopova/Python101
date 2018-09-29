#!/usr/bin/env python
# encoding: utf-8

"""
Preprocessing in Python: Programming for Linguists
HSE Linguistics, Fall 2018
Daria Popova

Assignment 1 Solutions

Distributed 2018-09-28
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
3

Complete the function zscore for computing the z-score (normal score) 
of a list of numeric values.  Your function should take a list vals as 
its value and return a list of z-score normed values. Use mean and sd, 
as defined above, for this calculation.

For details on calculating the z-score, see
http://en.wikipedia.org/wiki/Z_score
"""

"""def zscore(vals):
    This function is radical: it will replace vals with zscored vals.
    m = mean(vals)
    s = sd(vals)
    if sd(vals) > 0:
        for x in range(0,len(vals)):
            vals[x] = (vals[x] - m) / s
        return vals
    else:
        return 'n/a'"""

def zscore(vals):
    """Return the z-scored version of vals."""

    zscorelist = []
    if sd(vals) > 0:
        for x in vals:
            z = (x - mean(vals))/sd(vals)
            zscorelist.append(z)
        return zscorelist
    else:
        return 'n/a'

"""===================================================================
4.1  

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

"""===================================================================
4.2 

Complete the following function for computing the mean height of the 
subjects in this data set, using your mean function from above.
"""

def mean_height(data):
    """Return the mean numerical value of column 1 in an list of lists.
    data is the output of csv_parser(myspreadsheet)"""

    p = csv_parser(data)
    t = tuple(x[1] for x in p)
    return mean(t)


"""===================================================================
4.3  
Occupation distribution. Complete the following function so that it 
returns a dictionary mapping occupation names into the number of times 
they occur in the data.
"""

def occupation_distribution(data):
    """Returns the list of occupations given in column 2 of data.
    data is the output of csv_parser(myspreadsheet)"""

    p = csv_parser(data)
    t = tuple(x[2] for x in p)
    occupation_dictionary = {"Linguist" : t.count("Linguist"), "Psychologist" : t.count("Psychologist")}
    return occupation_dictionary

"""==================================================================="""

def proper_title_case(s):
    """
    Try to do a better job of getting title case.  For example,
    "the cat in the hat".title() ==> "The Cat In The Hat",
    but we want "The Cat in the Hat"    
    """
    nocaps = ["the", "in", "on", "a", "an"] # This needs to be extended.
    s = s.title()
    words = s.split(" ")
    new_words = []
    for w in words:
        if w.lower() in nocaps:
            w = w.lower()
        new_words.append(w)
    y = " ".join(new_words)
    return y[0].upper() + y[1: ]

"""===================================================================
5. Fillers, making nonsense items [1 point]
5.1
A frequent task for psycholinguists is finding items for experiments, either items that directly exemplify some property we want to test or items that fill out an experiment and can be used to distract subjects from the true goal of the experiment.
Imagine what we want are CV monosyllables. We could just try to think of all possible monosyllables with a CV shape, but another way to go is to generate these programmatically. If we know what the possible consonants are and what the possible vowels are, we can generate a list of possible CV monosyllables quite simply.
"""
#define vowels and consonants
vowels = 'aiu'
consonants = 'ptk'
#for every vowel
for v in vowels:
    #choose a consonant
    for c in consonants:
        #now print them together
        print(c+v)
"""=====
5.2
The same kind of logic can be used to construct nonsense sentences. Imagine we want every possible SVO sentence in some (nonsense) language. We have a set of
nouns and transitive verbs. We can combine them straightforwardly.
"""

#every possible N and V
nouns = 'mama rama'
verbs = 'myla krasila'
#every possible SVO combo
for s in nouns.split():
    for v in verbs.split():
        for o in nouns.split():
            #print combination
            print(s,v,o)


if __name__ == '__main__':

    print(mean([1,2,3,4,5,6,7,8,9,10]))
    print(sd([0,1,2]))
    print(zscore([0,2,4]))
    print(csv_parser(myspreadsheet))
    print(mean_height(myspreadsheet))
    print(occupation_distribution(myspreadsheet))
    print(proper_title_case("the cat in the hat"))
    print(proper_title_case("an ant on a table"))
