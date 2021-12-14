# 输入course list， （需要时间，必须修完的时间点） 不能同时修课。 求最多能修几门
# 贪心证明
# t1, d1 / t2, d2 / d2 > d1 情况下先选t1最优

from typing import List
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key = lambda c:c[1])

        q = []
        total = 0

        for ti,di in courses:
            if total + ti < di:
                total += ti
                heapq.heappush(q,-ti)
            elif q and -q[0] > ti:
                total = total + q[0] + ti
                heapq.heappop(q)
                heapq.heappush(q,-ti)
        
        return len(q)
