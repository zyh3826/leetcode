class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        yanghui_mat = []
        
        for i in range(numRows):
            row = [None for _ in range(i+1)]
            row[0], row[-1] = 1, 1
            
            for j in range(1, len(row) - 1):
                row[j] = yanghui_mat[i - 1][j - 1] + yanghui_mat[i - 1][j]
                
            yanghui_mat.append(row)
            
        return yanghui_mat
