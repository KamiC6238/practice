# practice

'''
 荷兰国旗问题，问的是给定一个整数数组和一个划分值num，小于num的放在数组左边，等于num的放中间，大于num的放在数组右边
 思路:设定初始值less = -1,more = len(seq),cur = 0
      less表示小于num的区域,more表示大于num的区域，若seq[cur] < num，则与小于区域的前一个数交换，之后cur += 1，若等于num，则cur += 1,
      若seq[cur] > num，则让seq[cur]与大于区域的前一个数交换，随后more -= 1
      之所以这里cur不用加1是因为在和大于区域的前一个数进行交换的时候，这个交换过来的数跟num之间的大小关系是未确定的，因此需要进行下一次判断。
'''

import random

def netherland_flag(seq,num):
    if len(seq) < 2:
        return seq
    less = -1
    more = len(seq)
    cur = 0
    while cur < more:
        if seq[cur] < num:
            seq[cur],seq[less+1] = seq[less+1],seq[cur]
            cur += 1
            less += 1
        elif seq[cur] == num:
            cur += 1
        else:
            seq[cur],seq[more-1] = seq[more-1],seq[cur]
            more -= 1
    return seq

if __name__ == '__main__':
    seq = list(range(random.randint(1,15)))
    length = len(seq)
    num = random.randint(1,length-1)
    random.shuffle(seq)
    seq = netherland_flag(seq,num)
    print(num)
    print(seq)
