# practice

'''
    题目:判断一个单链表是否是回文结构
    思路:有两种解法，一种使用栈，一种不用栈，而是使用快慢指针来实现，这里先用栈，因为栈可以实现逆序功能。所以可以用来解决这个回文结构的问题。
         逆序后通过出栈的值跟单链表头开始逐个比较，如果相等就继续比较，否则就直接返回False
'''

class Node:
    
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tailnode = None
        self.stack = list()

    def add(self,value):
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.head.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        
    def isPalindrome(self):
        stack = self.stack
        cur = self.head.next
        while cur is not None:
            if cur.value == stack.pop():
                cur = cur.next
            else:
                return False
        return True

    def add_to_stack(self):
        cur = self.head.next
        while cur is not None:
            self.stack.append(cur.value)
            cur = cur.next

if __name__ == '__main__':
    linkedlist = LinkedList()
    test1 = [1,2,2,1]
    test2 = [1,2,3,5,3,2,1]
    test3 = [1,2,3,4,2,1]
    for i in test1:
        linkedlist.add(i)
    linkedlist.add_to_stack()
    print(linkedlist.isPalindrome())
