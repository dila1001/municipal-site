"""
Python does offer magic methods like sum() and others, please try to write down your algorithms or coding 
instructions clearly without using any shortcuts
"""
# Multiply 3 and any number
def mult(number):
    if(not isinstance(number, (int, float))):
        raise TypeError('Expected type int or float')
    return 3 * number

    
# adds two numbers together
def add(a, b):
    if(not (isinstance(a, (int, float)) & isinstance(b, (int, float)))):
        raise TypeError('Expected type int or float')
    return a + b

"""
Using data structures like list, can you find the total or the values in that list.
Do not use a function like sum(someList), that would be cheating ;-)
"""
# Data structure
numbers = [1,2,3,6]
def sumOfListNumbers(someList):
    res = 0
    for n in someList:
        res += n

    return res
    

# Program checker (do not change the lines below)    
assert sumOfListNumbers(numbers) == 12
assert mult(3) == 9
assert add(1,3) == 4