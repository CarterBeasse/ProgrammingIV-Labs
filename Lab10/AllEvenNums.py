class Evens:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.tracker = start
    # ITER FUNCTIONS-----------------------------------------------------------------
    def __iter__(self):
        self.tracker = self.start #Initialize state tracker
        return self # return the iterator(self)
    # NEXT FUNCTION------------------------------------------------------------------
    def __next__(self):
        if self.tracker >= self.stop:
            raise StopIteration
        result = self.tracker
        self.tracker += 2
        return result
evens = Evens(0, 100)
for i in evens:
    print(i)
for i in evens:
    print(i)
