def get_position(ch):
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
        if type(ch) == str:
            if ch.isupper():
                print(ord(ch) - 64)
            else:
                print(ord(ch) - 96)
    except:
        print()

get_position("")
