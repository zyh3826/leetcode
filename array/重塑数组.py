class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        nums_r = len(nums)
        nums_c = len(nums[0])
        if nums_r * nums_c != r * c:
            return nums
        
        nums_flatten = []
        for i in range(nums_r):
            nums_flatten += nums[i]
        
        idx = 0
        reshaped_mat = []
        for i in range(r):
            row = [None for _ in range(c)]
            for j in range(c):
                row[j] = nums_flatten[idx]
                idx += 1
            reshaped_mat.append(row)
            
        return reshaped_mat
        
