import random
from typing import List
import time



def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    letters_generator = [[chr(random.randint(65, 90)) for i in range(3)] for i in range(3)]
    return letters_generator



def get_words(file: str, letters_generator: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    central_letter = letters_generator[1][1].lower()
    letters_lst = [letters_generator[i][j].lower() for i in range(len(letters_generator)) for j in range(len(letters_generator[i]))]

    game_dictionary = []
    with open("en.txt", "r", encoding = 'utf-8') as dictionary:
        lines = dictionary.readlines()[3:]
        for i in range(len(lines)):
            if len(lines[i].rstrip()) >= 4:
                if central_letter in lines[i]:
                    game_dictionary.append(lines[i].rstrip().lower())
    
    print(game_dictionary)

    letters_lst = "".join(letters_lst)

    new_game_dictionary = []
    for i in range(len(game_dictionary)):
        for j in range(len(game_dictionary[i])):
            if game_dictionary[i][j] not in letters_lst:
                break
            else:
                new_game_dictionary.append(game_dictionary[i])

    return None



def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    user_words = []
    while True:
        user_input = input()
        if ord(user_input) == 4:
            break
        else:
            user_words.append(user_input)
    return user_words
    pass



def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass



def results():
    pass



print(get_words(0, generate_grid()))
print(generate_grid())