# practice

'''
   二叉树的前中后遍历，包括递归和非递归,序列和反序列化，判断二叉树是否为搜索二叉树和是否为平衡二叉树,以及是否为完全二叉树
   
   判断是否为搜索二叉树:利用中序遍历，只要所有节点的值是按升序排列的即可。
   
   判断是否为平衡二叉树:创建一个包含是否平衡以及高度两个属性的类，利用递归的思想，判断一个节点的左子树是否平衡，不平衡则返回False，
                      同理判断右子树是否平衡，否则返回False，若左右子树都平衡，则将左右子树的高度差进行相减，若结果大于1，说明
                      不平衡，此时返回False，若小于1，则返回左右子树树中高度较高的那棵树的高度再加1。
                      加1是加上了父节点，表明整棵树的高度。
                      
   关于判断是否为完全二叉树的思路:首先这个题要采用层序遍历，既然是完全二叉树，那么必须满足下列的两种情况:
                                1.任意节点不得只有右子树却没有左子树
                                2.当任意节点的左右子树均不全时，该节点后面的所有节点必须是叶子节点。
                                第二个条件建立在第一个条件之上，也就是说第二个条件，当左右子树都不全的情况是只有左子树没有右子树
                                或者左右子树都没有。此时该节点后面的所有节点都必须为叶子节点。
                                在代码中，加入了一个leaf变量来表示是否要判断接下来的节点是否为叶子节点，起始值为False，
                                当满足第二个条件时，让leaf为True,也就是说不管左子树有没有，只要右子树为空，leaf就必须为True
                                
   
'''

from collections import deque

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
        self.leaf = False

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
   
    # 判断二叉树是否为完全二叉树
    def isCompleteBT(self,root):
        de = deque()
        de.append(root)
        while len(de) > 0:
            node = de.popleft()
            l = node.left
            r = node.right
            if (l is None and r is not None) or (self.leaf and (l is not None or r is not None)):
                return False
            if l is not None:
                de.append(l)
            if r is not None:
                de.append(r)
            else:
                self.leaf = True
        return True
   
    # 已知二叉树为完全二叉树，求节点个数，时间复杂度小于O（n）
    def getNodeNums(self,root):
        if root is None:
            return 0
        h = self.most_left_level(root,1)
        return self.bs(root,1,h)

    def bs(self,node,level,h):
        if level == h:
            return 1
        if self.most_left_level(node.right,level+1) == h:
            return pow(2,h - level) + self.bs(node.right,level+1,h) 
        else:
            return pow(2,h - level - 1) + self.bs(node.left,level+1,h)

    def most_left_level(self,node,level):
        while node is not None:
            level += 1
            node = node.left
        return level - 1

if __name__ == '__main__':
    tree = Tree(5) 
    # seq = [10,15,8,11,13,16,3,9]  测试完全二叉树节点个数的数据
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
