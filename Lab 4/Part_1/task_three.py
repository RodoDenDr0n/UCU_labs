def compare_str(s1, s2):
    """
    (str, str) -> bool
    Compare two srings lexicographicly. Return True if string s1 is larger
    than string s2 and False otherwise. If arguments aren't string or function
    have different length function should return None.

    >>> compare_str('abc', 'Abd')
    False
    >>> compare_str('zaD', 'zab')
    True
    >>> compare_str('zaD', 'Zad')
    False
    >>> compare_str('aaa', 'aaaaa')

    >>> compare_str('2015', 2015)

    """
    size1 = 0
    size2 = 0

    try:
        if len(s1) != len(s2):
            print()
            exit()
    except:
        print()

    try:
        if type(s1) == str and type(s2) == str:
            for i in range(len(s1)):
                if s1[i].isupper():
                    size1 += 1
                    
            for i in range(len(s2)):
                if s2[i].isupper():
                    size2 += 1
                
            if size1 > size2:
                print(True)
            else:
                print(False)
    except:
        print()

compare_str('zaDf', 2015)
