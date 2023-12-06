def are_equal(list1, list2):
    set1= set(list1)
    set2 = set(list2)

    return set1 == set2 
if __name__ == '__main__':

    print(f'are_equal([1,2,3], [3,1,2]): {are_equal([1,2,3], [3,1,2])}')

    # are_equal([1,2,3], [3,1,2]): True

 

    print(f'are_equal([1,2,3], [4,1,3]): {are_equal([1,2,3], [4,1,3])}')

    # are_equal([1,2,3], [4,1,3]): False

 

    print(f'are_equal([1,8,15], [1,15,8]): {are_equal([1,8,15], [1,15,8])}')

    # are_equal([1,8,15], [1,15,8]): True