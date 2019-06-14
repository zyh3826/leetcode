class Solution:
    def flipAndInvertImage(self, lists):
        n = len(lists[0])
        #h flip
        for l in range(n):
            lists[l].reverse()
            
        #0,1 invert
        for i in range(n):
            for j in range(n):
                lists[i][j] = (lists[i][j] == 0) + 0
                
        return lists
