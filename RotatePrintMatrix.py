# practice

'''
    题目:给定一个整形正方形矩阵matrix,把该矩阵调整成顺时针旋转90度的样子
    思路:跟转圈打印矩阵一样，都是先确定正方形的第一个元素和最后一个元素的坐标，如果最后一个元素的坐标横纵坐标不相等则不能旋转，因为会越界。
         times是调整次数，假设是4*4正方形，那么应该最大的那一圈应该3个3个的调整，若为2*2,就1个1个调整。
    
'''

class RotatePrintMatrix:
    
    def __init__(self,matrix):
        self.matrix = matrix
        self.tR = 0
        self.tC = 0
        self.dR = len(matrix) - 1
        self.dC = len(matrix[0]) - 1 
    
    def printMatrix(self,matrix,tR,tC,dR,dC):
        times = dC - tC
        i = 0
        while i < times:
            tmp = matrix[tR][tC+i]
            matrix[tR][tC+i] = matrix[dR-i][tC]
            matrix[dR-i][tC] = matrix[dR][dC-i]
            matrix[dR][dC-i] = matrix[tR+i][dC]
            matrix[tR+i][dC] = tmp
            i += 1
        return matrix

    def main(self):
        if self.dR != self.dC:
            print('the matrix must be square!')
        else:        	
            while self.tR <= self.dR and self.tC <= self.dC:
                matrix = self.printMatrix(self.matrix,self.tR,self.tC,self.dR,self.dC)
                self.tR += 1
                self.tC += 1
                self.dR -= 1
                self.dC -= 1
            return matrix
          
if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    r = RotatePrintMatrix(matrix)
    matrix = r.main()
    print(matrix)
