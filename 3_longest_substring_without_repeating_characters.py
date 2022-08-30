def length_of_longest_substring(s):
    i = j = 0
    longest_length = 0
    char_last_loc = dict()

    while j < len(s):
        if char_last_loc.get(s[j], -1) >= i:
            longest_length = max(longest_length, j - i)
            i = char_last_loc[s[j]] + 1

        char_last_loc[s[j]] = j
        j += 1

    return max(longest_length, j - i)
