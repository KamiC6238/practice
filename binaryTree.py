# practice

'''
   二叉树的前中后遍历，包括递归和非递归
   
'''

    
    def __init__(self,value=None,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    
    def __init__(self,value=None):
        self.root = Node(value)
        self.stack = list()
        self.help = list()

    def createTree(self,value):
        node = Node(value)
        root = self.root
        while True:
            if value > root.value and root.right is None:
                root.right = node
                break
            elif value < root.value and root.left is None:
                root.left = node
                break
            elif value > root.value:
                root = root.right
            elif value < root.value:
                root = root.left

    def preOrder(self,root):
        if root is None:
            return None
        print(str(root.value) + ' ',end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self,root):
        if root is None:
            return None
        self.inOrder(root.left)
        print(str(root.value) + ' ',end="")
        self.inOrder(root.right)

    def posOrder(self,root):
        if root is None:
            return None
        self.posOrder(root.left)
        self.posOrder(root.right)
        print(str(root.value) + ' ',end="")

    def isNotEmpty(self):
        stack = self.stack
        length = len(stack)
        if length > 0:
            return True
        return False

    def preOrderUnRecur(self,root):
        if root is None:
            return None
        self.stack.append(root)
        while self.isNotEmpty():
            node = self.stack.pop()
            print(str(node.value) + ' ',end="")
            if node.right is not None:
                self.stack.append(node.right)
            if node.left is not None:
                self.stack.append(node.left)

    def inOrderUnRecur(self,root):
        if root is None:
            return None
        while self.isNotEmpty() or root is not None:
            if root is not None:
                self.stack.append(root)
                root = root.left
            else:
                root = self.stack.pop()
                print(str(root.value) + ' ',end="")
                root = root.right

    def posOrderUnRecur(self,root):
        if root is None:
            return None
        self.stack.append(root)
        while self.isNotEmpty():
            node = self.stack.pop()
            self.help.append(node)
            if node.left is not None:
                self.stack.append(node.left)
            if node.right is not None:
                self.stack.append(node.right)
        while len(self.help) > 0:
            print(str(self.help.pop().value) + ' ',end="")

if __name__ == '__main__':
    tree = Tree(5)
    seq = [3,8,2,4,1,7,6,10,9,11]
    for i in seq:
        tree.createTree(i)
    
    tree.preOrderUnRecur(tree.root)
    print('\n')
    tree.preOrder(tree.root)
    print('\n')

    tree.inOrderUnRecur(tree.root)
    print('\n')
    tree.inOrder(tree.root)
    print('\n')

    tree.posOrderUnRecur(tree.root)
    print('\n')
    tree.posOrder(tree.root)
    print('\n')
