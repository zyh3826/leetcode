class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        try:
            while True:
                nums.remove(0)
                count += 1
        except ValueError:
            pass
        nums += [0] * count
