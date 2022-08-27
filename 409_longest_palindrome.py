from collections import Counter


def longest_palindrome(s):
    s = Counter(s)
    first_odd = True

    char_num = 0
    for char in s:
        if s[char] % 2 == 1:
            if first_odd:
                first_odd = False
            else:
                s[char] -= 1

        char_num += s[char]

    return char_num
