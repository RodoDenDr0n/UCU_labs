# ****************************************
# Problem 1
# ****************************************
def get_position(letter):
    """
    str -> int
    Return positon of letter in alphabet. If argument is not a letter function
    should return None.

    >>> get_position('A')
    1
    >>> get_position('z')
    26
    >>> get_position('Dj')

    """
    try:
        if isinstance(letter, str):
            if letter.isupper():
                return ord(letter) - 64
            else:
                return ord(letter) - 96
    except:
        return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())