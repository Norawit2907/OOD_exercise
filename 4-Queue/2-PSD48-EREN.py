class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def first(self):
        return self.items[0]

    def last(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

normalLine = Queue()
specialLine = Queue()

inputstr = input('Enter Input : ').split(',')


for i in inputstr:
    if i.split()[0] == 'EN':
        normalLine.enqueue(i.split()[1])
    
    elif i.split()[0] == 'ES':
        specialLine.enqueue(i.split()[1])
    
    elif i.split()[0] == 'D':
        if specialLine.isEmpty() == False:
            print(specialLine.first())
            specialLine.dequeue()
        
        elif specialLine.isEmpty() == True and normalLine.isEmpty() == False:
            print(normalLine.first())
            normalLine.dequeue()
        
        elif specialLine.isEmpty() == True and normalLine.isEmpty() == True:
            print("Empty")