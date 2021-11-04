'''
Lab 6 4
'''
from urllib import request
from typing import Counter, List

def read_input_file(url: str, number = 77) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77

    Return list of strings lists from url

    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць \
О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    list_web = []
    count = 0
    with request.urlopen(url) as webpage:
        for line in webpage:
            if count >= number or number > 77:
                return list_web
            line = line.strip()
            line = line.decode('utf-8')
            line = line.split("\t")
            if line[0] == "#":
                continue
            if line[0].isdigit():
                sub_list = []
                sub_list.append(line[0])
                sub_list.append(line[1])
                if line[2] == "До наказу":
                    sub_list.append("+")
                else:
                    sub_list.append("-")
                sub_list.append(line[3])
            if "Середній" in line[0]:
                sub_list.append(line[0][34:])
                list_web.append(sub_list)
                count += 1
    return list_web

def write_csv_file(url: str):
    '''
    The function writes csv file
    '''
    file = open("total.csv", "w")
    list_w = read_input_file(url)
    file.write("№,ПІБ,Д,Заг.бал,С.б.док.осв." + "\n")
    for i in range(77):
        for j in range(len(list_w[i])):
            if j + 1 == len(list_w[i]):
                file.write(list_w[i][j])
                continue
            file.write(list_w[i][j])
            file.write(",")
        file.write("\n")
    file.close()
