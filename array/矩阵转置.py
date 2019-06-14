class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        row = len(A)
        col = len(A[0])
        A_trans = []
        for i in range(col):
            A_trans.append([0] * row)
            
        for i in range(len(A[0])):
            for j in range(len(A)):
                A_trans[i][j] = A[j][i]
