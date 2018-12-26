# 求中位数

'''
	有一个流，不断流出整数，要求求出所吐出的所有数的中位数
	采用堆结构解决问题
	思路：
	1.将较大的n/2个数放在小根堆中，较小的n/2个数放在大根堆中
	2.如果两堆的元素个数相差为2，则将元素个数多的堆的堆顶节点弹出到另外一个堆中
	3.弹出堆顶的操作是先将堆顶节点和最后一个节点交换，然后数组长度减一，另外一个堆通过heapify操作将对方的堆顶元素接收形成大根堆或者小根堆
	4.小根堆的堆顶是较大的n/2个数中最小的，而大根堆中堆顶是较小的n/2个数最大的那个，那么这两个数就一定会在n个数的中间，然后相加除以2即可得到
	  中位数 
'''


import random

class Median:

    def __init__(self):
        num = random.randint(0,100)
        self.big_seq = list()
        self.small_seq = list()
        self.big_seq.append(num)

    def heapInsert_big(self,index):
        seq = self.big_seq
        while seq[index] > seq[int((index-1)/2)]:
            seq[index],seq[int((index-1)/2)] = seq[int((index-1)/2)],seq[index]
            index = int((index-1)/2)
        return self.big_seq

    def heapInsert_small(self,index):
        seq = self.small_seq
        while seq[index] < seq[int((index-1)/2)]:
            seq[index],seq[int((index-1)/2)] = seq[int((index-1)/2)],seq[index]
            index = int((index-1)/2)
            return self.small_seq

    def heapify_big(self,index,size):
        seq = self.big_seq
        left = index * 2 + 1
        while left < size:
            if left + 1 < size and seq[left+1] > seq[left]:
                largest = left + 1
            else:
                largest = left
            if seq[largest] > seq[index]:
                seq[largest],seq[index] = seq[index],seq[largest]
            else:
                break
            index = largest
            left = index * 2 + 1
        return seq

    def heapify_small(self,index,size):
        seq = self.small_seq
        left = index * 2 + 1
        while left < size:
            if left + 1 < size and seq[left+1] < seq[left]:
                smallest = left + 1
            else:
                smallest = left
            if seq[smallest] < seq[index]:
                seq[smallest],seq[index] = seq[index],seq[smallest]
            else:
                break
            index = smallest
            left = index * 2 + 1
        return seq

    def isBigger_than_two(self,length_small,length_big):
        num1 = length_small - length_big
        num2 = length_big - length_small
        if num1 >= 2:
            return 1
        if num2 >= 2:
            return 0

    def adjustment(self,flag,length_small,length_big):
        if flag == 1:
            small_seq = self.small_seq
            num = small_seq[0]
            self.big_seq.append(num)
            self.heapInsert_big(length_big)
            small_seq[0],small_seq[length_small] = small_seq[length_small],small_seq[0]
            small_seq.pop()
            self.heapify_small(0,length_small-1)
        else:
            big_seq = self.big_seq
            num = big_seq[0]
            self.small_seq.append(num)
            self.heapInsert_small(length_small)
            big_seq[0],big_seq[length_big] = big_seq[length_big],big_seq[0]
            big_seq.pop()
            self.heapify_big(0,length_big-1)


    def getMedian(self):
        new_lst = self.big_seq + self.small_seq
        if len(new_lst) % 2 == 0:
            num1 = self.big_seq[0]
            num2 = self.small_seq[0]
            median = (num1 + num2) / 2
        elif len(self.big_seq) > len(self.small_seq):
            median = self.big_seq[0]
        elif len(self.small_seq) > len(self.big_seq):
            median = self.small_seq[0]
        return median

    def main(self,num):
        big_seq = self.big_seq
        small_seq = self.small_seq
        value = big_seq[0]
        if num <= value:
            big_seq.append(num)
            length_small = len(small_seq)
            length_big = len(big_seq)
            for i in range(0,length_big):
                big_seq = self.heapInsert_big(i)
            if self.isBigger_than_two(length_small,length_big) == 0:
                self.adjustment(0,length_small-1,length_big-1)
        else:
            small_seq.append(num)
            length_small = len(small_seq)
            length_big = len(big_seq)
            for i in range(0,length_small):
                small_seq = self.heapInsert_small(i)
            if self.isBigger_than_two(length_small,length_big) == 1:
                self.adjustment(1,length_small-1,length_big-1)

if __name__ == '__main__':
    me = Median()
    for i in range(0,11):
        num = random.randint(1,100)
        me.main(num)
    median = me.getMedian()
    print(median)
    
    # print(me.big_seq)
    # print(me.small_seq)
    # new_lst = me.big_seq + me.small_seq
    # print(sorted(new_lst))
    # value = (me.big_seq[0] + me.small_seq[0])/2
    # print(median,value)
