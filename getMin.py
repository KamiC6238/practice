# practice

'''
  实现一个特殊的栈，在实现栈的基本功能的基础上，再实现返 回栈中最小元素的操作。 
  [要求] 1．pop、push、getMin操作的时间复杂度都是O(1)。
         2．设计的栈类型可以使用现成的栈结构。
         
  思路:使用两个列表作为栈，每个栈分配一个index作为指针，起始值为0，表示应该存放的值的下标。
  
       push的时候，value在stakc1正常入栈，在stack2时先判断stack2是否为空，如果为空则入栈，否则比较value与stack2栈顶元素的大小，
       如果value大于等于stack2的栈顶元素，那么将stack2的栈顶元素压入栈，否则将value压入栈。
       pop的时候先判断栈是否为空，不为空的时候正常出栈即可。
       
       获取栈的最小值操作只要返回stack2的栈顶即可。这样就使时间复杂度为O(1)了。
  
  提醒:    我一开始想的是只要根据入栈的元素来不断更新stack2栈顶元素就可以了，但很快意识到错误，因为只要一pop，stack2就为空了。
       由于stack1和stack2的高度是同步增长的，而且value大于stakc2栈顶元素时，会继续把最小值进行压栈，所以stack2中可能会有
       多个最小值在栈顶，因此不用担心在pop的过程中把最小值给pop掉了。
  
'''

class getMin:
    
    def __init__(self):
        self.stack1 = list()
        self.stack2 = list()
        self.index1 = 0
        self.index2 = 0

    def push(self,value):
        self.stack1.append(value)
        length = len(self.stack2)
        if length == 0:
            self.stack2.append(value)
        elif value >= self.stack2[self.index2-1]:
            self.stack2.append(self.stack2[self.index2-1])
        else:
            self.stack2.append(value)
        self.index1 += 1
        self.index2 += 1


    def pop(self):
        if self.index1 > 0 and self.index2 > 0:
            value = self.stack1.pop()
            self.stack2.pop()
            self.index1 -= 1
            self.index2 -= 1
        elif self.index1 == 0:
        	print('the stack is empty!')
        	return None
        return value

    def getMin(self):
        if self.index2 > 0:
            return self.stack2[self.index2-1]
        else:
            print('the stack is empty,the min is not exist!')
        return -1

if __name__ == '__main__':
    g = getMin()
    g.push(1)
    g.push(4)
    g.push(0)
    g.pop()
    g.pop()
    g.pop()
    g.pop()
    print(g.stack1)
    print(g.stack2)
    print(g.getMin())
