class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = []
        if not A:
            return res
        if len(A) == 1:
            res = A[0].split()
            return res
        setkey = set(A[0])
        for k in setkey:
            num = min([a.count(k) for a in A])
            res += [k] * num
            
        return res
