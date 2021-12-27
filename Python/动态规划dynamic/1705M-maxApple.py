# apple list 表示每天得到的苹果数目， days表示每天得到苹果保质期长度
# 每天最多吃1个苹果，求最多能吃多少苹果
import heapq
from typing import List
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq = []
        ans = 0
        i = 0
        heapq.heapify(pq)
        while i < len(apples):
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if apples[i]:
                heapq.heappush(pq, [i + days[i],apples[i]])
            if pq:
                pq[0][1] -= 1
                if pq[0][1] == 0:
                    heapq.heappop(pq)
                ans += 1
            i += 1
        # 超出days 范围
        while pq:
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if len(pq) == 0:
                break
            p = heapq.heappop(pq)
            a = min(p[1], p[0]-i)
            i += a
            ans += a
            
        
        return ans