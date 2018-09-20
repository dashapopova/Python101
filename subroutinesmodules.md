### Subroutines and Modules

Eventually, you might want to break your code into more efficient and conceptually
more reasonable chunks and to re-use it. In order to do that, we need to learn how to write our own functions and modules.

1. **Simple functions**

Functions are defined with the `def` keyword, followed by a function name of your
choosing, parentheses, and colon. These are followed by a block of statements.

```python
#a function to print that sentence
def myfunc():
  print(’Colorless green ideas...’)
  print(’...sleep furiously’)
#invoke the function
myfunc()
#collect the number
num = input(’Enter a number: ’)
#check if the number is < 5
if int(num) < 5:
  #print the sentence again if so
  myfunc()
else:
  print(’Your number was big enough’)
```
Advantages:
* the new code makes it clear that the repeated parts are the same;
* if we wanted to change one of the repeated
lines, we can do so once and the change is applied in both applications of the
function.

2. **Functions that return values**

The returned value of a function follows the keyword `return`.

```python
#function definition
def sillyfunc():
  #user supplies a word
  wd = input(’Type a word: ’)
  #check the length of the word
  if len(wd) > 4:
    #return length of word...
    #...and exit function
    return len(wd)
  #otherwise...
  else:
    print(’The word is too short!’)
#save value of function in variable
res = sillyfunc()
#print value of variable
print(’The result: ’,res)
```

3. **Functions that take arguments**

For a function to take an argument, you put some number of
variable names in the parentheses in the function definition.

```python
#function that takes 2 arguments
def myfunc(a,b):
  #return the concatenation
  #OR addition of those values
  return a + b
#invoke the function with numbers
print(myfunc(3,10))
#invoke the function with strings
print(myfunc(’strings ’,’too’))
```

The `=` can be used in the function declaration as well to give default values to the
function arguments. Here's an example:

```python
#function with default value
#for 2nd argument
def f(x,y=’oops’):
  return x + ’ ’ + y
#invoked 3 ways
print(f(’hat’))
print(f(x=’chair’))
print(f(’hat’,’chair’))
```
You can also write functions with a variable number of arguments. If you want
a variable number of unnamed arguments, you put some variable name in the
parentheses in your function declaration with a preceding asterisk. This variable
can then be used as a list in the function body. If you want a variable number of
named arguments, you put some variable name in the parentheses in your function
declaration with two preceding asterisks. This variable can be used as a dictionary
in the function body. If you use both, the list variable must precede the dictionary
variable. Here is a simple example:

```python
#function with an unspecified
#number of unnamed and named arguments
def func(*args,**kwargs):
  #print unnamed args
  for a in args:
    print(’\t’,a)
  #print named args
  for k in kwargs:
    print(’\t’,k,’\t’,kwargs[k])
#invoked with unnamed FOLLOWED by
#named arguments
func(3,6,8,hat=’wow’,chair=3.5)
```
4. **Modules**

To find out what modules are installed on your system, go to the interactive system
and type:
```python
>>> help(’modules’)
...
```

To find out more about any one of these, you first import it and then use
the help system. For example:
```python
>>> import re
>>> help(re)
...
```
When a program is loaded in directly, rather than imported from another program:
```python
#module that can run on its own
#a variable
myVar = ’hats and lemons’
#a function
def myFunc(s):
  return len(s)
#if this is loaded on its own...
if __name__ == ’__main__’:
#do this
  print(myFunc(myVar))
```






