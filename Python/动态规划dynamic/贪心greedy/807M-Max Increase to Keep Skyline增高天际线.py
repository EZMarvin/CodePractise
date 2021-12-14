# 给出矩阵，数值代表高度。/ 从行或者列方向看会有天际线 / 保证天际线不变，可以给所有建筑增高的数值总和
from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxrow = []
        ans = 0
        for i in grid:
            m = max(i)
            maxrow.append(m)
        for i in range(len(grid[0])):
            cm = max([m[i] for m in grid])
            for j in range(len(grid)):
                ans += min(cm,maxrow[j]) - grid[j][i]
        
        return ans
        
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rowMax = list(map(max, grid))
        colMax = list(map(max, zip(*grid)))
        return sum(min(rowMax[i], colMax[j]) - h for i, row in enumerate(grid) for j, h in enumerate(row))