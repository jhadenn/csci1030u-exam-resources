def sum_of_squares(min, max) :
    sum = 0 
    for i in range(min, max + 1) :
        sum += i * i

    return sum



if __name__ == '__main__':

    print(f'sum_of_squares(1,10): {sum_of_squares(1,10)}')

    # output: sum_of_squares(1,10): 385

 

    print(f'sum_of_squares(1,5): {sum_of_squares(1,5)}')

    # output: sum_of_squares(1,5): 55