# practice


'''
    题目:判断一个单链表是否是回文结构。
    思路:上一份使用了栈来实现逆序，以此来判断单链表是否是回文结构，但是为了使空间复杂度为O(1),就只利用几个变量来实现判断是否为回文结构的功能。
         1.利用快慢指针，快指针走两步，慢指针走一步。
         2.当快指针走到单链表尾时，慢指针走到链表的中间
         3.将慢指针之后的一半链表逆序过来
         4.将慢指针指向的节点的next设置为None
         5.之后设置几个变量将后半部分逆序即可
    提醒:单链表的节点有奇数和偶数个，所以快指针在移动的时候需要根据情况来移动。
    
    感悟:coding能力真的很重要，即使有思路，但如果没办法亲自动手实现，就废了一半了。
         
'''

class Node:
    
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class IsPalindrome:
    
    def __init__(self):
        self.head = Node()
        self.tailnode = None

    def append(self,value):
        tailnode = self.tailnode
        node = Node(value)
        if tailnode is None:
            self.head.next = node
        else:
        	tailnode.next = node
        self.tailnode = node

    def iter_node(self):
        cur = self.head.next
        while cur is not None:
            print(str(cur.value) + ' ',end="")
            cur = cur.next
    
    def isPalidrome(self):
        n1 = self.head
        n2 = self.head
        tailnode = self.tailnode
        while n1 is not None and n2 is not None:
            n2 = n2.next.next
            n1 = n1.next
            if n2 is None or n2 is tailnode:
                n2 = tailnode
                break
        n2 = n1.next
        n1.next = None
        while n2 is not None:   # 交换完之后n1是最后一个节点
            n3 = n2.next
            n2.next = n1
            n1 = n2
            n2 = n3
        res = True
        n3 = n1
        n2 = self.head.next
        while n1 is not None and n2 is not None:
            if n1.value != n2.value:
                return False
            n2 = n2.next
            n1 = n1.next
        n1 = n3.next
        n3.next = None
        while n1 is not None:
            n2 = n1.next
            n1.next = n3
            n3 = n1
            n1 = n2
        return True 

if __name__ == '__main__':
    ip = IsPalindrome()
    seq = [1,2,3,2,1]
    for i in seq:
        ip.append(i)
    print(ip.isPalidrome())
