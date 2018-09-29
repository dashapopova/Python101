## Homework 4 Assignment -- due 6.10 by 12:00

### Task 1: Initial Consonant Clusters \[7 points\]

Your task is to show me how to use pattern matching to investigate the distribution of
word-initial consonant clusters in *Alice* (alice.txt). The basic question is how frequent different
kinds of initial consonant clusters are. 

An initial consonant cluster is a sequence of consonants (not interrupted by vowels) at the beginning of a word.
E.g., *crouton* has an initial consonant cluster *cr*, *flamingo* has an initial consonant cluster *fl*, 
*mimosa* does not have an initial consonant cluster, it starts with a single consonant. 

A challenge here is that English orthography only indirectly reflects the phonology.
First, you must deal with silent letters. These include cases like *know* or *gnostic* where *k* and
*g* are silent. Another issue to wrestle with is that sometimes a single consonant
is written with several letters, e.g. [θ] as in *thimble* or [ʃ] as in *show*, etc. Finally,
there are cases where the same letter (sequence) has multiple pronunciations. For
example, *c* is pronounced [s] in *city*, but [k] in *coat*. Similarly, *ch* is pronounced [tʃ]
in *church*, but [k] in *chord*. Note that sometimes the difference is predictable, as in
the case of *c*, but sometimes it is not, as in the case of *ch*. You should set aside
the mapping of orthography to precise phonological forms, except insofar as you
need to decide what a cluster is.

You will need to do the following (or something which is analogous to the following):

1. apply the `gutenberg_file_wc(filename)` (HW3 Q1,2) and the `view_wc(d)` (HW3 Q3) functions to alice.txt -- up to 2 points;
2. try to search for (word) initial consonant clusters using regular expression(s) (Don't forget to `import re` at the beginning of your program) -- up to 2 points;
3. do the counts for all the clusters that you have identified -- 2 points; 
4. print the clusters with the counts -- 1 point.
   
### Task 2 \[3 points\]

These tasks are designed to start you thinking about your project: you don't need to figure out everything by the next Saturday, but I want to see that you are thinking about your project. And remember that, unfortunately, our course will end in this module, so the deadline for the final project will be October, 20th.

1. State your final project idea. Say a few words about why you are interested in doing this project. -- 1 point
2. Split your project into tasks that you would like to accomplish -- 1 point
3. Make the first step (e.g., if you opt for Funky Dictionary, you should list 10 potential entries for the dictionary; if you choose to write a tokenizer for a particular language, select a text file that you will use to train your tokenizer on) -- 1 point.

#### Final Project Suggestions

##### Funky dictionary -- a group project

Create a dictionary of funky Russian words -- slang, expressives, old-fashioned words, fairytale characters. If the word is already in the dictionary, the user will be able to see its definition and rate(!) it. If the word is not in the dictionary, the user should have an option of adding it and its definition to the dictionary. The user should have an option of seeing the words with the top most ratings. May be, you could also add the *fortune cookie word game* -- the user gets a randomly chosen word as a sort of prophecy for the day.

##### Tokenizer 2.0

Write a more advanced version of the tokenizer that you have written for HW3 question 1. For example, you could make use of regular expressions that we have learnt today. You can choose any language, including English, but if you choose English, you will have to write a truly decent version of a tokenizer (and you won't be allowed to just import existing tokenizer modules for English).
