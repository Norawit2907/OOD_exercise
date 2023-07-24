class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peak(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)

inputstr = input("input str: ").split(',')
stack = Stack()
for curplate in inputstr:
    curweight = int(curplate.split()[0])
    curfreq = int(curplate.split()[1])

    while stack.isEmpty() == False and int(stack.peak().split()[0]) < int(curweight):
        print(f"{stack.peak().split()[1]}")
        stack.pop()
        
    stack.push(curplate)

