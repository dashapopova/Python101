#!/usr/bin/env python
# encoding: utf-8

from operator import itemgetter
from itertools import dropwhile
from string import punctuation

"""
Python 101: Programming for Linguists
HSE, Fall 2018
Daria Popova

Assignment 3 Tips

Distributed 2018-09-24
"""

"""===================================================================
1.  Tokenizing. This is one of the most common (and vexing) operations  
when processing data.  There is no single correct way to do it."""

def tokenize(s):
    """Break str s into a list of strings according to some procedure 
    tailored for the task at hand."""

    words = s.lower().strip().split()
    twords = [word.strip(punctuation) for word in words]
    return twords

"""===================================================================
2.   Create a text file, e.g., 'hw3test.txt'.
Complete text_file_wc so that it can read in and tokenize your file."""

def text_file_wc(filename):
    """Open the file with name filename, tokenize it with your 
    tokenize function, and return a dict mapping words to their 
    counts in the file."""
    testtext = open('hw3test.txt').read()
    testtext_tokens = tokenize(testtext)
    text_file_wc = {x: testtext_tokens.count(x) for x in testtext_tokens}
    return text_file_wc


"""===================================================================
3.   Corresponds to question 4 on the homework

The raw data files for the Google Books collection are available for 
download. The files are huge, so I created a sample. Download this 
file to your computer and make sure it is in the same directory/folder 
as this homework file:

https://github.com/dashapopova/Python101/blob/master/googlebooks.txt

The format of this file is as follows (whitespace inserted for 
readability):

word TAB year TAB match_count TAB volume_count NEWLINE

The TAB character is "\t", which you can treat like any other (for
example, you can split a string on "\t").

Your task: complete googlebooks_counts_by_year so that it processes
my sample file and returns a 2d dictionary with this structure:

{
  word1: {year1: count, year2: count ...},
  word2: {year1: count, year2: count ...},
  ...
}

where the nature of the year dicts is determined by the file.
(That is, different words will have different years and counts
associated with them.)"""

def googlebooks_counts_by_year(filename):
    """Maps a Google books 1-grams file to a 2d dictionary
    giving each word's counts by year."""

    d = {}                            
    fields = []                        
    for line in open('googlebooks.txt', "r"):            
        line = line.strip()               
        line = line.split("\t")                
        fields.append(line)                
    for item in fields:
        if item[0] not in d.keys():            
            d[item[0]] = {int(item[1]) : int(item[2])} 
        else:                        
            x = d[item[0]]               
            x[int(item[1])] = int(item[2])      
    return d

if __name__ == '__main__':

    print(text_file_wc('hw3test.txt'))
    print(googlebooks_counts_by_year('googlebooks.txt'))












