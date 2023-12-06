def find_longest_string_with_e(strings) :
    strings_with_e = [word for word in strings if 'e' in word]
    longest_string = ""

    for string in strings_with_e :
        if len(string) > len(longest_string) :
            longest_string = string

    return longest_string

print(find_longest_string_with_e(['always', 'the', 'longest', 'string', 'is', 'best', 'applied', 'to', 'hunting', 'ducks', 'everywhere']))

print(find_longest_string_with_e(['act', 'now', 'to', 'invite', 'a', 'duck', 'to', 'be', 'your', 'best', 'bud']))