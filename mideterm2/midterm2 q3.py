'''
Write a function, higher_order3, which finds the sum of the return values produced when each value from the list is passed to the provided function.

The arguments of the function will be:

values - the sequence of values to be searched
op - the operation to be performed on each value
Sample calls of this function and their output are given below, but your code should work for all inputs:

def times_two(x):
   return x * 2
print(f'{higher_order3([2,1,3], times_two) = }')
# output: higher_order3([2,1,3], times_two) = 12

print(f'{higher_order3([6,-3,2], lambda x: x ** 2) = }')
# output: higher_order3([6,-3,2], lambda x: x ** 2) = 49
'''

def higher_order3 (values, op) :
    sum = 0
    for value in values : 
        sum += op(value)
        
    return sum

def times_two(x) : 
    return x * 2

print(f'{higher_order3([2,1,3], times_two) = }')
# output: higher_order3([2,1,3], times_two) = 12

print(f'{higher_order3([6,-3,2], lambda x: x ** 2) = }')
# output: higher_order3([6,-3,2], lambda x: x ** 2) = 49