def compare_char(ch1, ch2):
    """
    (str, str) -> bool
    Compare two char by their position in alphabet. Return True if letter
    ch2 appears before ch1 and False otherwise. If neither ch1 nor ch2 are
    letters function should return None.

    >>> compare_char('a', 'z')
    False
    >>> compare_char('c', 'B')
    True
    >>> compare_char('d', 'ad')

    >>> compare_char('2', 2)

    """

    try:
        if type(ch1) == str:
            if ch1.isupper():
                ch1 = ord(ch1) - 64
            elif ch1.islower():
                ch1 = ord(ch1) - 96

        if type(ch2) == str:
            if ch2.isupper():
                ch2 = ord(ch2) - 64
            elif ch2.islower():
                ch2 = ord(ch2) - 96        

    except:
        print()

    try:
        if ch1 < ch2:
            print(False)
            
        if ch1 > ch2:
            print(True)
    except:
        print()

compare_char(2, "2")
