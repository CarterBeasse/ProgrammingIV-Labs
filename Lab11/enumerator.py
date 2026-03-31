class Enumerate():
    def __init__(self, obj):
        self.obj = obj
        self.count = -1
    def __iter__(self):
        self.obj = iter(self.obj)
        self.count += 1
        return self
    def __next__(self):
        self.count += 1
        return self.count,next(self.obj)

for i in Enumerate([1, 5, 12]):
    print(i)

