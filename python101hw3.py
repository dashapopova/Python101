#!/usr/bin/env python
# encoding: utf-8

from operator import itemgetter
from itertools import dropwhile
from string import punctuation


"""
Python 101: Programming for Linguists
HSE, Fall 2018
Daria Popova

Assignment 3

Distributed 2018-09-21
Due noon 2018-09-29

NOTE: Please submit a modified version of this file, including
comments.  Python should be able to run through your file without
errors.
"""

"""===================================================================
1.   [2 points] 

Tokenizing. This is one of the most common (and vexing) operations  
when processing data.  There is no single correct way to do it.  The 
correct method will depend on the task at hand.  This problem is 
designed to give you a sense for the challenges and the possibilities. 
Give it some thought, but don't go overboard.  We'll soon have 
additional techniques for defining good tokenizers."""

def tokenize(s):
    """Break str s into a list of strings according to some procedure 
    tailored for the task at hand."""

"""===================================================================
2.  [2 points] 

Download this file to your computer and make sure it is in the same
directory/folder as this homework file:

github.com/dashapopova/Python101/alice.txt

Open alice.txt in your text editor and study its composition. Clearly,
we would need to do a lot of special processing of this file in order
to get accurate word counts for Alice.  However, for this problem, you
need to make only a minimal effort:

Complete gutenberg_file_wc so that it can read in the file alice.txt 
and tokenize only the lines that occur between the two lines from the 
file that start this way:

*** START OF THIS PROJECT GUTENBERG EBOOK
*** END OF THIS PROJECT GUTENBERG EBOOK

There are a lot of strategies for doing this.  The one that is
NOT ALLOWED is deleting material from alice.txt and saving the
result.  Your function has to work without any modifications to 
alice.txt."""

"""alice = open('alice.txt').read()

a = alice.find("*** START OF THIS PROJECT GUTENBERG EBOOK") 

z = alice.find("*** END OF THIS PROJECT GUTENBERG EBOOK") 

alice_new = alice[a:z]"""

def gutenberg_file_wc(filename):
    """Open the file with name filename, tokenize it with your 
    tokenize function, and return a dict mapping words to their 
    counts in the file.  Tokenize only the material that occurs
    between the two lines given above."""
   


"""===================================================================
3.   [2 points] 

This problem asks you to write a little helper function to view the
output of gutenberg_file_wc.  The goal is to print to the screen a
list of (word, count) pairs, sorted so that the most frequent word
is at the top.  Requirements:

* We want to see only words whose count is at least 10.
* The output should be formatted so that it can be read by the 
Wordle Advanced API: 

http://www.wordle.net/advanced

* Optional: Attach your Wordle image with your homework.

To sort a dictionary on its value element, with the most frequent
tuple at the top of the list, I recommend this method:

d = {'a': 5, 'b': 10, 'c': 8}
from operator import itemgetter
dist = sorted(d.items(), key=itemgetter(1), reverse=True)

Optional extra credit (0.5 points): it would nice for the threshold 
value to be something that the user can set when calling view_wc(),
rather than having it coded as part of the function.  Modify
view_wc so that the default is 10 but the user can set the value
when calling the function.
"""

def view_wc(d):
    """The input is a dict d mapping strings to ints. 
    The function should sort d in reverse order and
    return only pairs whose count value (index 1) is
    at least as large as the threshold, set to 10."""


"""===================================================================
4.   [2 points] 

The raw data files for the Google Books collection are available for 
download. The files are huge, so I created a sample. Download this 
file to your computer and make sure it is in the same directory/folder 
as this homework file:

github.com/dashapopova/Python101/googlebooks.txt

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

"""===================================================================
5.   [2 points] 

Complete the function googlebooks_year_collapse so that it takes
as input the output of googlebooks_counts_by_year and collapses
it down so that each word is associated with its single tokencount
for the full, obtained by summing up all of the counts for the
years associated with that word. 

Once you've written this function, you can use view_wc to view it."""

def googlebooks_year_collapse(d):
    """Convert the output of googlebooks_counts_by_year to 
    a simpler dict mapping words to counts."""


if __name__ == '__main__':

    #print gutenberg_file_wc('alice.txt')
    #print view_wc(gutenberg_file_wc('alice.txt'))
    #print googlebooks_counts_by_year('googlebooks.txt')
    #print googlebooks_year_collapse(googlebooks_counts_by_year('googlebooks.txt'))
