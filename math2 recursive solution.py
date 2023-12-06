import math

def math2(x,n, max_n) :
    sign = math.pow(-1,n)
    exponent = math.pow(x,2 * n)
    fact = math.factorial(2 * n)
    term = sign * exponent / fact

    if n == max_n :
        return term
    
    return term + math2(x,n + 1, max_n)

print(f'{math2(0.0, n = 0, max_n = 10) = }')
# output: math2(0.0, n = 0, max_n = 10) = 1.0

print(f'{math2(0.5,n = 0, max_n = 10) = }')
# output math2(0.5, n = 0, max_n = 10) = 0.8775825618903728