# Functional Programming
## Map, Filter, Reduce, Zip and Lambda Function
* Map - Map function helps to create a new and modified array without affecting real array
  ```python
  lists = range(1, 100)
  
  def multiply2times(items):
     return items * 2

  newArray = map(multiply2times, lists)
  ```
  <br/>
  
* Filter - Filter function helps to filter on a certain condition
  ```python
  lists = range(1, 100)
  
  def filteredOdd(items):
    return items % 2 == 0
    
  newList = filter(filteredOdd, lists)

  ```
<br/>

* Reduce - With reduce function you can do many things that can be done with filter and map and much more
  ```python
  from functools import reduce
  def reduce_f(acc, item):
    return acc + str(item)

  reducedList = reduce(reduce_f, [1, 2, 3, 4, 5, 5], "")
  ```
  Capitalize all of the pet names and print the list with reduce function
  ```python
    
   my_pets = ['sisi', 'bibi', 'titi', 'carla']

   def cap(acc, item):
    acc += f"""    {item.capitalize()}\n{len(item) * 3 * "_"} \n"""
    return acc
    reducedList = reduce(cap, my_pets, "")
  ```
  <br/>
* Zip - Pack your list into one
  ```python
  numbers = [1, 2, 3]
  letters = ['A', 'B', 'C']
  names = ['John', 'Alice', 'Bob']

  zipped = zip(numbers, letters, names)
  ```
</br>

* Lambda Function: A lambda function in Python is an anonymous function that can be defined in a single line and used as a lightweight, inline function. <br/>
  **Structure:**
  ```python
  add = lambda x, y: x + y
  result = add(3, 5)
  print(result)  # Output: 8 
  ```

## List, Dict, Set Comprehension
List comprehension is a concise syntax in Python to create new lists by transforming or filtering existing iterables in a single line of code.
**Structure of List Comprehension:**<br/>
**[parameters for parameters in iterables condition (Optional)]** <br/>

**Code:**
```python
#Without Condition
newListComprehense = [nums * 2 for nums in range(1, 10)]

##With Condition
odd = [nums * 2 for nums in range(1, 10) if nums % 2 == 0]

# Set and dictionary comprehension
#SET
setOfOdds = {nums * 2 for nums in range(1, 10) if nums % 2 == 0}

#dictionary comprehension
dict = {"A": 1, "B": 2}

my_dict = {key: value**2 for key, value in dict.items()}
```
## Decorators
Decorators are a feature in Python that allow you to modify the behavior of functions or classes without changing their source code. Decorators are defined using the @decorator_name syntax and are applied to functions or classes by placing them above the function or class definition.
```python
def decorators(fn):
  def extra_features(*args):
    print("******************")
    fn(*args)
    print("******************")

  return extra_features  #Returning function definaion

@decorators
def hello(arg):
  print(arg)


hello("Greet")
```
Performance Decorator Code(Self Made)
```python
#Decorators Excersize - Performance decorators
from time import time


def performance(func):
  def wrapper(*args):
    t1 = time()
    func(*args)
    t2 = time()
    print(f"It took{t2-t1}")

  return wrapper


@performance
def code(firstNum, lastNum):
  for i in range(firstNum, lastNum):
    i * 5
```

## Generators
A generator in Python is a special type of iterator that allows you to iterate over a sequence of values without needing to store them all in memory at once. 
It pauses the function then run the next() to make it run
```python
def generator_function(num):
  for i in range(num):
    yield i #Yield pause a function

g = generator_function(1000)
next(g) # 0
next(g) #1
print(next(g)) #2
  ```