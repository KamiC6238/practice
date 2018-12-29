# practice

'''
    利用栈结构实现队列结构
    思路:使用两个栈，data栈存放Push的数据，help栈存放pop的数据，只需将入栈到data栈的数据pop出来后压入help栈中，即可实现队列结构应有的效果
         条件1:当data栈和help栈都不为空时，不可以将data栈的数据压入help栈中，否则会导致顺序错误。
         条件2:将data栈的数据压入help栈时，要将data栈中的数据一次性全部压入help栈。
'''

class Stack_to_Queue:

    def __init__(self):
        self.data = list()
        self.help = list()
    
    def push(self,value):
        self.data.append(value)

    def pop(self):
        if len(self.help) == 0 and len(self.data) == 0:
            print('the queue is empty!')
            return False   	
        if len(self.help) == 0 and len(self.data) != 0:
            self._data_to_help()
        return self.help.pop()

    def _data_to_help(self):
        while len(self.data) > 0:
            value = self.data.pop()
            self.help.append(value)

if __name__ == '__main__':
	  pass
    # s = Stack_to_Queue()
    # for i in range(0,5):
    #     s.push(i)
    # for i in range(0,6):
    #     print(s.pop())
