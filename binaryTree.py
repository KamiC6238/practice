# practice

'''
   二叉树的前中后遍历，包括递归和非递归,序列和反序列化，判断二叉树是否为搜索二叉树以及是否为平衡二叉树
   
'''

class ReturnData:
    
    def __init__(self,isB,height):
        self.isB = isB
        self.height = height
      
class Node:
   
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
            if value == root.value:
                break
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
    
    # 前序遍历序列化
    def serialize(self,root):
        if root is None:
            self.res += '#_'
        else:
            self.res += str(root.value) + '_'
            self.serialize(root.left)
            self.serialize(root.right)
    
    # 反序列化
    def deserialize(self,res):
        if res is '':
            return None
        seq = re.split('_',res)
        for value in seq:
            if value.isdigit() is True:
                self.create_Tree(int(value))
                  
    # 判断二叉树是否为搜索二叉树
    def isSearchBinaryTree(self,root):
        res = 0
        while self.isNotEmpty() or root is not None:
            if root is not None:
                self.stack.append(root)
                root = root.left
            else:
                node = self.stack.pop()
                if node.value >= res:
                    res = node.value
                    root = node.right
                else:
                    return False
        return True
   
    # 判断二叉树是否为平衡二叉树
    def isBalanceBinaryTree(self,root):
        return self.process(root)
    
    def process(self,root):
        if root is None:
            return ReturnData(True,0)
        data_left = self.process(root.left)
        if data_left.isB is False:
            return ReturnData(False,0)
        data_right = self.process(root.right)
        if data_right.isB is False:
            return ReturnData(False,0)
        if (data_left.height - data_right.height) > 1:
            return ReturnData(False,0)
        return ReturnData(True,max(data_left.height,data_right.height) + 1)             

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
   
    tree.serialize(se.root)
    print(tree.res)
    tree.res = ''
    tree.deserialize(tree.res)
    tree.serialize(tree.root)
    print(tree.res)
   
    print(tree.isSearchBinaryTree(tree.root))
      
    print(tree.isBalanceBinaryTree(tree.root).isB)
