def convert_to_column(s):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print_column("Revenge is a dish that tastes best when served cold.")
    revenge
    is
    a
    dish
    that
    tastes
    best
    when
    served
    cold
    >>> print_column("Never hate your enemies. It affects your judgment.")
    never
    hate
    your
    enemies
    it
    affects
    your
    judgment
    >>> print_column(2015)
    """
    if type(s) == str:
        s = s.replace(",", "")
        s = s.replace(".", "")
        words = s.split(" ")
        for i in range(len(words)):
            print(words[i].lower())
    else:
        print()

convert_to_column(1)
