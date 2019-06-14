class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even_num = []
        odd_num = []
        for i in range(len(A)):
            if A[i] % 2 == 0:
                even_num.append(A[i])
            else:
                odd_num.append(A[i])
                
        return even_num + odd_num
