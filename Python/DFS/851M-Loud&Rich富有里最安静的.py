# 输入 一个（a,b)元组list + 安静程度 list。
# 元组表示 a > b
# 求输出List，每个位置 比自己富有的人里(包含自己) 最安静的的人

from typing import Deque, List
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        track = [[i] for i in range(len(quiet))]
        for a, b in richer:
            track[b].append(a)
        ans = [-1 for _ in range(len(quiet))]

        ## 记忆搜索
        def dfs(i):
            if ans[i] != -1:
                return ans[i]
            q = i
            if len(track[i]) == 1:
                ans[i] = q
                return q
            for index in track[i]:
                if index == i:
                    continue
                m = dfs(index)
                if quiet[m] < quiet[q]:
                    q = m 
            ans[i] = q
            return q

        for i in range(len(quiet)):
            if ans[i] == -1:
                ans[i] == dfs(i)
        
        return ans

# 拓扑排序
# 从最富有的开始算 联系list 入度list
# 队列遍历
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        track = [[] for _ in range(n)]
        indig = [0 for _ in range(n)]
        for a, b in richer:
            track[a].append(b)
            indig[b] += 1

        ans = list(range(n))

        q = Deque(i for i,j in enumerate(indig) if j == 0)
        ## 记忆搜索
        while q :
            node = q.popleft()
            for y in track[node]:
                if quiet[ans[node]] < quiet[ans[y]]:
                    ans[y] = ans[node]
                indig[y] -= 1
                if indig[y] == 0:
                    q.append(y)
                
        return ans 


