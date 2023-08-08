class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    
class Linkedlist():
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.previous = self.tail
        self.tail.next = newNode
        self.tail = newNode
    
    def isEmpty(self):
        return self.head == None

    def __str__(self):
            if self.isEmpty():
                return "Empty"
            cur, s = self.head, str(self.head.data) + " "
            while cur.next != None:
                s += str(cur.next.data) + " "
                cur = cur.next
            return s
    
    def reverse(self):
        temp, s = self.tail, str(self.tail.data) + " "
        while temp.previous != None:
            s += str(temp.previous.data) + " "
            temp = temp.previous
        return s

inputstr = input("Enter Input (L1,L2) : ").split()

list1 = Linkedlist()
list2 = Linkedlist()


for i in inputstr[0].split('->'):
    if i not in '->':
        list1.append(i)
for i in inputstr[1].split('->'):
    if i not in '->':
        list2.append(i)

print(f"L1    : {list1}")
print(f"L2    : {list2}")
print(f"Merge : {list1}{list2.reverse()}")