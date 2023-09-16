"""
Generators
A generator in Python is a special type of iterator that allows you to iterate over a sequence of values without needing to store them all in memory at once. It pauses the function then run the next() to make it run
"""

def generator_function(num):
  for i in range(num):
    yield i #Yield pause a function

g = generator_function(1000)
next(g) # 0
next(g) #1
print(next(g)) #2