# practice

'''
    题目:给一个单链表和一个整数num，节点的数值均为整数，比num小的放左边，等于num的放中间，大于num的放右边。
    
    思路:通过设置几个变量来达到不使用额外的空间。
         将小于num的放到less链表，等于num的放到equal链表，大于num的放到more链表，最后将三个链表收尾相连，就得到最后的结果。
    
    提醒:跟使用数组的时候不一样，在单链表中，考虑两种极端情况，没有less链表或者没有more链表的时候要分情况讨论。
         因为num可能是所有数中最小的或者最大的。
    
    总结:其实这个题还是很简单的，就是很普通的链表操作而已。
    
'''
class Node:
    
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = next

class NetherlandsFlag:
    
    def __init__(self):
        self.head = Node()
        self.less = Node()
        self.more = Node()
        self.equal = Node()
        self.end1 = None
        self.end2 = None
        self.end3 = None
        self.tailnode = None

    def append(self,value):
        tailnode = self.tailnode
        node = Node(value)
        if tailnode is None:
            self.head.next = node
        else:
            tailnode.next = node
        self.tailnode = node

    def partition(self,num):
        cur = self.head.next
        while cur is not None:
            if cur.value < num:
                if self.end1 is None:
                    self.less.next = cur
                else:
                    self.end1.next = cur    
                self.end1 = cur
            elif cur.value == num:
                if self.end2 is None:
                    self.equal.next = cur
                else:
                    self.end2.next = cur
                self.end2 = cur
            elif cur.value > num:
                if self.end3 is None:
                    self.more.next = cur
                else:
                    self.end3.next = cur
                self.end3 = cur
            cur = cur.next
        self.reconnect()
    
    def reconnect(self):
        if self.less.next is None:
            self.head.next = self.equal.next
            self.end2.next = self.more.next
            self.end3.next = None
        elif self.more.next is None:
            self.head.next = self.less.next
            self.end1.next = self.equal.next
            self.end2.next = None
        else:
            self.head.next = self.less.next
            self.end1.next = self.equal.next
            self.end2.next = self.more.next
            self.end3.next = None

    def iter_node(self):
        cur = self.head.next
        while cur is not None:
            print(str(cur.value) + ' ',end="")
            cur = cur.next
            
if __name__ == '__main__':
    ne = NetherlandsFlag()
    seq = [55,10,5,3,100,22,33,1,58]
    for i in seq:
        ne.append(i)
    ne.partition(100)
    ne.iter_node()
