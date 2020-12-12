# This method to make the dequeuing of row.
def Dequeue(elements, last):
    if last == -1:
        return 'The Queue it is empty!', False
    repositionTheElements(elements, last)
    return True
       
# This method to make the queuing of row.
def Queue(value, elements, last):
    if last == len(elements) - 1:
        return 'The Queue it is full!', False
    last += 1
    elements[last] = value
    return True

# This method to make the repositing of elements until the scorer reaches the last.    
def repositionTheElements(elements, last):
    pont = 0
    while pont != last:
        elements[pont] = elements[pont + 1]
        pont += 1
    elements[last] = ''
    last -= 1
