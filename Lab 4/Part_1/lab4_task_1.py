'''laboratorna'''
def get_number():
    '''
    Returns the number of student
    '''
    number = 99
    return number


# Complete all of the following functions. Currently they all just
# 'pass' rather than explicitly return value, which means that they
# implicitly return None. They all include doctests, which you can
# test by running this file.

# The doctests are just examples. Feel free to add your own doctests.

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


# ****************************************
# Problem 2
# ****************************************
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
        if isinstance(ch1, str):
            if ch1.isupper():
                ch1 = ord(ch1) - 64
            elif ch1.islower():
                ch1 = ord(ch1) - 96

        if isinstance(ch2, str):
            if ch2.isupper():
                ch2 = ord(ch2) - 64
            elif ch2.islower():
                ch2 = ord(ch2) - 96

    except:
        return None

    try:
        if ch1 < ch2:
            return False

        if ch1 > ch2:
            return True
    except:
        return None

# ****************************************
# Problem 3
# ****************************************
def compare_str(textline1, textline2):
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
        if len(textline1) != len(textline2):
            return
    except:
        return

    try:
        if isinstance(textline1, str) and isinstance(textline1, str):
            textline1_len = len(textline1)
            for i in range(textline1_len):
                if textline1[i].isupper():
                    size1 += 1

            textline2_len = len(textline2)
            for i in range(textline2_len):
                if textline2[i].isupper():
                    size2 += 1

            if size1 > size2:
                return True
            else:
                return False
    except:
        return

# ****************************************
# Problem 6
# ****************************************
def remove_spaces(textline):
    """
    str -> str
    Remove all additional spaces in string and return a new string without additional spaces.
    If argument is not a string function should return None.

    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World

    """
    space = " "
    try:
        words = textline.split(" ")
    except:
        return None
    num = words.count("")
    for i in range(num):
        words.remove("")
        i += 0
    return space.join(words)

# ****************************************
# Problem 7
# ****************************************
def convert_to_column(textline):
    """
    str -> str
    Convert string to a column of words.
    If argument is not a string function should return None.

    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    """
    if isinstance(textline, str):
        textline = textline.replace(",", "")
        textline = textline.replace(".", "")
        words = textline.split(" ")
        words_len = len(words)
        variable = ""
        for i in range(words_len):
            if i+1 == words_len:
                variable += words[i].lower()
                break
            variable += words[i].lower() + "\n"
        return variable
    else:
        return None

# ****************************************
# Problem 8
# ****************************************
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
    if isinstance(enter_string, str):
        sentences_number = enter_string.count(".")
        return sentences_number
    else:
        return None

# ****************************************
# Problem 15
# ****************************************
def find_intersection(intersection1, intersection2 = 0):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    'b'
    >>> find_intersection("aZAbc", "zzYYxp")
    'z'
    >>> find_intersection("sfdfsdf", 2015)

    """
    if isinstance(intersection1, str) and isinstance(intersection2, str):
        letters1 = []
        letters2 = []

        len_intersection1 = len(intersection1)
        for i in range(len_intersection1):
            letters1.append(intersection1[i].lower())

        len_intersection2 = len(intersection2)
        for i in range(len_intersection2):
            letters2.append(intersection2[i].lower())
        
        variable = ""
        for i in range(len_intersection1):
            if letters1[i] in letters2:
                variable += letters1[i]
                # print(letters1[i])
                letters1.remove(letters1[i])
                letters1.append("")
        return variable
    else:
        return None

# ****************************************
# Problem 16
# ****************************************
def find_union(union1, union2):
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)

    """
    if isinstance(union1, str) and isinstance(union2, str):
        letters = union1 + union2
        len_letters = len(letters)
        union = []
        for i in range(len_letters):
            if letters[i] not in union:
                union.append(letters[i])
        union.sort()
        space = ""
        return space.join(union)
    else:
        return None

# ****************************************
# Problem 20
# ****************************************
def polynomial_eval(coefficients, value):
    """
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    """
    value_list = []
    add_numbers = 0
    len_coefficients = len(coefficients)
    for i in range(len_coefficients):
        value_list.append(value)
        value_list[i] = value_list[i]**(len(coefficients)-(i+1))
        value_list[i] = value_list[i] * coefficients[i]

    for i in range(len(value_list)):
        add_numbers += value_list[i]

    return add_numbers
# ****************************************
# Problem 21
# ****************************************
def polynomials_multiply(polynom1, polynom2):
    """
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World

    """

    return True


# ****************************************
# Problem 22
# ****************************************
def pattern_number(sequence):
    """
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    >>> print('Hello World')
    Hello World
    """

    return True
# ****************************************
# Problem 25
# ****************************************
def happy_number(number):
    """
    >>> happy_number(32)
    True
    >>> happy_number(33)
    False
    """
    number = list(str(number))
    len_number = len(number)
    for i in range(100):
        numeral = 0
        i += 0
        for j in range(len_number):
            numeral += int(number[j])**2
        number = list(str(numeral))
        if numeral == 1:
            return True
    return False

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
