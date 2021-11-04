"""CREATE ACRONYM"""
def create_acronym(message):
    """
    >>> print('Hello World!')
    Hello World!
    """
    elements = []
    amount = message.count("\n")
    for i in range(amount):
        element = message[:message.find("\n") + 1]
        elements.append(element)
        message = message.replace(element, "")
    elements.append(message)

    for i in range(len(elements)):
        elements[i] = elements[i].replace("\n", "")

    notify_list = []

    for i in range(len(elements)):
        prior_message = elements[i]
        elements[i] = elements[i].split(" ")

        for j in range(len(elements[i])):
            elements[i].insert(j, (elements[i])[j][0:1])
            elements[i].remove((elements[i])[j+1])

        elements[i] = "".join(elements[i])
        elements[i] = elements[i].upper()

        notify = f"{elements[i]} - {prior_message}"
        notify_list.append(notify)

    notify_list = "\n".join(notify_list)

    return print(notify_list)

create_acronym('random access memory\nAs soon As possible')
