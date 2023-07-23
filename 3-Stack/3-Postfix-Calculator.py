class Stack():

    def __init__(self, ls = None):
        self.ls = []
    def push(self,i):
        self.ls.append(i)

    def pop(self):
        return self.ls.pop()

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
    def size(self):
        return len(self.items)

def postFixeval(st):

    s = Stack()

    ### Enter Your Code Here ###
    for i in st: 
        if i == '+' or i == '-' or i == '*' or i == '/':
            num2 = s.pop()
            num1 = s.pop()
            if i == '+':
                s.push(num1 + num2)
            elif i == '-':
                s.push(num1 - num2)
            elif i == '*':
                s.push(num1 * num2)
            elif i == '/':
                s.push(num1 / num2)

        else:
            s.push(int(i))
       

    return s.pop()

            


print(" ***Postfix expression calcuation***")

token = list(input("Enter Postfix expression : ").split())

print("Answer : ",'{:.2f}'.format(postFixeval(token)))