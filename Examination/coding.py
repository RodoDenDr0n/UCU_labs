def read_crossword(path):
    """
    This function returns tuple with letter and its coordinates
    """
    coordinates_lst = []
    with open(path, "r", encoding = "utf-8") as file:

        letters_lst = []
        for line in file:
            letters_lst.append(line[0])
            coordinates = line[1:]
            coordinates_lst.append(coordinates.rstrip())
        print(letters_lst)

        new_coord_lst = []
        for i in range(len(coordinates_lst)):
            sliced_coord = 0
            times = int(len(coordinates_lst[i])/2)
            coord_lst = []
            for j in range(times):
                coord_tuple = []                
                sliced_coord = coordinates_lst[i][0:2]
                coord_tuple.append(sliced_coord[0])
                coord_tuple.append(sliced_coord[1])

                coord_tuple = tuple(coord_tuple)
                coord_lst.append(coord_tuple)

            new_coord_lst.append(coord_lst)

        lst_lst = zip(new_coord_lst)
        print(new_coord_lst)

# def find_words(crossword, length):

read_crossword("crossword_1_1.txt")
