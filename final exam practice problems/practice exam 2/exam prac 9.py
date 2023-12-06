import math

def get_powers_of_2(n) :
    powers = []

    if n == 0 :
        powers.append(math.pow(2,0))
        return powers
    
    elif n < 0 :
        return powers 
    else :
        powers.append(math.pow(2,n))
        return get_powers_of_2(n-1), powers


if __name__ == '__main__':
    
    print(f'2^0 .. 2^4: {get_powers_of_2(4)}')

    # output: [1, 2, 4, 8, 16]

 

    print(f'2^0 .. 2^10: {get_powers_of_2(10)}')

    # output: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]