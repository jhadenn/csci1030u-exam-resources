def greedy_change(amount, denoms) :
    denoms.sort(reverse=True)

    change_count = {}

    for denom in denoms :
        num_denoms = amount // denom

        if num_denoms > 0 :
            change_count[denom] = num_denoms

        amount -= num_denoms * denom

    return change_count

if __name__ == '__main__':

    denoms = [1,2,5,10,20,50]

 

    print(f'greedy_change(174, {denoms}) == {greedy_change(174, denoms)}')

    # output: greedy_change(174, [1,2,5,10,20,50]) == [50, 50, 50, 20, 2, 2]

 

    print(f'greedy_change(99, {denoms}) == {greedy_change(99, denoms)}')

    # output: greedy_change(99, [1,2,5,10,20,50]) == [50, 20, 20, 5, 2, 2]