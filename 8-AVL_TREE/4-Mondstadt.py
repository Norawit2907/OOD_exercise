class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.index = 0

    def __repr__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        index = 0
        node = self.root
        node.index = index
        queue = []
        queue.append(node)
        while len(queue) > 0:
            node = queue.pop(0)
            if node.left is not None:
                index += 1
                node.left.index = index
                queue.append(node.left)

            if node.right is not None:
                index += 1
                node.right.index = index
                queue.append(node.right)

            if node.left is None:
                node.left = Node(data)
                index += 1
                node.left.index = index
                break
            if node.right is None:
                node.right = Node(data)
                index += 1
                node.right.index = index
                break

    def getnodefromindex(self, node, index):
        if node is None:
            return
        if node.index == index:
            return node
        else:
            getnodeleft = self.getnodefromindex(node.left, index)
            getnoderight = self.getnodefromindex(node.right, index)
            if getnodeleft != None:
                return getnodeleft
            if getnoderight != None:
                return getnoderight

    def findtotal(self, node):
        if node is None:
            return 0
        return self.findtotal(node.left) + node.data + self.findtotal(node.right)    
    
    def checksize(self, node1, node2):
        node1 = self.getnodefromindex(self.root, node1)
        node2 = self.getnodefromindex(self.root, node2)
        totalf = self.findtotal(node1)
        totals = self.findtotal(node2)
       
        if totalf < totals:
            return str(node1.index)+'<'+str(node2.index)
        elif totalf > totals:
            return str(node1.index)+'>'+str(node2.index)
        else:
            return str(node1.index)+'='+str(node2.index)
            
    def printTree(self, node, level = 0):
         if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


inp = input('Enter Input : ').split('/')
data = inp[0].split()
check = inp[1].split(',')
#print(data, check)
tree = Tree()
for i in data:
    tree.insert(int(i))    
#tree.printTree(tree.root)
print(tree.findtotal(tree.root))
for i in check:
    fn = int(i.split()[0])
    sn = int(i.split()[1])
    print(tree.checksize(fn,sn))