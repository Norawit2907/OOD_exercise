class Node:
    def __init__(self, name):
        self.setName(name)
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"{self.name} ({self.id})"
    
    def setName(self, name):
        self.name = name
        self.id = sum(ord(i) for i in name)

class AVL_Tree:
    def __init__(self):
        self.root = None

    def _insert(self, node, name):
        if node is None:
            return Node(name)
        
        if sum(ord(i) for i in name) < node.id:
            node.left = self._insert(node.left, name)
        else:
            node.right = self._insert(node.right, name)

        bf = self.getBalance(node)
        if bf > 1: #left heavy
            lbf = self.getBalance(node.left)
            if lbf >= 0: #left
                return self.rightRotate(node)
            elif lbf < 0:# right
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)    
            
        elif bf < -1:#right heavy
            rbf = self.getBalance(node.right)
            if rbf > 0: #left
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
            elif rbf <= 0:# right
                return self.leftRotate(node)
        return node
    
    def insert(self, name):
        self.root = self._insert(self.root, name)

    def height(self, node):
        if node is None:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)
        if left > right:
            val = left + 1

        else:
            val = right + 1

        return val
    
    '''
        y                            x
       / \     Right Rotation       / \ 
      x   C    - - - - - - - >     A   y
     / \       < - - - - - - -        / \ 
    A   B      Left Rotation         B   C
    '''

    def getBalance(self, root):
        return self.height(root.left) - self.height(root.right)

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y
    
    def rightRotate(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        return x

    def _delete(self, node: Node, name):
        if node is None:
            return
        id = sum(ord(i) for i in name)
        if id < node.id:
            node.left = self._delete(node.left, name)

        elif id > node.id or (id == node.id and node.name != name):
            node.right = self._delete(node.right, name)

        else:
            if node.left and node.right:
                suc = node.right
                while suc.left is not None:
                    suc = suc.left
                node.setName(suc.name)
                node.right = self._delete(node.right, suc.name)
            elif node.right is not None:
                return node.right
            elif node.left is not None:
                return node.left
            else:
                return None
            
        bf = self.getBalance(node)
        if bf > 1: #left heavy
            lbf = self.getBalance(node.left)
            if lbf >= 0: #left
                return self.rightRotate(node)
            elif lbf < 0:# right
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)    
            
        elif bf < -1:#right heavy
            rbf = self.getBalance(node.right)
            if rbf > 0: #left
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
            elif rbf <= 0:# right
                return self.leftRotate(node)

        return node
                

    def delete(self, name):
        self.root = self._delete(self.root, name)
    
    def printTree(self, node, level = 0):
        if node != None:
            print('    ' * level, node, sep = '')
            if node.left is None and node.right is None:
                return
            
            self.printTree(node.left, level + 1)
            self.printTree(node.right, level + 1)

        else:
            print('    ' * level, '*', sep = '')
    

avl_tree = AVL_Tree()
inp = input("Enter the data of your friend: ").split(",")
print("------------------------------")
for i in inp:
    op, *data = i.split(" ")
    data = data[0] if data else ""
    if op == "I":
        root = avl_tree.insert(data)
    elif op == "D":
        root = avl_tree.delete(data)
    elif op == "P":
        if avl_tree.root is not None:
            avl_tree.printTree(avl_tree.root)
        print("------------------------------")
