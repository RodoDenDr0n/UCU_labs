def polynomial_eval(coefficients, value):
    """
    # f(x) = 2x^3 + 3x^2 + 4, f(4) = 180
    >>> polynomial_eval([2,3,0,4], 4)
    180
    # f(x) = 6, f(42) = 6
    >>> polynomial_eval([6], 42)
    6
    # f(x) = 6x^2 -2x - 20, f(-1) = -12
    >>> polynomial_eval([6,-2,-20], -1)
    -12
    # f(x) = 6x^5-8x^3-8x, f(2) = 112, f(1) = -10, f(0) = 0
    >>> polynomial_eval([6,0,-8,0,-8,0], 2)
    112
    >>> polynomial_eval([6,0,-8,0,-8,0], 1)
    -10
    >>> polynomial_eval([6,0,-8,0,-8,0], 0)
    0
    """
    value_list = []
    x = value
    add_numbers = 0
    for i in range(len(coefficients)):
        value_list.append(x)
        value_list[i] = value_list[i]**(len(coefficients)-(i+1))
        value_list[i] = value_list[i] * coefficients[i]

    for i in range(len(value_list)):
        add_numbers += value_list[i]

    return add_numbers

print(polynomial_eval([6,0,-8,0,-8,0], 0))
