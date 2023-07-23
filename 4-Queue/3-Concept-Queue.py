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
    
inputstr = input("input : ").split(',')

queue = Queue()
errorDequeue = 0
errorInput = 0
currentnumber = 0
for i in inputstr:
    letters = ''
    numbers = ''
    for char in i:
        if char.isdigit():
            numbers += char
        else:
            letters += char
    
    if letters == "D":
        for j in range(int(numbers)):
            if queue.isEmpty() == False:
                queue.dequeue()
            elif queue.isEmpty() == True:
                errorDequeue += 1

    elif letters == "E":
        for j in range(int(numbers)):
            if numbers != '':
                queue.enqueue('*'+str(currentnumber))
                currentnumber += 1
            
            else:
                errorInput += 1
    else:
        errorInput += 1

    
    print("Step : " + i)
    if letters == "D":
        print(f"Dequeue : {queue.items}")
    
    elif letters == "E":
        print(f"Enqueue : {queue.items}")
    
    else:
        print(queue.items)
    
    print("Error Dequeue : " + str(errorDequeue))
    print("Error input : " + str(errorInput))
    print("--------------------")