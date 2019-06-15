class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        even_nums = []
        odd_nums = []
        for i in A:
            if i & 1 == 0:
                even_nums.append(i)
            else:
                odd_nums.append(i)
                
        res=[]        
        for even_num, odd_num in zip(even_nums, odd_nums):
            res.append(even_num)
            res.append(odd_num)
            
        return res
