#MAP -> Map function helps to create a new and modified array without affecting real array
lists = range(1, 100)

def multiply2times(items):
   return items * 2

newArray = map(multiply2times, lists)

#FILTER -> Filter function helps to filter on a certain condition
def filteredOdd(items):
  return items % 2 == 0
  
newList = filter(filteredOdd, lists)

#Reduce - With reduce function you can do many things that can be done with filter and map and much more
from functools import reduce

def reduce_f(acc, item):
  return acc + str(item)

reducedList = reduce(reduce_f, [1, 2, 3, 4, 5, 5], "")

#ZIP -> Pack your list into one
numbers = [1, 2, 3]
letters = ['A', 'B', 'C']
names = ['John', 'Alice', 'Bob']

zipped = zip(numbers, letters, names)

#Lambda -> A lambda function in Python is an anonymous function that can be defined in a single line and used as a lightweight, inline function.
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8 