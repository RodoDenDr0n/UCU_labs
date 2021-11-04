def happy_number(n):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """
    n = list(str(n))
    for i in range(100):       
        numeral = 0
        for j in range(len(n)):
            numeral += int(n[j])**2
        n = list(str(numeral))
        if numeral == 1:
            return print(True)
        
    return print(False)

happy_number(33)