import copy
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0 or rowIndex == 1:
            return [1] * (rowIndex + 1)
        
        a, b = [1] * (rowIndex + 1), [1] * (rowIndex + 1)
        for k in range(2, rowIndex+1):
            for i in range(1, k):
                b[i] = a[i] + a[i-1]
            #a = b 错误，查看深浅copy的区别
            a = copy.deepcopy(b)
            
        return b
