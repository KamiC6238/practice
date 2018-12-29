# practice

'''
    用数据结构实现大小固定的队列
'''

class Queue:

    def __init__(self,capacity):
        self.queue = [None] * capacity
        self.capacity = 10
        self.size = 0
        self.start = 0
        self.end = 0

    def getStart(self):
        if self.size == 0:
            print('this queue is empty!')
            return -1      	
        if self.size != 0:
            value = self.queue[self.start]
            self.start += 1
            self.size -= 1
            if self.start == self.capacity:
               self.start = 0
        return value

    def insertEnd(self,value):
        if self.size == self.capacity:
            print('the queue is full!')
            return -1
        self.queue[self.end] = value
        self.end += 1
        self.size += 1
        if self.end == self.capacity:
            self.end = 0

if __name__ == '__main__':
    q = Queue(10)
    for i in range(0,10):
        q.insertEnd(i)
    q.getStart()
    q.insertEnd(100)
    q.getStart()
    q.insertEnd(200)
    # print(q.start,q.end)
    print(q.queue)
