"""
Decorators are a feature in Python that allow you to modify the behavior of functions or classes without changing their source code. 
Decorators are defined using the @decorator_name syntax and are applied to functions or classes by placing them above the function or class definition.
"""
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