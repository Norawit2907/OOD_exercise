class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        node = self.root
        q = []
        q.append(node)
        while len(q) > 0:
            node = q.pop(0)
            if node.left is not None:
                q.append(node.left)
            else:
                node.left = Node(data)
                break

            if node.right is not None:
                q.append(node.right)
            else:
                node.right = Node(data)
                break
    
    def printtree(self, node, level = 0):
        if node != None:
            self.printtree(node.right, level+1)
            print("     " * level, node.data)
            self.printtree(node.left, level+1)
    
    def cuttree(self, node):
        if node.left is None and node.right is None:
            return node.data 
        leftvalue = self.cuttree(node.left)
        rightvalue = self.cuttree(node.right)

        if leftvalue < rightvalue:
            node.data = leftvalue
        else:
            node.data = rightvalue  
        return node.data
    
    def minusleaf(self, node):
        if node.left is None and node.right is None:
            return node.data
        leftvalue = self.minusleaf(node.left)
        rightvalue = self.minusleaf(node.right)
        
        if leftvalue < rightvalue:
            node.left.data -= leftvalue
            node.right.data -= leftvalue
        else:
            node.right.data -= rightvalue
            node.left.data -= rightvalue 
        return node.data
    
    def gettotal(self, node):
        if node is None:
            return 0
        leftv = self.gettotal(node.left)
        rightv = self.gettotal(node.right)
        return leftv + node.data + rightv
    
    def getnodenum(self, node):
        if node is None:
            return 0
        left = self.getnodenum(node.left)
        right = self.getnodenum(node.right)
        return left + 1 + right 


inp = input('Enter Input : ').split('/')
n = int(inp[0])
data = inp[1].split()
tree = Tree()
for i in range(n//2):
    tree.insert('*')

for i in data:
    tree.insert(int(i))
#tree.printtree(tree.root)
if tree.getnodenum(tree.root) > n:
    print("Incorrect Input")
    exit()
#print('----------------------------')
tree.cuttree(tree.root)
#tree.printtree(tree.root)
#print('----------------------------')
tree.minusleaf(tree.root)
#tree.printtree(tree.root)
print(tree.gettotal(tree.root))
            