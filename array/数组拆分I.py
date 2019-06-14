class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # s1
        #nums = sorted(nums)
        #sums = 0
        #for i in range(0, len(nums), 2):
        #    sums += nums[i]
        #return sums
        # s2
        return sum(sorted(nums)[::2])
