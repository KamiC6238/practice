# practice

'''
   题目:给定一个矩形matrix,按照“之”字形的方式打印这个矩阵
   
   思路:如果按照常规的想法，想着怎么从这个坐标换到另外一个坐标，那么这个题将会很难解。因此要宏观的去看待这道题(现学现用左神的话）。
        1.设置两个坐标，分别为A(tR,tC),B(dR,dC),起始值都为0,0，再设置一个布尔变量判断当前打印应该是斜右向上打印还是斜左向下打印。
        2.每次打印完，A坐标向右移动一个位置，B坐标向下移动一个位置,这样每次两个坐标之间就会形成对角线，也就是我们要的之字形
        3.判断两个坐标是否到达边界，到达的话需要对坐标做相应的改动
      
   感悟:题目的思路很简单，但是一下手就发觉自己的coding能力很差，频频报错，还需要多加练习。
'''

class ZigZagPrintMatrix:

    def __init__(self,matrix):
        self.tR = 0
        self.tC = 0
        self.dR = 0
        self.dC = 0
        self.bool = False
        self.matrix = matrix
        self.endR = len(matrix) - 1       # 下边界
        self.endC = len(matrix[0]) - 1    # 右边界

    def printMatrix(self,matrix,tR,tC,dR,dC):
        if self.bool:
            while tR != dR + 1:
                print(str(matrix[tR][tC]) + ' ',end="")
                tR += 1
                tC -= 1
        else:
            while dR != tR - 1:
                print(str(matrix[dR][dC]) + ' ',end="")
                dR -= 1
                dC += 1

    def main(self):
        while self.tR != self.endR + 1:
            self.printMatrix(self.matrix,self.tR,self.tC,self.dR,self.dC)
            if self.tC == self.endC:
                self.tR += 1
            else:
                self.tC += 1
            if self.dR == self.endR:
                self.dC += 1
            if self.dR != self.endR:
                self.dR += 1
                
            if self.bool:
                self.bool = False
            else:
                self.bool = True

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    z = ZigZagPrintMatrix(matrix)
    z.main()
