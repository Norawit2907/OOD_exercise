class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def __repr__(self):
        return str(self.data) 
    

class Tree:
    def __init__(self): 
        self.root = None
        self.num = 0

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
            self.num += 1

        else:
            h = height(self.root)
            max_node = pow(2,h+1)-1
            current = self.root
            if self.num+1 > max_node:
                while(current.left != None):
                    current = current.left
                current.left = Node(val)
                self.num+=1

            elif self.num+1 == max_node:
                while(current.right != None):
                    current = current.right
                current.right = Node(val)
                self.num+=1

            else:
                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)

                else:
                    insert_subtree(current.right,self.num - pow(2,h),val)
                self.num+=1

                    

def insert_subtree(r,num,val):
    if r != None:
        h = height(r)
        max_node = pow(2,h+1)-1
        current = r

        if num+1 > max_node:
            while(current.left != None):
                current = current.left
            current.left = Node(val)
            return

        elif num+1 == max_node:
            while(current.right != None):
                current = current.right
            current.right = Node(val)
            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):
            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:
            insert_subtree(current.right,num - pow(2,h),val)

    else:
        return



def height(root):
    if root == None:
        return -1
    
    else:
        left = height(root.left)
        right = height(root.right)

        if left>right:
            return left + 1
        
        else:
            return right + 1

                       

def printTree90(node, level = 0):

    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

def maxValue(node: Node):
    if node is None:
        return 0
    
    left  = maxValue(node.left)
    right = maxValue(node.right)

    value = 0
    if left>right:
        value = left
    else:
        value = right

    if value < node.data:
        value = node.data
    return value

def minValue(node: Node):
    if node is None:
        return 10000000
    
    left = minValue(node.left)
    right = minValue(node.right)

    if left < right:
        value = left
    else:
        value = right

    if value > node.data:
        value = node.data
    return value


def check_binary_search_tree_(root: Node):
    if root is None:
        return True
    
    if root.left != None and (root.data <= maxValue(root.left) or maxValue(root.left) > 100 or minValue(root.left) < 0):
        return False
    if root.right != None and (root.data >= minValue(root.right) or maxValue(root.left) > 100 or minValue(root.left) < 0):
        return False
    if check_binary_search_tree_(root.left) is False or check_binary_search_tree_(root.right) is False:
        return False
    return True

tree = Tree()
data = input("Enter Input : ").split()
for e in data:
    tree.insert(int(e))

printTree90(tree.root)
print(check_binary_search_tree_(tree.root))
