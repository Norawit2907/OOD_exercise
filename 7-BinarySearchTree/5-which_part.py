class Node():
    def __init__(self, data):
         self.data = data
         self.left = None
         self.right = None

    def insert(self, data):
        if self is None:
             return Node(data)
        if self.data > data:
             self.left = Node.insert(self.left, data)
        else:
             self.right = Node.insert(self.right, data)
        return self
    
    def __repr__(self) -> str:
        return str(self.data)
    
class BST():
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root.insert(data)
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def checkpos(self, num):
        r = self.root
        if r.data == num:
            return 'Root'
        while True:
            if r is None:
                return "Not exist"
            if r.data == num and (r.left != None or r.right != None):
                return "Inner"
            if r.data == num and (r.left == None and r.right == None):
                return "Leaf"
            if r.data > num:
                r = r.left
            else:
                r = r.right

inp = input("Enter Input : ").split()
k = int(inp[0])
t = BST()
for i in range(1,len(inp)):
     t.insert(int(inp[i]))

t.printTree(t.root)
print(t.checkpos(k))

