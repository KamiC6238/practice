# practice

'''
    题目:转圈打印矩阵
    思路:记录矩阵的第一个元素和最后一个元素的坐标，设第一个元素的坐标为tR,tC,最后一个元素的坐标为dR,dC.有三种情况
         1.当tR=dR时，说明矩阵只有一行，因此通过while打印后tC+=1即可
         2.当tC=dC时，说明矩阵只有一列，情况跟第一种一样
         3.当tR<=dR且tC<=dC时，说明此时是一个n*m矩阵，需要多设置两个变量curR和curC来控制打印的走向
'''

class PrintMatrixLoop:
    
    def __init__(self,matrix):
        self.tR = 0
        self.tC = 0
        self.dR = len(matrix) - 1
        self.dC = len(matrix[0]) - 1
        self.matrix = matrix

    def print_matrix(self,matrix,tR,tC,dR,dC):
        if tR == dR:
            while tC <= dC:
                print(str(matrix[tR][tC]) + ' ',end="")
                tC += 1
        elif tC == dC:
            while tR <= dR:
                print(str(matrix[tR][tC]) + ' ',end="")
                tR += 1
        else:
            curR = tR
            curC = tC
            while curC < dC:
                print(str(matrix[tR][curC]) + ' ',end="")
                curC += 1
            while curR < dR:
                print(str(matrix[curR][dC]) + ' ',end="")
                curR += 1
            while curC > tC:
                print(str(matrix[curR][curC]) + ' ',end="")
                curC -= 1
            while curR > tR:
                print(str(matrix[curR][tC]) + ' ',end="")
                curR -= 1

    def main(self):
        tR = self.tR
        tC = self.tC
        dR = self.dR
        dC = self.dC
        while tR <= dR and tC <= dC:
            self.print_matrix(self.matrix,tR,tC,dR,dC)
            tR += 1
            tC += 1
            dR -= 1
            dC -= 1

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    m = PrintMatrixLoop(matrix)
    m.main()
