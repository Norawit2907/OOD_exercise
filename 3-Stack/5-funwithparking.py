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

print("******** Parking Lot ********")
strinput = input("Enter max of car,car in soi,operation : ").split()
soicapacity = int(strinput[0])
listcar = strinput[1].split(',')
listcar = list(map(int, listcar))
action = strinput[2]
editcar = int(strinput[3])

canpark = True
candepart = False
soia = Stack()
soib = Stack()
for car in listcar:
    if car == 0:
        break
    soia.push(car)

if action == 'arrive':
    if soia.size() == soicapacity:
        print(f"car {editcar} cannot arrive : Soi Full")
    
    else:
        while soia.isEmpty() == False:
            if soia.top() == editcar:
                print(f"car {editcar} already in soi")
                canpark = False
                break
            soib.push(soia.pop())
        
        while soib.isEmpty() == False:
            soia.push(soib.pop())
        
        if canpark == True:
            soia.push(editcar)
            print(f"car {editcar} arrive! : Add Car {editcar}")

elif action == 'depart':
    if soia.isEmpty():
        print(f"car {editcar} cannot depart : Soi Empty")
    
    else:
        while soia.isEmpty() == False:
            if soia.top() == editcar:
                candepart = True
                soia.pop()
                continue

            soib.push(soia.pop())
        
        while soib.isEmpty() == False:
            soia.push(soib.pop())
        
        if candepart == True:
            print(f"car {editcar} depart ! : Car {editcar} was remove")
        
        elif candepart == False:
            print(f"car {editcar} cannot depart : Dont Have Car {editcar}")


print(soia.items)     

