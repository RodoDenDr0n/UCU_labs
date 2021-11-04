def find_intersection(intersection1, intersection2 = 0):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    b
    >>> find_intersection("aZAbc", "zzYYxp")
    z
    >>> find_intersection("sfdfsdf", 2015)

    """
    if type(intersection1) == str and type(intersection2) == str:
        letters1 = []
        letters2 = []

        for i in range(len(intersection1)):
            letters1.append(intersection1[i].lower())

        for i in range(len(intersection2)):
            letters2.append(intersection2[i].lower())

        for i in range(len(letters1)):
            if letters1[i] in letters2:
                print(letters1[i])
                letters1.remove(letters1[i])
                letters1.append("")
    else:
        print()

find_intersection("sfdfsdf", 2015)
