class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        self.items.pop()
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    
    def top(self):
        return self.items[-1]

strin = input("Enter Input : ").split(',')
s = Stack()

for i in strin:
    w = i.split()[0]

    while s.isEmpty() == False and int(s.top().split()[0]) < int(w):
        print(s.top().split()[1])
        s.pop()
    
    s.items.append(i)