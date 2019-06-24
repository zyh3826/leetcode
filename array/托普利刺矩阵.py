class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        row = len(matrix)
        col = len(matrix[0])
        
        if row == 1 or col == 1:
            return True
        
        #初始化colA，rowA，colB，rowB
        rowA, colA = 0, col - 1
        rowB, colB = 0, col - 1
        
        for _ in range(row + col - 3):
            if colA > 0:
                colA -= 1
            else:
                rowA += 1
                
            if rowB < row - 1:
                rowB += 1
            else:
                colB -= 1
                
            sub_list = [matrix[i][j] for i, j in zip(range(rowA, rowB+1), range(colA, colB+1))]
            if len(set(sub_list)) != 1:
                return False
        return True
