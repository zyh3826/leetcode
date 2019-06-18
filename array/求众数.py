class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        count_dict = Counter(nums)
        sorted_dict = sorted(count_dict.items(), key=lambda d: d[1], reverse=True)
        return sorted_dict[0][0]
    
        # s2
        return sorted(nums)[len(nums) // 2]
