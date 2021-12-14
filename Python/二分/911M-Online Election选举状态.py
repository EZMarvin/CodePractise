# 给出投票顺序 以及 投票时间 / 实现查询某个时间 谁得票最多的function

# 
from typing import List
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        vote = defaultdict(int)
        status = []
        top = -1
        vote[-1] = -1

        for i in persons:
            vote[i] += 1
            if vote[i] >= vote[top]:
                top = i
            status.append(top)
        
        self.status = status
        self.times = times


    def q(self, t: int) -> int:
        l,r = 0, len(self.times) - 1

        while l < r:
            mid = l + (r-l+1)//2
            if self.times[mid] <= t:
                l = mid
            else:
                r = mid - 1
                
        
        return self.status[l]
