"""SORT SONGS"""

# song_titles = ['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд']
# length_songs = ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21']

from typing import List, Tuple, Callable

def song_length(tuple_lst: Tuple[str]) -> int:
    """
    This function returns a song_length sort key
    >>> print("The working doctest")
    The working doctest
    """
    return tuple_lst[1]

def title_length(tuple_lst: Tuple[str]) -> int:
    """
    This function returns a title_length sort key
    >>> print("The working doctest")
    The working doctest
    """
    return len(tuple_lst[0])

def last_word(tuple_lst: Tuple[str]) -> str:
    """
    This function returns a last_word sort key
    >>> print("The working doctest")
    The working doctest
    """
    return tuple_lst[0].split(" ")[-1]

def sort_songs(song_titles: List[str], length_songs: List[str], key) -> List[tuple]:
    """
    This function returns a sort_songs sort key
    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'], ['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21'], last_word)
    [('африка', '4.24'), ('відпусти', '3.52'), ('той день', '3.58'), ('етюд', '2.21'), ('кавачай', '4.39'), ('мало мені', '5.06'), ('коли тебе нема', '3.17'), ('поясни', '3.39'), ('сосни', '4.31'), ('фіалки', '3.43'), ('янанебібув', '3.19')]
    """
    if len(song_titles) != len(length_songs):
        return None
    else:
        tuple_lst = []
        for i in range(len(song_titles)):
            tuple_lst.append((song_titles[i].lower(), length_songs[i]))
    return sorted(tuple_lst, key = key)

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
