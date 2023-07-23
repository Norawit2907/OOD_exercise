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
    
inputstr = input("Enter width, height, and room: ").split()
width = int(inputstr[0]) - 1
height = int(inputstr[1]) - 1
room = inputstr[2].split(',')

visited = []
queue = Queue()
y = 0

check = True


if len(room) != height + 1:
    check = False
    print("Invalid map input.")

for i in room:
    if len(i) != width + 1:
        check = False
        print("Invalid map input.")


for floor in room:
    x = 0
    for tile in floor:
        if tile == 'F':
            startx = x
            starty = y
            queue.enqueue((startx, starty))
            visited.append((startx, starty))
        x += 1
    y += 1

if queue.isEmpty():
    print("Invalid map input.")
    check = False

#room[y][x]

if check == True:
    running = True
    while running:

        if queue.isEmpty():
            print("Cannot reach the exit portal.")
            break

        print(f"Queue: {queue.items}")
        currentx = queue.first()[0] 
        currenty = queue.first()[1]

        if 0 < currenty and room[currenty-1][currentx] == '_' and (currentx, currenty - 1) not in visited: # north พัง
            #print("enqueue North")
            visited.append((currentx, currenty - 1))
            queue.enqueue((currentx, currenty - 1))
        
        if currentx < width and room[currenty][currentx + 1] == '_' and (currentx + 1, currenty) not in visited:
            #print("enqueue East")
            visited.append((currentx + 1, currenty))
            queue.enqueue((currentx + 1, currenty))

        if currenty < height and room[currenty + 1][currentx] == '_' and (currentx, currenty + 1) not in visited:
            #print("enqueue South")
            visited.append((currentx, currenty + 1))
            queue.enqueue((currentx, currenty + 1))

        if 0 < currentx and room[currenty][currentx - 1] == '_' and (currentx - 1, currenty) not in visited :
            #print("enqueue West")
            visited.append((currentx - 1, currenty))
            queue.enqueue((currentx - 1, currenty))

        if 0 < currenty and room[currenty-1][currentx] == 'O' and (currentx, currenty - 1) not in visited:
            print("Found the exit portal.")
            break
        
        if currentx < width and room[currenty][currentx + 1] == 'O' and (currentx + 1, currenty) not in visited:
            print("Found the exit portal.")
            break

        if currenty < height and room[currenty + 1][currentx] == 'O' and (currentx, currenty + 1) not in visited:
            print("Found the exit portal.")
            break

        if 0 < currentx and room[currenty][currentx - 1] == 'O' and (currentx - 1, currenty) not in visited :
            print("Found the exit portal.")
            break
        
    
        
        queue.dequeue()
