"""DYVO INSERT"""
def dyvo_insert(sentence, flag):
    """
    Inserting word "диво" before every word that starts with flag.
    >>> print(dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки"))
    дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті
    """
    words = sentence.split(" ")
    for i in range(len(words)+len(words)):
        try:
            words[i] = words[i].lower()
            if words[i-1] == "диво":
                continue
            if flag in words[i]:
                words.insert(i, "диво")
        except IndexError:
            break

    words_length = len(words)
    for i in range(words_length):
        try:
            if words[i] == "диво":
                words.insert(i, words[i] + words[i+1])
                for j in range(2):
                    words.remove(words[i+1])
                    j += 0
            else:
                continue
        except IndexError:
            break

    words = " ".join(words)

    return words

print(dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті", "ки"))
