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

# custome = [arrivetime, ordertime, id, waitedtime]

print(" ***Cafe***")
log = input("Log : ").split('/')
log = [e+','+str(i+1)+','+'0' for i, e in enumerate(log) ] # add id and wait time
log = [[int(x) for x in i.split(',')] for i in log]

logqueue = Queue()
for i in log:
    logqueue.enqueue(i)

barista = Queue()
waitline = Queue()
longestwait = 0
longestwaitcustomer = 0
time = 0

while (logqueue.isEmpty() == False or waitline.isEmpty() == False or barista.isEmpty() == False) and time <= 20:
    #print(f'time : {time}')
    

    temp = Queue()
    while not barista.isEmpty():
        cus = barista.dequeue()
        cus[1] -= 1
        if cus[1] <= 0:
            print(f"Time {time} customer {cus[2]} get coffee")
        else:
            temp.enqueue(cus)

    barista = temp


    while logqueue.isEmpty() == False and logqueue.first()[0] <= time:
        waitline.enqueue(logqueue.dequeue())
        #print(f"waitline add : {waitline.items}")
    
    while barista.size() < 2 and waitline.isEmpty() == False:
        cus = waitline.dequeue()
        cus[3] = time - cus[0]
        if cus[3] > longestwait:
            longestwait = cus[3]
            longestwaitcustomer = cus[2]
        barista.enqueue(cus)

    time += 1

if longestwait == 0:
    print("No waiting")
else:
    print(f"The customer who waited the longest is : {longestwaitcustomer}")
    print(f"The customer waited for {longestwait} minutes")

  
# [[0, 3, 1, 0], [0, 7, 2, 0], [2, 3, 3, 0], [7, 7, 4, 0], [10, 5, 5, 0], [10, 1, 6, 0]]
# barista = []
# waitline = []
# time = 0

# waittime++ bartime--(canpop) waitline.add  barempty(takecust) time++