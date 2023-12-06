# Create a function (drawSquare) that, for any positive integer n, prints an n xn square made of ‘*’ symbols.
def drawSquare(n) :
    for _ in range(n) :
        print('*' * n)

drawSquare(4)

# Create a function (drawTriangle) that, given any positive integer n, prints an n xn triangle made of ‘*’ symbols.

def drawTriangle(n) :
    for i in range(1, n + 1) :
        print('*' * i)

drawTriangle(4)

# Create a function (drawTriangle2) that, given any positive integer n, prints an upside-down n xn triangle made of ‘*’ symbols.

def drawTriangle2(n) :
    for i in range(n, 0, -1) :
        print('*' * i)

drawTriangle2(4)

# Create a function (jumpMaximum) that, given any list of integers list, returns a list with the same elements as list, except that the first element has been swapped with the maximum element in list.

def jumpMaximum(list) :

    largest = max(list)
    largest_index = list.index(largest)
    list[0], list[largest_index] = list[largest_index], list[0]

    return list

print(jumpMaximum([1,2,3,4]))
print(jumpMaximum([5,8,3,21,7,4,14]))

# Create a function (doubleList) that, given any list of floating point numbers list, returns a list where every element of the output list corresponds to the element at the same position in list, but doubled (times two).Note: This function should not print the list, but return it.

def doubleList(list) :
    list = [num * 2 for num in list]
    return list

print(doubleList([1,2,3,4]))
# expected: [2,4,6,8]

print(doubleList([5,8,3,21,7,4,14]))
# expected: [10,16,6,42,14,8,28]

# Create a function (sublistInRange) that, given a list of floating point numbers, list, and two numbers (min and max), returns a list (or modify list) where the elements of the output list corresponds to the elements of list that are greater than or equal to min and less than or equal to max.

def sublistInRange(list, min, max) :
    list = [num for num in list if num >= min and num <= max]
    return list

print(sublistInRange([1,2,3,4,5], 2, 4))
# expected [2,3,4]


print(sublistInRange([5,8,3,21,7,4,14], 4, 14))
# expected [5,8,7,4,14]


    