# practice

'''
    题目:判断一个单链表是否有环,并求两个链表第一个相交的节点。
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
        self.head1 = Node()
        self.head2 = Node()
        self.tailnode = None
        self.tailnode2 = None
    
    def append(self,value,head):
        if head is self.head1:
            self.append1(value)
        else:
            self.append2(value)
            
    def append1(self,value):
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.head1.next = node
        else:
            tailnode.next = node
        self.tailnode = node

    def append2(self,value):
        node = Node(value)
        tailnode = self.tailnode2
        if tailnode is None:
            self.head2.next = node
        else:
            tailnode.next = node
        self.tailnode2 = node

    # 判断是否有环,并且返回入环的第一个节点
    def isLoop(self,head):
        n1 = n2 = head
        while n1 is not None and n2 is not None:
            n1 = n1.next.next
            n2 = n2.next
            if n1.next is None or n1.next.next is None:
                return False
            elif n1 is n2:
                n1 = head
                while n1 is not n2:
                    n1 = n1.next
                    n2 = n2.next
                return n1

    # 两个单链表均无环的情况
    def noloop(self):
        cur1 = self.head1.next
        cur2 = self.head2.next
        n = 0
        while cur1 is not None:
            n += 1
            cur1 = cur1.next
        while cur2 is not None:
            n -= 1
            cur2 = cur2.next
        if cur1 is not cur2:
            return None
        cur1 = self.head1.next
        cur2 = self.head2.next
        if n > 0:
            while n > 0:
                cur1 = cur1.next
                n -= 1
        else:
            while n < 0:
                cur2 = cur2.next
                n += 1
        while cur1 is not cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

    # 两个链表均有环时分两种情况
    def bothloop(self):
        head1 = self.head1
        head2 = self.head2
        loop1 = self.isLoop(head1)
        loop2 = self.isLoop(head2)
        if loop1 is not loop2:          # 同环不同入环节点
            cur = loop1.next
            while cur is not loop1:
                if cur is loop2:
                    return loop1
                else:
                    cur = cur.next
            return None 
        n = 0
        cur1 = head1.next
        cur2 = head2.next
        while cur1 is not loop1:
            n += 1
            cur1 = cur1.next
        while cur2 is not loop2:
            n -= 1
            cur2 = cur2.next
        if n > 0:
            cur1 = head1.next
            while n > 0:
                cur1 = cur1.next
                n -= 1
        elif n < 0:
            cur2 = head2.next
            while n < 0:
                cur2 = cur2.next
                n += 1
        while cur1 is not cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1

    def iter_node(self,head):
        cur = head.next
        # count = 0
        while cur is not None:
            print(str(cur.value) + ' ',end="")
            cur = cur.next
            # count += 1
            # if count == 30:
            #     break
        print('\n')

    # 将链表变成环
    def toLoop(self,head,tailnode):
        cur = head.next.next.next.next
        tailnode.next = cur
        return cur

if __name__ == '__main__':
    seq = [2,1,3,5,6,7]
    seq1 = [1,2]
    f = FindFirstEntryPoint()
    head1 = f.head1
    head2 = f.head2

    # 两个单链表均无环的情况

    # for i in seq:
    #     f.append(i,head1)

    # for i in seq1:
    #     f.append(i,head2)
    # cur = head1.next.next.next
    # f.tailnode2.next = cur
    # print(f.noloop().value)

    # 具有同一个环且入环节点相同的情况

    # for i in seq:
    #     f.append(i,head1)
    # cur = f.toLoop(head1,f.tailnode) # 得到其中一个单链表的入环点

    # for i in seq1:
    #     f.append(i,head2)
    # f.tailnode2.next = cur           # 将另一个链表的节点接入上一个节点所在的环
    # print(f.bothloop().value)

    # 具有同一个环但是入环节点不同的情况

    # seq3 = [1,2,3,4]
    # for i in seq3:
    # 	f.append(i,head2)
    # cur2 = cur.next.next
    # f.tailnode2.next = cur2
    # print(f.bothloop().value)
