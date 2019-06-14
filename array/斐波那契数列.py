class Solution:
    def fib(self, N: int) -> int:
        #s 1
        #if N == 0:
        #    return 0
        #elif N == 1:
        #    return 1
        #else:
        #    return self.fib(N - 1) + self.fib(N - 2)
        
        #s 2
        f0 = 0
        f1 = 1
        while(N >= 1):
            f0, f1 = f1, f0 + f1
            N -= 1
            
        return f0
