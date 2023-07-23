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

inputstr = input("Enter Input : ").split(',')
queue = Queue()
for i in inputstr:
    if i.split()[0] == 'E':
        queue.enqueue(i.split()[1])
        print(queue.size())

    elif i.split()[0] == 'D' and queue.isEmpty() == False:
        print(queue.first(), queue.items.index(queue.first()))
        queue.dequeue()
    
    elif i.split()[0] == 'D' and queue.isEmpty() == True:
        print("-1")

if queue.isEmpty() == False:
    for i in queue.items:
        print(i, end = ' ')

else:
    print("Empty")