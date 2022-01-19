"""
Python Syntax can be writen in command line
Python Indentation
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important.
Python uses indentation to indicate a block of code.
"""

# Example
if 5 > 2:
  print("Five is greater than two!")

# Python will give you an error if you skip the indentation:
# example

if 5 > 2:
print("Five is greater than two!") #here you get a syntax error

# The number of spaces is up to you as a programmer, but it has to be at least one.
# Example
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!") 

# Python Variables
# In Python, variables are created when you assign a value to it:

# Example
# Variables in Python:

x = 5
y = "Hello, World!"
""""
Python has no command for declaring a variable.
You will learn more about variables in the Python Variables chapter.

Comments
Python has commenting capability for the purpose of in-code documentation.
Comments start with a #, and Python will render the rest of the line as a comment:

use of comments
Comments in Python:
Comments can be used to explain Python code.
Comments can be used to make the code more readable.
Comments can be used to prevent execution when testing code.

Creating a Comment
Comments starts with a #, and Python will ignore them:
"""

#This is a comment.
print("Hello, World!")

# Comments can be placed at the end of a line, and Python will ignore the rest of the line:
# example
print("welcome to kabwata") #this is a comment

# A comment does not have to be text that explains the code, it can also be used to prevent Python from executing code:

# Example
#print("Hello, World!")
print("Cheers, Mate!")

"""
Multi Line Comments
Python does not really have a syntax for multi line comments.
To add a multiline comment you could insert a # for each line:
"""

# Example
#This is a comment
#written in
#more than just one line
print("Hello, World!")










