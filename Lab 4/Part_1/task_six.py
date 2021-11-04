def remove_spaces(s):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> remove_spaces("I'll make     him an     offer he can't refuse.")
    I'll make him an offer he can't refuse.
    >>> remove_spaces("Great    men     are    not born great, they grow great...")
    Great men are not born great, they grow great...
    >>> remove_spaces(2015)

    """
    space = " "
    words = s.split(" ")
    num = words.count("")
    for i in range(num):
        words.remove("")
    print(space.join(words))
    