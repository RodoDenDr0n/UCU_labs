# ************************************
# Problem 22
# ************************************
def pattern_number(sequence):
    """
    >>> pattern_number([])
    None
    >>> pattern_number([42])
    None
    >>> pattern_number([1,2])
    None
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    None
    >>> pattern_number([1,2,3,1,2,3])
    ([1,2,3], 2)
    >>> pattern_number([1,2,3,1,2])
    None
    >>> pattern_number([1,2,3,1,2,3,1])
    None
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    None
    """
    i = 1
    type_of_entered = type(sequence)
    len_s = len(sequence)
    sequence = list(sequence)
    cont = True
    while i != len_s:
        repeat = []
        if len_s % i == 0:
            for j in range(i):
                repeat.append(sequence[(int(j * len_s/(i))): (int((j + 1) * len_s/i + 1)) - 1])
        if len(repeat) != 1:
            try:
                len(repeat[0])
            except IndexError:
                i += 1
                continue
            for error_check in range(len(repeat[0]) - 1):
                if repeat[0][0] == repeat[0][error_check + 1]:
                    cont = False
                    i += 1
                    break
            if cont is False:
                cont = True
                continue
            if type_of_entered == list and repeat[0] == repeat[len(repeat) - 1 and\
                repeat[0] == repeat[1]]:
                strr = repeat[0]
                strr = strr, int(len_s / len(strr))
                return strr
            if type_of_entered == str and repeat[0] == repeat[len(repeat) - 1]:
                result = ""
                for in_string in range(len(repeat[0])):
                    result += repeat[0][in_string]
                strr = ('{}').format(result), int(len_s / len(result))
                return strr
        i += 1