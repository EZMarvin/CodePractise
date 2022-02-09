# 在 10 ** 6 的 矩阵中。 给定source & target 点, 以及 block的list。判定source是否能到达target
# block length <= 200
# 思路: 
# 正常用DFS/BFS 遍历看是否能到达 target
# 但是矩阵比起block数量大得多，所以转为看 block是否能包围source & target
# 判定 包围可以BFS 遍历看能到达点的数量是否能超过 block能围出的最大面积
# 最大面积是 block为斜边，用边界围绕的三角形
from typing import List
from collections import deque
class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        n = len(blocked)
        if n < 2:
            return True
        
        boundary = 10 ** 6
        blockSet = set(tuple(p) for p in blocked)

        def check(start, end):
            sx, sy = start
            ex, ey = end
            q = deque([(sx,sy)])
            s = set([(sx,sy)])
            cnt = n * (n - 1) // 2
            while q and cnt > 0:
                x, y = q.popleft()
                for nx,ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                    if 0 <= nx < boundary and 0 <= ny < boundary and (nx,ny) not in blockSet and (nx,ny) not in s:
                        if (nx,ny) == (ex,ey):
                            return 1
                        q.append((nx,ny))
                        cnt -= 1
                        s.add((nx,ny))
            
            if cnt > 0:
                return -1
            return 0

        if (res := check(source, target)) == 1:
            return True
        elif res == -1:
            return False
        else :
            res = check(target, source)
            if res < 0:
                return False
            return True
            
