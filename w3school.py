import sys

print(sys.version)

print("hello world")

if 5>2:
     print("yes")


x = 5
y = "Hello, World!"

print(x)
print(y)

#This is a comment

"""
command
command
command
"""

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#gettype

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'


""""
Illegal variable names:

2myvar = "John"
my-var = "John"
my var = "John"

"""


x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#________________________________________________________________   

x = y = z = "Orange"
print(x)
print(y)
print(z)
#________________________________________________________________   

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#________________________________________________________________   

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
#________________________________________________________________   

x = "Python "
y = "is "
z = "awesome"
print(x + y + z+"dell")
#________________________________________________________________   

x = 5
y = 10
print(x + y)
#________________________________________________________________   

x = 5
y = "John"
print(x, y)

#________________________________________________________________   

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


#________________________________________________________________   


x = "2awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#________________________________________________________________   


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#________________________________________________________________   
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#________________________________________________________________   