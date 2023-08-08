class Stack():
    def __init__(self):
        self.item = []
    
    def push(self, value):
        self.item.append(value)
    
    def pop(self):
        return self.item.pop()

    def peek(self):
        return self.item[-1]

    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

inputstr = input("ENTER : ").split(',')
s = Stack()

for curplate in inputstr:
    weight = int(curplate.split()[0])
    freq = int(curplate.split()[1])
    while s.isEmpty() == False and int(s.peek().split()[0]) <= weight:
        print(s.peek().split()[1])
        s.pop()
    s.push(curplate)