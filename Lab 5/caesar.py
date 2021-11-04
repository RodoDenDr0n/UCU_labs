"""CAESAR ENCODE"""
def caesar_encode(message, key):
    """
    >>> caesar_encode("hello", 1)
    ifmmp
    """
    message = message.lower()
    message = list(message)

    if key >= 26:
        key = key % 26

    for i in range(len(message)):
        if message[i] == " ":
            continue
        if ord(message[i]) < 120:
            if ord(message[i]) + key >= 123:
                message[i] = chr(ord(message[i]) - 26 + key)
            else:
                message[i] = chr(ord(message[i]) + key)
        else:
            message[i] = chr(ord(message[i]) - 26 + key)

    message = "".join(message)

    return message

print(caesar_encode("hello", 1))

def caesar_decode(message, key):
    """
    >>> caesar_decode("ifmmp", 1)
    hello
    """
    message = message.lower()
    message = list(message)

    if key >= 26:
        key = key % 26

    for i in range(len(message)):
        if message[i] == " ":
            continue
        if ord(message[i]) > 99:
            if ord(message[i]) - key < 96:
                message[i] = chr(ord(message[i]) + 26 - key)
            else:
                message[i] = chr(ord(message[i]) - key)
        else:
            message[i] = chr(ord(message[i]) + 26 - key)
            if message[i] == "{":
                message[i] = "a"

    message = "".join(message)

    return message

print(caesar_decode("ifmmp", 1))
