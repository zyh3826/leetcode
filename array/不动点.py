class Solution:
    def fixedPoint(self, A: List[int]) -> int:
        fixed_point = [x for x in A if x == A.index(x)]
        if len(fixed_point) == 0:
            return -1
        return fixed_point[0]
