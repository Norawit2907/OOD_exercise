class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def append(root, data):
        if root is None:
            return Node(data)
        
        if data < root.data:
            root.left = Node.append(root.left, data)
        
        else:
            root.right = Node.append(root.right, data)
        
        return root

    def timesThree(self, k):
        if self != None:
            if self.data > k:
                self.data *= 3
            Node.timesThree(self.left, k)
            Node.timesThree(self.right, k)

    def __repr__(self) -> str:
        return str(self.data)
    
    
    def inorder(self):
        if self is None:
            return
        Node.inorder(self.left)
        print(self.data, end=' ')
        Node.inorder(self.right)
    
    def preorder(self):
        if self is None:
            return
        print(self.data, end=' ')
        Node.preorder(self.left)
        Node.preorder(self.right)


class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        
        else:
            self.root.append(data)
    
    def printTree(self, node, level = 0):
         if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

inp = input("Enter Input : ").split()
k = int(inp[-1].split('/')[1])
inp[-1] = inp[-1].split('/')[0]
inp = [int(i) for i in inp]
T = BST()
for i in inp:
    T.insert(i)
T.printTree(T.root)
print('--------------------------------------------------')
T.root.timesThree(k)
T.printTree(T.root)
