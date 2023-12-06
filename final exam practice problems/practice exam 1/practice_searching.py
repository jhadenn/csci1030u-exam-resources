# practice_searching.py

class NoMatchFoundException(Exception):
    pass

def has_no_repeated_letter(string):
    # Helper function to check if a character is repeated in the given string
    def is_repeated(char, index):
        if index == len(string):
            return True
        if string[index] == char:
            return False
        return is_repeated(char, index + 1)

    # Base case: an empty string has no repeated letters
    if not string:
        return True

    # Check if the first character is repeated
    if not is_repeated(string[0], 1):  # Fix: Start checking from index 1
        return False

    # Recursively check the rest of the string
    return has_no_repeated_letter(string[1:])

def get_longest_matching_substring(string, check_match):
    # Helper function to find the longest matching substring using brute force
    def find_longest_substring(start_index):
        for end_index in range(len(string), start_index, -1):
            substring = string[start_index:end_index]
            if check_match(substring):
                return substring
        return None

    # Iterate through all possible starting indices
    for i in range(len(string)):
        longest_substring = find_longest_substring(i)
        if longest_substring:
            return longest_substring

    # If no match is found, raise the custom exception
    raise NoMatchFoundException("No matching substring found")

# Test code
print('ablewasiereisawelba:', has_no_repeated_letter('ablewasiereisawelba'))
# expected output: ablewasiereisawelba: False

print('abcd:', has_no_repeated_letter('abcd'))
# expected output: abcd: True

print('longest with no repeated letter:', get_longest_matching_substring('i saw abba, but ablewasiereisawelba by the racecar', has_no_repeated_letter))
# expected output: longest with no repeated letter: ut ablew
