def max_of_divisible_by_5(numbers) :
    numbers_divisble_by_5 = [num for num in numbers if num % 5 == 0]
    largest = 0
    for number in numbers_divisble_by_5 :
        if number > largest :
            largest = number

    return largest

print(max_of_divisible_by_5([21,3,12,8,35,9,18,10,1,15,19,5,25]))


print(max_of_divisible_by_5([7,11,12,4,1,10,9,2,6]))
