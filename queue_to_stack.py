# practice

'''
    利用队列结构实现栈结构
'''

'''
    利用队列结构实现栈结构
    思路:利用两个队列，进队时push到data队列，出队时也从data队列出队，但是要实现栈结构，因此要出队的是最后一个进队的。
         调用pop时，将data队列中的数据依次使用popleft出队，并逐个进入help队列，直到data队列只剩下最后一个元素，此时
         返回data队列中的这一个数据给用户，这样就利用了两个队列实现了栈结构。需要注意的是，最后需要调换data和help两个
         队列的引用。
'''

from collections import deque

class Queue_to_Stack:

    def __init__(self):
        self.data = deque()
        self.help = deque()
    
    def push(self,value):
    	self.data.append(value)

    def pop(self):
        if len(self.data) == 0:
            print('the stack is empty!')
            return False
        while len(self.data) > 1:
            value = self.data.popleft()
            self.help.append(value)
        stack_top = self.data.popleft()
        self.data,self.help = self.help,self.data
        return stack_top

    def peek(self):
        if len(self.data) == 0:
            print('the stack is empty!')
            return False
        while len(self.data) > 1:
            value = self.data.popleft()
            self.help.append(value)
        stack_top = self.data.popleft()
        self.help.append(stack_top)
        self.data,self.help = self.help,self.data
        return stack_top

if __name__ == '__main__':
    pass
    # q = Queue_to_Stack()
    # for i in range(0,5):
    #     q.push(i)
    # print(q.peek(),len(q.data))
