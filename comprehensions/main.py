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