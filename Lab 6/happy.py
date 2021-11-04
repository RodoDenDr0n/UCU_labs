"""HAPPY"""

def happy_number(number: int) -> bool:
    """
    This function evaluetes happy number
    >>> happy_number(123)
    False
    """
    number = str(number).zfill(8)
    sum1 = []
    sum2 = []
    for i in range(4):
        sum1.append(int(number[i]))
        sum2.append(int(number[i+4]))
    
    sum1 = sum(sum1)
    sum2 = sum(sum2)

    if sum1 == sum2:
        boolean = True
    else:
        boolean = False
    
    return boolean

def count_happy_numbers(numeral: int) -> bool:
    """
    This function returns the amount of happy numbers
    >>> count_happy_numbers(22000)
    14
    """
    return len(happy_numbers(0, numeral))

def happy_numbers(first_ticket: int, last_ticket: int) -> list:
    """
    This function returns the list with happy numbers
    >>> happy_numbers(11000, 11000)
    []
    """
    happy_numbers_lst = []
    value = 0
    for i in range(first_ticket, last_ticket):
        value = happy_number(first_ticket)
        if value:
            happy_numbers_lst.append(first_ticket)
        first_ticket += 1
    return happy_numbers_lst

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
