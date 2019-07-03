class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numsLen = len(nums)
        l = set(list(range(1, numsLen+1)))
        return list(l - set(nums))
        # other solution: https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/
