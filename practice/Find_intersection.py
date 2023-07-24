class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class LinkedList:
    def __init__(self):
      self.headval = None
    
    def append(self, value):
        temp = self.headval
        if self.headval == None:
            self.headval = Node(value)
            return

        while temp.nextval != None:
            temp = temp.nextval
        temp.nextval = Node(value)
    
    def __str__(self):
        list = []
        temp = self.headval
        while temp != None:
            list.append(temp.dataval)
            temp = temp.nextval
        
        return str(list)

inputstr = [list(map(int, x.split('>'))) for x in input("").split(',')]
#print(inputstr)

inputstr.sort(key=lambda x: x[1])
#print(inputstr)

for currentnode in inputstr:
    newnode = Node(currentnode)


listofhead = []
for currentnode in range(len(inputstr)-1):
    i = 1
    while inputstr[currentnode][1] == inputstr[currentnode + i][1]:
        listofhead.append(int(inputstr[currentnode][1]))
        i += 1 
#print(listofhead)


for i in listofhead:
    ll = [i]
    while True:
        for j in inputstr:
            if j[0] == ll[-1]:
                ll.append(j[1])
                break
        else:
            break

    print(f"Node({ll[0]}, size={len(ll)})")


        


    



#[['1', '2'], ['2', '3'], ['6', '7'], ['7', '3'], ['4', '5'], ['3', '4']]