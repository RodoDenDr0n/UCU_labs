def number_of_sentences(enter_string):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """
    if type(enter_string) == str:
        sentences_number = enter_string.count(".")
        print(sentences_number)
    else:
        print()

number_of_sentences()
