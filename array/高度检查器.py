class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_list = sorted(heights)
        return sum([heights[i] != sorted_list[i] for i in range(len(heights))])
