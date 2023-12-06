# Create a function (reverse_rec) that takes a single string and returns the reverse of that string using recursion

def reverse_rec(string):
    if len(string) <= 1:
        return string
    
    # Recursive case: Reverse the substring excluding the first character,
    # then append the first character at the end
    return reverse_rec(string[1:]) + string[0]

# Test the function
original_string = "Hello, World!"
reversed_string = reverse_rec(original_string)
print(reversed_string)

# Write a recursive function (palindrome_rec) that takes a string (str), and returns True or False, depending on whether or not str is a palindrome.

def palindrome_rec(s):
    # Base case: If the string has zero or one character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Recursive case: Check if the first and last characters are equal,
    # and check if the substring without the first and last characters is a palindrome
    return s[0] == s[-1] and palindrome_rec(s[1:-1])

# Test the function
test_string1 = "radar"
test_string2 = "python"

print(palindrome_rec(test_string1))  # Output: True
print(palindrome_rec(test_string2))  # Output: False

# QUESTION 3 

class Product:
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def get_shipping_cost(self):
        shipping_cost = self.weight * 10
        return shipping_cost

    def get_tax(self):
        tax = self.price * 0.13
        return tax

    def get_total_cost(self):
        shipping_cost = self.get_shipping_cost()
        tax = self.get_tax()
        total_cost = self.price + tax + shipping_cost
        return total_cost

# Test the class with sample output
razor = Product("Electric Razor", 49.99, 0.25)
home_gym = Product("Home Gym", 879.99, 115.0)

print(f'Total cost of {razor.name}: {razor.get_total_cost():0.2f}')
# Output: Total cost of Electric Razor: 58.99

print(f'Total cost of {home_gym.name}: {home_gym.get_total_cost():0.2f}')
# Output: Total cost of Home Gym: 2144.39

# QUESTION 4

class Student_Entry:
    def __init__(self, name, sid):
        self.labs = 0.0
        self.assignments = 0.0
        self.midterm = 0.0
        self.final = 0.0
        self.name = name
        self.sid = sid

    def get_average(self):
        weighted_average = (self.labs + self.assignments) / 30 * 30 + self.midterm * 0.3 + self.final * 0.4
        return weighted_average

    def letter_grade(self):
        average = self.get_average()

        if 80 <= average <= 100:
            return 'A'
        elif 70 <= average <= 79:
            return 'B'
        elif 60 <= average <= 69:
            return 'C'
        elif 50 <= average <= 59:
            return 'D'
        else:
            return 'F'

    def __lt__(self, other):
        return self.get_average() < other.get_average()

# Test the class with sample output
bsmith = Student_Entry("Bob Smith", "1000001")
bsmith.labs = 9.0
bsmith.assignments = 17.0
bsmith.midterm = 57.5
bsmith.final = 60.0
print(f'Bob Smith: {bsmith.letter_grade()}')
# Output: Bob Smith: C

sjones = Student_Entry("Sally Jones", "1000002")
sjones.labs = 9.5
sjones.assignments = 19.5
sjones.midterm = 81.0
sjones.final = 74.5
print(f'Sally Jones: {sjones.letter_grade()}')
# Output: Sally Jones: A

# QUESTION 5

class Dictionary:
    def __init__(self):
        self.data = []

    def set(self, key, value):
        # Check if the key already exists, and update the value if it does
        for i, (existing_key, existing_value) in enumerate(self.data):
            if existing_key == key:
                self.data[i] = (key, value)
                return

        # If key doesn't exist, add a new key/value pair
        self.data.append((key, value))

    def get(self, key):
        for existing_key, existing_value in self.data:
            if existing_key == key:
                return existing_value

        # If key doesn't exist, raise KeyNotFoundError
        raise KeyNotFoundError(f'Key not found: {key}')

    def __str__(self):
        return str(self.data)


class KeyNotFoundError(Exception):
    pass

# Test the classes with sample output
products = Dictionary()
products.set('RTX3060', 329.99)
products.set('RTX3070', 499.99)
products.set('RTX3080', 1499.99)
products.set('RTX3090', 1999.99)

print(f'products = {products}')
# Output: products = [('RTX3060', 329.99), ('RTX3070', 499.99),
# ('RTX3080', 1499.99), ('RTX3090', 1999.99)]

try:
    print(f'RTX3090 = {products.get("RTX3090")}')
    # Output: RTX3090 = 1999.99
    print(f'RTX3050 = {products.get("RTX3050")}')
except KeyNotFoundError as error:
    print(f'Cannot find key: {error}')
    # Output: Cannot find key: Key not found: RTX3050

# QUESTION 6
import math
def math1(x, n, max_n):
    total = 0.0
    for i in range(n, max_n + 1):
        term = math.pow(-1, i) * math.pow(x, i) / math.factorial(i)
        total += term
    return total

print(f'{math1(0.0, n = 0, max_n = 10) = }')
# output: math1(0.0, n = 0, max_n = 10) = 1.0
print(f'{math1(0.5, n = 0, max_n = 10) = }')
# output: math1(0.5, n = 0, max_n = 10) = 0.606530659724375

# QUESTION 7

def math2(x, n, max_n):
    total = 0.0
    for i in range(n, max_n + 1):
        term = 2 * math.pow(-1, i) * math.pow(x, 2 * i + 1) / (math.sqrt(math.pi) * (2 * i + 1) * math.factorial(i))
        total += term
    return total

print(f'{math2(0.0, n = 0, max_n = 10) = }')
# output: math2(0.0, n = 0, max_n = 10) = 0.0
print(f'{math2(0.5, n = 0, max_n = 10) = }')
# output: math2(0.5, n = 0, max_n = 10) = 0.5204998778130467
