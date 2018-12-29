# practice

'''
   利用数组结构实现固定长度的栈结构
   思路:本身很简单，可以用列表实现，不过列表跟数组的差别是列表的边界是会伸缩的，因此pop的时候，不能直接使用list.pop()这样的形式，
        否则会导致长度不是固定长度。
        解决方法发是设置一个index指针，起始值为0，表示应该入栈的位置，pop的时候返回指针的上一个位置的值即可。随后将其设为None，之后index -= 1
'''

class Stack:
    
    def __init__(self,size):
        self.size = size
        self.index = 0
        self.stack = [None] * size

    def push(self,value):
        if self.index < self.size:
            self.stack[self.index] = value
            self.index += 1
        else:
        	print('the stack is full!')
    
    def pop(self):
        if len(self.stack) == 0:
            print('the stack is empty!')
            return False
        value = self.stack[self.index-1]
        self.stack[self.index-1] = None
        self.index -= 1
        return value

    def peek(self):
        if len(self.stack) == 0:
            print('the stack is empty!')
            return False
        value = self.stack[self.index-1]
        return value 
        
if __name__ == '__main__':
    pass
    # s = Stack(3)
    # for i in range(0,3):
    #     s.push(i)
    # s.push(2)		# the stack is full!
    # s.pop()
    # s.pop()
    # print(s.stack)	# [0,None,None]
