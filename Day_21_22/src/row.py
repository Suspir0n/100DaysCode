# This method to make the dequeuing of row.
def dequeue(elements, last):
    if last == -1:
        return 'The Queue it is empty!', False
    reposition_elements(elements, last)
    return True


# This method to make the queuing of row.
def queue(value, elements, last):
    if last == len(elements) - 1:
        return 'The Queue it is full!', False
    last += 1
    elements.append(value)
    elements = rearrange_elements(elements, last)
    return elements


def rearrange_elements(elements, last):
    elements_secondary = elements[:]
    """for c in range(0, len(elements)):
        dequeue(elements, last)"""
    for value in elements:
        if value[1] > 65:
            elements.append(value)
    for value in elements:
        if value[1] < 65:
            elements.append(value)
    return elements


# This method to make the repositing of elements until the scorer reaches the last.
def reposition_elements(elements, last):
    pont = 0
    while pont != last:
        elements[pont] = elements[pont + 1]
        pont += 1
    elements.pop(last)
    last -= 1