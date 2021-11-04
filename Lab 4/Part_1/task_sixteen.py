def find_union(union1, union2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    abc
    >>> find_union("aZAbc", "zzYYxp")
    AYZabcpxz
    >>> find_union("sfdfsdf", 2015)

    """
    if type(union1) == str and type(union2) == str:
        letters = union1 + union2
        union = []
        for i in range(len(letters)):
            if letters[i] not in union:
                union.append(letters[i])
        
        union.sort()
        space = " "
        print(space.join(union))
    else:
        print()

find_union("sfdfsdf", 2015)
