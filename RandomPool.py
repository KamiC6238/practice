# practice

'''
   设计一种结构,在该结构中有如下三个功能:insert(key):将某个key加入到该结构,做到不重复加入。
                                   delete(key):将原本在结构中的某个key移除
                                   getRandom():等概率随机返回结构中的任何一个key。
                                  【要求】 Insert、delete和getRandom方法的时间复杂度都是O(1)
   思路:使用两个哈希表，一个存放key value，一个存放相反的value key键值对，在python中字典可以当作哈希表使用。
       insert操作很简单，主要是delete操作。
       可以准备一个变量size用来表示哈希表中一共有多少个节点，在删除的时候，要注意到如果删除的是序号在0～size-1之间的，此时
       会出现漏洞，也就是说在getRandom中可能出现返回None的现象。
       因此让被删除的key与size最大的那个节点进行交换，随后将其删除即可。
       
   提醒:哈希表中节点存放的位置是无序的，节点之间也不一定是相邻的，这个解法只是利用了size对节点进行标号，
       让整体看起来像是有序的。
'''

import random

class RandomPool:

    def __init__(self):
        self.dict1 = dict()
        self.dict2 = dict()
        self.size = 0

    def insert(self, key):
        dict1 = self.dict1
        dict2 = self.dict2
        size = self.size
        res = dict1.get(key, None)
        if res is None:
            dict1[key] = size
            dict2[size] = key
            self.size += 1

    def delete(self, key):
        dict1 = self.dict1
        dict2 = self.dict2
        size = self.size
        if dict1.get(key, None) is None:
            return False
        number = dict1.get(key)
        key1 = dict2[size - 1]
        dict1[key1] = dict1[key]
        dict2[number] = dict2[size - 1]
        dict1.pop(key)
        dict2.pop(size - 1)
        self.size -= 1

    def getRandom(self):
        size = self.size
        d = self.dict2
        num = random.randint(0, size - 1)
        key = d.get(num)
        return key


if __name__ == '__main__':
    ran = RandomPool()
    ran.insert('a')
    ran.insert('b')
    ran.insert('c')
    ran.insert('d')
    ran.delete('c')
    print(ran.getRandom())
