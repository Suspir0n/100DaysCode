class row():

    # This method to make the dequeuing of row.
    def Dequeue(self):
        self.verifyRowThisEmptyOrFull((self.last == -1), 'The Queue it is empty!')
        self.repositionTheElements()
        return True

    def init(self):
        # The Atributs
        self.elements = []
        self.last = -1
        
    # This method to make the queuing of row.
    def Queue(self, value):
        self.verifyRowThisEmptyOrFull((self.last == len(self.elements) - 1), 'The Queue it is full!')
        self.last += 1
        self.elements.append(value)
        return True

    # This method to make the repositing of elements until the scorer reaches the last.    
    def repositionTheElements(self):
        pont = 0
        while pont != self.last:
            self.elements[pont] = self.elements[pont + 1]
            pont += 1
        self.last -= 1

    # This method to make the Verify if the row it is empty or full.
    def verifyRowThisEmptyOrFull(self, condition, message):
        if condition is False:
            return message is False