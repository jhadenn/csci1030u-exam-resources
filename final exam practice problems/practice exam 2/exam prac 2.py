def is_prime(n, divisor=2):
    if n < 1:
        return False
    elif divisor > n // 2:
        return True
    elif n % divisor == 0:
        return False
    else:
        return is_prime(n, divisor + 1)

def filter_primes(elements):
    if not elements:
        return []
    
    head, *tail = elements
    
    if is_prime(head):
        return [head] + filter_primes(tail)
    else:
        return filter_primes(tail)

if __name__ == '__main__':

    print(f'filter_primes(range(20)): {filter_primes(range(20))}')

    # output:  filter_primes(range(20)): [1, 2, 3, 4, 5, 7, 11, 13, 17, 19]

 

    print(f'filter_primes(range(100,200)): {filter_primes(range(100,200))}')

    # output:  filter_primes(range(100,200)): [101, 103, 107, 109, 113, 127,

    #          131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,

    #          193, 197, 199]
