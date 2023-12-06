def towers_of_hanoi(n, start, end, temp):
    if n < 1:
        return 0

    count = towers_of_hanoi(n - 1, start, temp, end)
    count += 1
    print('Move 1 ring from', start, 'to', end) # count this line only 


    count += towers_of_hanoi(n - 1, temp, end, start)
    count += 1
    return count

print(towers_of_hanoi(1,1,2,3))
print(towers_of_hanoi(2,1,2,3))
print(towers_of_hanoi(3,1,2,3))