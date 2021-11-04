"""TOTAL OCCURRENCES"""
def total_occurrences(word1, word2, flag):
    """
    (str, str, str) -> int
    Precondition: len(flag) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    result = 0
    word1_length = len(word1)
    for i in range(word1_length):
        if word1[i] == flag:
            result += 1

    word2_length = len(word2)
    for i in range(word2_length):
        if word2[i] == flag:
            result += 1

    return result

print(total_occurrences('green', 'purple', 'b'))
