# practice

'''
    题目:给一棵二叉树和树中的节点，打印该节点的后继节点。
    
    思路:后继节点就是按照中序遍历的顺序来看的，比如节点值为2的left是1，right是3，中序遍历打印出来就是123,所以2就是1的后继节点，3就是2的后继节点。
         在寻找后继节点的过程中，需要判断该节点是否有右子树，所以应该分两种情况。
         1.如果该节点的右子树为空，此时该节点的后继节点应该从下往上找，找到一个节点，该节点的父节点的左子树等于当前节点，那么返回父节点。
           要注意的是第一次找到的时候就返回，边界条件往上找直到根节点。因为根节点的父节点为None
         2.如果该节点的右子树不为空，那么该节点的后继节点就是该右子树最左边的节点，如果右子树只有一个节点，那么返回其本身。
    
    感悟:感觉coding能力有点点提升了。

'''
class Node:
    
    def __init__(self,value=None,parent=None,left=None,right=None,next=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.next = next

class FindNextNode:
    
    def __init__(self,value):
        self.root = Node(value)
        self.stack = list()

    def createTree(self,value):
        node = Node(value)
        root = self.root
        while True:
            if value > root.value and root.right is None:
                root.right = node
                node.parent = root
                break
            elif value < root.value and root.left is None:
                root.left = node
                node.parent = root
                break
            elif value > root.value:
                root = root.right
            elif value < root.value:
                root = root.left

    def isNotEmpty(self):
        stack = self.stack
        length = len(stack)
        if length > 0:
            return True
        return False

    def inOrderUnRecur(self,root):
        if root is None:
            return None
        while self.isNotEmpty() or root is not None:
            if root is not None:
                self.stack.append(root)
                root = root.left
            else:
                node = self.stack.pop()
                print(str(node.value) + ' ',end="")
                root = node.right
    
    def findNextNode(self,node):
        if node is None:
            return None
        elif node.right is not None:
            parent = self.getMostNode(node.right)
        else:
            parent = node.parent
            while parent is not None and parent.left is not node:
                node = parent
                parent = node.parent
        return parent

    def getMostNode(self,node):
        if node.left is None:
            return node
        while node is not None:
            node = node.left
        return node

if __name__ == '__main__':
    tree = FindNextNode(5)
    seq = [3,8,2,4,1,7,6,10,9,11]
    for i in seq:
        tree.createTree(i)
    tree.inOrderUnRecur(tree.root)
    node = tree.findNextNode(tree.root.right.right.right)
    print('\n')
    if node is None:
        print('None')
    else:
        print(node.value)
