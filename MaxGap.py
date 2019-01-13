# practice

'''
    题目:一个无序数组排序后，求相邻两数的最大差值,要求不能用基于比较的算法。
    
    思路:不能基于比较的算法，可以用桶排序，但这个题目并不是用桶排序来解决，只是借用了桶排序的概念。
         假设数组有n个数，每个数都放到自己对应的桶中，这样就能实现数组的有序化。
         由此产生的问题就是相邻两数可能来自同一个桶，也可能来自相邻的桶，如果要把桶内的数也比较了，显然就很费时间。
         因此解决办法是，如果有n个数，就准备n+1个桶，让最小值放在第一个桶，最大值放在最后一个桶，从而在第一和最后
         一个桶中，必然有一个空桶，所以空桶左边离空桶最近的桶的最大值和空桶右边离空桶最近的桶的最小值是相邻的，
         并且最大差值至少有一个空桶的大小这么大。
         由于空桶的存在，使得我们只需要求桶的最大值和最小值即可，也就是说可以忽略桶里的其他元素，从而化简了这个过程。
         
         getbid方法比较妙的地方在于它能够使整个数组的最小值放在第一个桶，最大值放在最后一个桶，从而确保空桶存在于这
         两个桶之间。
'''

import sys
import random

class MaxGap:
    
    def __init__(self):
        self.max_num = -sys.maxsize
        self.min_num = sys.maxsize
        self.seq = list()

    def max_gap(self):
        seq = self.seq
        length = len(seq)
        for i in range(0,length):
            self.max_num = max(seq[i],self.max_num)
            self.min_num = min(seq[i],self.min_num)
        max_num = self.max_num
        min_num = self.min_num
        if max_num == min_num:     # 若数组中的最大值等于最小值，说明数组长度为1，直接返回0即可
            return 0
        hasnum = [False] * (length + 1)  # 判断桶中是否有数，初始值全为False
        maxs = [None] * (length + 1)     # 每个桶的最大值
        mins = [None] * (length + 1)     # 每个桶的最小值
        for i in range(0,length):
            bid = self.getbid(seq[i],length,max_num,min_num)  # 判断数应该进入哪个桶
            if hasnum[bid] is False:
                maxs[bid] = seq[i]
                mins[bid] = seq[i]
            else:
                maxs[bid] = max(maxs[bid],seq[i])
                mins[bid] = min(mins[bid],seq[i])
            hasnum[bid] = True
        lastmax = maxs[0]
        res = 0
        for i in range(1,length):					# 桶和桶之间的最大差值就是右边的桶的最小值减去左边桶的最大值
            if hasnum[i]:
                res = max(res,mins[i] - lastmax)
                lastmax = maxs[i]
        return res
    
    def getbid(self,num,len,max_num,min_num):
        return int(((num-min_num) * len)/(max_num-min_num))	# 保证了最小的数一定放在第一个桶，最大的数放在最后一个桶

if __name__ == '__main__':
    m = MaxGap()
    for i in range(0,10):
        value = random.randint(1,50)
        m.seq.append(value)
    print(m.seq)
    print(m.max_gap())
