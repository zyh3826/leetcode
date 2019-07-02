class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLength = 1
        lenCount = 1
        try:
            idx = nums.index(1) #find the frist 1
        except ValueError:
            return 0
        i = idx + 1
        while i < len(nums):
            if nums[i] == 1:
                lenCount += 1
                #if lenCount > maxLength:
                    #maxLength = lenCount
                maxLength = max(maxLength, lenCount)
            else:
                lenCount = 0
            i += 1
        return maxLength
                
            
