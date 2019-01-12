# practice

'''
    题目:判断一个单链表是否有环。
    思路:使用两个指针，一个快指针一个慢指针，快指针走两步，慢指针走一步，若快指针走到None，则return False表示该链表五环。
         若链表有环，则快慢指针一定会相遇，在第一次相遇时，让快指针回到头结点，慢指针不改变，此时让快慢指针同时移动，但是
         快指针改为一次只走一步。
         最后，当快慢指针相遇时，相遇的节点就是第一个入环的节点。
         这个是有关数学归纳的证明。
         
'''


class Node:
    
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class FindFirstEntryPoint:

    def __init__(self):
        self.head = Node()
        self.tailnode = None

    def append(self,value):
        tailnode = self.tailnode
        node = Node(value)
        if tailnode is None:
            self.head.next = node
        else:
            self.tailnode.next = node
        self.tailnode = node
    
    def toLoop(self):
        cur = self.head.next.next
        self.tailnode.next = cur

    def isLoop(self):
        n1 = n2 = self.head
        tailnode = self.tailnode
        while n1 is not None and n2 is not None:
            n1 = n1.next.next
            n2 = n2.next
            if n1.next is None or n1.next.next is None:
                return False
            elif n1 is n2:
                n1 = self.head
                while n1 is not n2:
                    n1 = n1.next
                    n2 = n2.next
                return n1

if __name__ == '__main__':
    seq = [2,1,3,4,5,6]
    f = FindFirstEntryPoint()
    for i in seq:
        f.append(i)
    f.toLoop()
    print(f.isLoop().value)
