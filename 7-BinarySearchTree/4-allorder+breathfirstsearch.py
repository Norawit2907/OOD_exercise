class Node:
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

    def postorder(self):
        if self is None:
            return
        Node.postorder(self.left)
        Node.postorder(self.right)
        print(self.data, end=' ')
    
    def breathFirstSearch(self):
        if self is None:
            return
        
        q = []
        q.append(self)
        while len(q) > 0:
            print(q[0].data, end = ' ')
            node = q.pop(0)

            if node.left != None:
                q.append(node.left)
            if node.right != None:
                q.append(node.right)

    def __repr__(self) -> str:
        return str(self.data)

class BST:
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

inp = input('Enter Input : ').split()
inp = [int(i) for i in inp]
t = BST()
for i in inp:
    t.insert(i)

print("Preorder : ",end = '')
t.root.preorder()
print('')

print("Inorder : ",end = '')
t.root.inorder()
print('')

print("Postorder : ",end = '')
t.root.postorder()
print('')

print("Breadth : ",end = '')
t.root.breathFirstSearch()



