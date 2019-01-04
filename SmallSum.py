# practice


'''
   题目:小和问题。在一个数组中，每一个数左边比当前数小的数累加起来，叫做这个数组的小和。求一个数组的小和。
   思路:利用归并的思想，求一个数的左边有多少个小于该数的，相当于可以变相的求该数右边有多少个比该数大的数，然后将大于该数的数的个数乘以该数的值，
        即为该数的小和，每个数都这样做，最后累加起来就是整个数组的小和
   
   感悟:网络上python版本的小和问题相对较少，自以为对python的语法有一定程度的熟悉了，结果在写的时候还是马马虎虎，还是coding,coding,coding。
'''

import random

class SmallSum:

    def __init__(self):
        self.res = 0

    def merge_sort(self,seq):
        if len(seq) < 2:
            return seq
        mid = int(len(seq)//2)
        sorted_left = self.merge_sort(seq[:mid])
        sorted_right = self.merge_sort(seq[mid:])
        seq = self.merge(sorted_left,sorted_right)
        return seq
   
    def merge(self,sorted_left,sorted_right):
        length_left = len(sorted_left)
        length_right = len(sorted_right)
        sorted_seq = list()
        a = b = 0
        while a < length_left and b < length_right:
            if sorted_left[a] > sorted_right[b]:
                self.res += 0
                sorted_seq.append(sorted_right[b])
                b += 1
            else:
                self.res += (len(sorted_right)-b) * sorted_left[a]
                sorted_seq.append(sorted_left[a])
                a += 1
        while a < length_left:
            sorted_seq.append(sorted_left[a])
            a += 1
        while b < length_right:
            sorted_seq.append(sorted_right[b])
            b += 1
        return sorted_seq
    
    def smallsum(self,seq):
        self.merge_sort(seq)
        print(self.res)

if __name__ == '__main__':
    # seq = list()
    # for i in range(10):
    #     seq.append(i)
    # random.shuffle(seq)
    seq = [1,3,4,2,5]
    s = SmallSum()
    s.smallsum(seq)
