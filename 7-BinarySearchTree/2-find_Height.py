class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = Node.insert(root.left, data)
        
        else:
            root.right = Node.insert(root.right, data)
        
        return root
    
    def getHeight(self):
        if self is None:
            return 0
        
        lheight = Node.getHeight(self.left)
        rheight = Node.getHeight(self.right)

        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

    def __str__(self) -> str:
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            self.root = Node.insert(self.root, data)
    
    def getHeight(self):
        if self.root is None:
            return -1
        else:
            return Node.getHeight(self.root) - 1
                


    def printTree(self, node, level = 0):
         if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print(f"Height of this tree is : {T.getHeight()}")