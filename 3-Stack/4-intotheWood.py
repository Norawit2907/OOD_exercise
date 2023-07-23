class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    
    def top(self):
        return self.items[-1]

stack = Stack()


inp = input('Enter Input : ').split(',')

for tree in inp:
    if tree.split()[0] == 'A':
        
        while stack.isEmpty() == False and int(tree.split()[1]) >= int(stack.top()):
            #print(tree.split()[1], stack.top())  
            stack.pop()
            
        stack.push(int(tree.split()[1]))
        #print(stack.items)

    elif tree.split()[0] == 'B':
        #print(stack.items)
        print(stack.size())
        
        
    
    
    