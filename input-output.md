# Input--output

Now we turn to programs that can respond to data entered by a user or that come from a file or set of files. 

Here we look at the following ways of inputting data:
1. **Keyboard input**: a user can enter data when prompted by the program.
2. **File input–output**: a program can read data from or write data to files. 

### Keyboard input

We can write programs that pause at some point and wait for the user to enter data. The code for this is quite simple: there is a function `input()` that takes a single string
argument and returns what the user types as a string:

```python
s = input('Type something: ')
print('You typed "',s, '"')
```

*A potential downside*: the data have to be typed in by hand.

There is a potentially *desirable aspect* of entering data from the keyboard like this: the number and content of each input item can respond
to the program's behavior with respect to earlier items.

```python
import random
letters = ’abcdefghijklmnopqrstuvwxyz’
#get a random letter
letter = letters[random.randint(0,25)]
#loop until the user guesses correctly
while True:
#prompt them to type a letter
  guess = input(’Type a lower-case letter: ’)
  #check that it’s actually a letter
  if guess not in letters:
    print(”That’s not a lower-case letter.”)
    continue
  #if they’re right
  if guess == letter:
    print(”That’s right!”)
    break
  #give them a hint if they’re wrong
  if guess > letter:
    print(”It’s earler in the alphabet.”)
  else:
    print(”It’s later in the alphabet.”)
```

### File input-output

The usual way to input or output large amounts of data is from or to files. The
basic idea is that your program is written to respond to any amount of data. The
file contains data of the appropriate sort and your program reads in that data and
processes it either all at once or chunk by chunk.

Writing to files is a dangerous operation. If you are not careful, you
can accidentally overwrite important data. Work with *copies* of the files.

Let’s begin with **writing to a file**. The basic logic is that you create a stream
or pathway to a file, print to that stream, and then close the stream. Here’s a very
simple example of this:
```python
#open the file stream
newFile = open(’testfile.txt’,’w’)
#write to it
newFile.write(’some text!\n’)
newFile.write(’...and some more text!\n’)
#close the stream
newFile.close()
```
Let’s now look at **file input**. The system is basically the same. You create a file
input stream, read from it, and then close the stream. In the following example,
we read from the file we created in the previous example and print the result to the
screen.

```python
#open file stream
newFile = open(’testfile.txt’,’r’)
#read form it
stuff = newFile.read()
#close stream
newFile.close()
#print contents
print(stuff)
```
It is possible to read lines from the stream and process them one by one:

```python
#open file
newFile = open(’testfile.txt’,’r’)
#read from stream line by line
for line in newFile:
  #print length of line and the line
  print(len(line),’: ’,line,sep=’’,end=’’)
#close file stream
newFile.close()
```
