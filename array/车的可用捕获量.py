class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # find rook
        flag = 0
        for i in range(8):
            for j in range(8):
                if board[i][j] == "R":
                    x = i
                    y = j
                    flag = 1
                    break
            if flag:
                break
        
        R_loc = [x, y]
        #print("R_loc: " R_loc)
        cap_num = 0
        derection = [1, -1]
        # move
        for d in derection:
            for k in range(2):
                for i in range(((1 + d) * (8 - R_loc[k]) + (1 - d) * R_loc[k]) // 2 - 1):
                    R_loc[k] += d
                    #print("d: {}, k: {}, R[k]: {}".format(d, k, R[k]))
                    if board[R_loc[0]][R_loc[1]] == "p":
                        cap_num += 1
                        break
                    elif board[R_loc[0]][R_loc[1]] == "B":
                        break
                R_loc = [x, y]       
        return cap_num
                    
