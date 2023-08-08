class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:

    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
 
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        newNode.previous = self.tail
        self.tail = newNode


    def addHead(self, item):
        newNode = Node(item)
        if self.head == None:
            self.head = self.tail = newNode
            return
        self.head.previous = newNode
        newNode.next = self.head
        self.head = newNode

    def insert(self, pos, item):
        lenght = self.size()
        if pos >= lenght:
            self.append(item)
            return
        elif pos <= -lenght:
            self.addHead(item)
            return
        
        newNode = Node(item)
        p = -lenght
        temp = self.head
        while p != pos:
            temp = temp.next
            if temp == None:
                temp = self.head
            p += 1
        temp.previous.next = newNode
        newNode.next = temp
        newNode.previous = temp.previous
        temp.previous = newNode

    def search(self, item):
        return "Not Found" if self.index(item) == -1 else "Found"

    def index(self, item):
        temp = self.head
        i = 0
        while temp != None:
            if temp.value == item:
                return i
            temp = temp.next
            i += 1
        return -1

    def size(self):
        temp = self.head
        s = 0
        while temp != None:
            s += 1
            temp = temp.next
        return s

    def pop(self, pos):
        lenght = self.size()
        if not (-lenght <= pos < lenght):
            return "Out of Range"
            
        temp = self.head
        p = -lenght
        while p != pos:
            p += 1
            temp = temp.next
            if temp == None:
                temp = self.head
        if temp == self.head:
            self.head = self.head.next
            temp.next = None
            if self.head != None:
                self.head.previous = None
            return "Success"
        elif temp == self.tail:
            self.tail = self.tail.previous
            self.tail.next = None
            temp.previous = None
            return "Success"
        
        temp.previous.next = temp.next
        temp.next.previous = temp.previous
        return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())