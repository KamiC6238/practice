# practice

'''
   题目:给定一个行和列都排好序的N*M整形矩阵matrix和一个整数k，判断k是否在matrix中，存在返回True,不存在返回False
        要求时间复杂度O(N+M)
        
   思路:1.将寻找的起点定在矩阵的右上角坐着左下角，代码中是右上角。
        2.设置起点的值为cur,坐标为(tR,tC),要寻找的值为num
        3.如果num大于cur,因为有序的原因，cur左边的都是比cur小的，因此不需要寻找，所以tR += 1
        4.如果num小于cur,同理此时tC -= 1
        5.如果相等，返回True，否则返回False
        
   感悟:其实很多题都是我第一次接触，直接让我做肯定写不来，但总要尝试，多写就会有思路了。
        一些细节比如边界的处理还是不到位，思考的不全面。Coding能力还是很差。
'''

class FindNumInSortedMatrix:
    
    def __init__(self,matrix):
        self.matrix = matrix
        self.endR = len(matrix) - 1
        self.endC = len(matrix[0]) - 1
        self.endL = 0

    def find_num(self,num):
        matrix = self.matrix
        endR = self.endR
        endC = self.endC
        endL = self.endL
        tR = 0
        tC = endC
        while tR >= endL and tR <= endR and tC >= endL:
            cur = matrix[tR][tC]
            if num > cur:
                tR += 1
            elif num < cur:
                tC -= 1
            elif num == cur:
                return True
        return False

if __name__ == '__main__':
    matrix = [[1,3,5,6],[2,5,7,9],[4,6,8,10]]
    res = FindNumInSortedMatrix(matrix)
    print(res.find_num(0))
