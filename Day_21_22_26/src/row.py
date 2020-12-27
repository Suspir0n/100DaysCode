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
    if value[1] > 65:
         elements_secondary = rearrange_elements(value, elements, last)
         desinfileiramento_total(elements, last)
         elements.append(elements_secondary[:])
    return elements


def desinfileiramento_total(elements, last):
    if last == len(elements):
        for c in range(0, last):
            last -= 1
            dequeue(elements, last)
    else:
        last = len(elements)
        for c in range(0, last):
            last -= 1
            dequeue(elements, last)
    if last == -1:
        dequeue(elements, last=0)


def rearrange_elements(value, elements, last):
    elements_secondary = list()
    elements_secondary.append(value)
    if last == len(elements):
        for c in range(0, last):
            elements_secondary.append(elements[c])
    else:
        last = len(elements)
        for c in range(0, last):
            elements_secondary.append(elements[c])
    return elements_secondary


# This method to make the repositing of elements until the scorer reaches the last.
def reposition_elements(elements, last):
    pont = 0
    while pont != last:
        elements[pont] = elements[pont + 1]
        pont += 1
    last -= 1
    elements.pop(last)
    print(elements)
    print(len(elements))
    print(last)