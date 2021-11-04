def polynomials_multiply(polynom1, polynom2):
    """
    # (2x)*(3x) == 6
    >>> polynomials_multiply([2], [3])
    [6]
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    >>> polynomials_multiply([2,-4],[3,5])
    [6,-2,-20]
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6,0,-8,0,-8,0]

    """
    arguments = 0
    arguments_list = []
    for i in range(len(polynom1)):
        for j in range(len(polynom2)):
            arguments = polynom1[i]*polynom2[j]
            arguments_list.append(arguments)
    
    # def numerals_list(polynom1, polynom2):
    #     numerals = []
    #     numerals_list = []
    #     for i in range(len(polynom1)):
    #         for j in range(len(polynom2)):
    #             arguments = polynom1[i]*polynom2[j]
    #             arguments_list.append(arguments)
    #     numerals_list.append(numerals)

    # numerals = []
    # numerals.append(arguments_list[0])
    # numerals.append(arguments_list[len(arguments_list)-1])
    # arguments_list.pop(0)
    # arguments_list.pop(len(arguments_list)-1)
    
    # step = len(polynom1)
    
    # for i in range(len(arguments_list)):
    #     try:
    #         number = arguments_list[i] + arguments_list[i+step]
    #         arguments_list.pop(i)
    #         arguments_list.pop(i+step)
    #         numerals.append(number)
    #     except:
    #         continue

    # print(numerals)

    # step = len(polynom1)
    # for i in range(len(arguments_list)):
    #     num = arguments_list[i+1] + arguments_list[step]
    #     arguments_list.pop(arguments_list[i+1])
    #     arguments_list.pop()
        

    # counter = 1
    # new_args = []
    # for i in range(len(arguments_list)):
    #     counter += 1
    #     num = arguments_list[i+(len(arguments_list)-counter)] + arguments_list[i+(len(arguments_list)-counter)]
    #     arguments_list.pop(arguments_list[i])
    #     arguments_list.pop(arguments_list[i+1])
    #     new_args.append(num)
    #     print(new_args)

    return arguments_list

print(polynomials_multiply([2,0,-4],[3,0,2,0]))
