class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self, headnode= None):
        self.head = headnode
        self.tail = self.head
    
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return

        self.tail.next = newNode
        self.tail = newNode
    
    def isEmpty(self):
        return self.head == None

    def search(self, data):
        cur = self.head
        while cur != None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def intersecthead(self, data):
        while cur.next.data != data:
            cur = cur.next
    
        deletednode = cur.next

        cur.next = cur.next.next
        return deletednode
    

    def size(self):
        cur = self.head
        s = 0
        while cur != None:
            s += 1
            cur = cur.next
        return s

    def seperate(self, deldata):
        cur = self.head
        header = self.head

        while cur.next.data != deldata:
            print(cur.next.data)
            cur = cur.next
        
        intersectll = Linkedlist(cur.next)
        print(f"Node({deldata}, size={intersectll.size()})")
        self.head = cur.next.next       
        cur.next = None 

        temp = Linkedlist(header)
        return temp

    def add_head(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = new
        newNode.next = self.head
        self.head = newNode

    def get_data(self):
        cur = self.head
        datalist = []
        while cur != None:
            datalist.append(cur.data)
            cur = cur.next
        return datalist
            

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    

        

inputstr = input("").split(",")
print(inputstr)

mainll = Linkedlist()

firstdata = int(inputstr[0].split('>')[0])
firstnext = int(inputstr[0].split('>')[1])

mainll.append(firstdata)
mainll.append(firstnext)
inputstr.pop(0)

while True: # get main Linked list
    for cur in inputstr:
        curdata = int(cur.split('>')[0])
        curnext = int(cur.split('>')[1])

    
        if mainll.search(curdata) and mainll.search(curnext): # check circular linked list
            inputstr.remove(cur)
            break

        if mainll.tail.data == curdata: # append to linkedlist
            mainll.append(curnext)
            inputstr.remove(cur)
            print(mainll)
            break
    else:
        break

print(inputstr)    
branchll = []

branchll.append([int(inputstr[0].split('>')[0])])
branchll[0].append(int(inputstr[0].split('>')[1]))
inputstr.pop(0)


while inputstr != []: # find branches
    curdata = int(inputstr[0].split('>')[0])
    curnext = int(inputstr[0].split('>')[1])

    for eachbranchll in branchll:
        if eachbranchll[-1] == curdata:
            eachbranchll.append(curnext)
            inputstr.pop(0)
            break
                
    else:
        if inputstr != []:
            branchll.append([int(inputstr[0].split('>')[0])])
            branchll[-1].append(int(inputstr[0].split('>')[1]))
            inputstr.pop(0)



branchll = sorted(branchll, key=lambda x:x[-1]) # sort branch
print(branchll)

seperatedmain = []
for eachintersect in branchll:
    intersectnode = eachintersect[-1]
    if mainll.search(intersectnode):
        seperatedmain.append(mainll.seperate(intersectnode))
        eachintersect.pop(-1)


# get all remaining data

alllist = []
for eachseperatedmain in seperatedmain:
    alllist.append(eachseperatedmain.get_data())

for eachbranchll in branchll:
    alllist.append(eachbranchll)

alllist.append(mainll.get_data())

alllist = sorted( alllist, key= lambda x:x[0])
print(alllist)


#swap merge
s = ''
while alllist != []:
    for eachfirst in alllist:
        if eachfirst != []:
            s += str(eachfirst.pop(0)) + '->'
        else :
            alllist.remove(eachfirst)

print(s[:-2])





        
