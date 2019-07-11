"""包含整数的二维矩阵 M 表示一个图片的灰度。你需要设计一个平滑器来让每一个单元的灰度成为平均灰度 (向下舍入) ，平均灰度的计算是周围的8个单元和它本身的值求平均，如果周围的单元格不足八个，则尽可能多的利用它们。

示例 1:

输入:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
输出:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0
注意:

给定矩阵中的整数范围为 [0, 255]。
矩阵的长和宽的范围均为 [1, 150]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/image-smoother
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
class Solution:
    def imageSmoother(self, M):
        direction = {"up": [0, -1],
                     "down": [0, 1],
                     "left": [-1, 0],
                     "right": [1, 0],
                     "right-up": [1, -1],
                     "left-up": [-1, -1],
                     "right-down": [1, 1],
                     "left-down": [-1, 1]
                     }
        zerosList1 = [0] * (len(M[0]) + 2)
        res = []
        M.append(zerosList1)
        M.insert(0, zerosList1)
        res = [[0] * (len(M[0]) - 2) for _ in range(1, len(M)-1)]
        for i in range(1, len(M)-1):
            M[i].append(0)
            M[i].insert(0, 0)
        for i in range(1, len(M)-1):
            for j in range(1, len(M[0])-1):
                s = 0
                s += M[i][j]
                for k in direction.keys():
                        s += M[i + direction[k][0]][j + direction[k][1]]
                if ((j == 1 or j == len(res[0])) and (i > 1 and i < len(res))) or ((i == 1 or i == len(res)) and (j > 1 and j < len(res[0]))):
                    if len(res) == 1 or len(res[0]) == 1:
                        s //= 3
                    else:
                        s //= 6
                elif (i > 1 and i < len(res)) and (j > 1 and j < len(res[0])):
                    s //= 9
                else:
                    if len(res) == 1 and len(res[0]) == 1:
                        s //= 1
                    elif len(res) == 1 or len(res[0]) == 1:
                        s //= 2
                    else:
                        s //= 4
                res[i-1][j-1] = s
        return res
#更好的办法：https://leetcode-cn.com/problems/image-smoother/solution/gou-zao-xin-ju-zhen-lao-ju-zhen-jin-xing-bian-li-p/
