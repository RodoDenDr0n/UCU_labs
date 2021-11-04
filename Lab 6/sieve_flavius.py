"""SIEVE FLAVIUS"""

from typing import List

def sieve_flavius(numeral: int) -> List[int]:
    """
    This function returns a list of lucky numbers in certain range n
    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 27, 31, 33, 37, 43, 45, 49, 51, 55, 57, 63, 67, 69, 73, 75, 79, 85, 87, 91, 93, 97, 99]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    """
    values = []
    for i in range(1, numeral, 2):
        values.append(i)
        i += 1

    third_values = []
    for i in range(2, len(values), 3):
        third_values.append(values[i])

    for i in range(len(third_values)):
        if third_values[i] in values:
            values.remove(third_values[i])

    seventh_values = []
    for i in range(6, len(values), 7):
        seventh_values.append(values[i])

    for i in range(len(seventh_values)):
        if seventh_values[i] in values:
            values.remove(seventh_values[i])

    return values

print(sieve_flavius(100))

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
