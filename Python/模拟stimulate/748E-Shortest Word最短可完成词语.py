# 给出车牌，以及词汇串 / 给出能完成车牌字母的最短词汇
from collections import Counter
from typing import List
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        count = [0] * 26
        l = 0
        ans = ''
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        
        for i in words:
            if not cnt - Counter(i):
                if ans == '' or len(ans) > len(i):
                    ans = i

        return ans

### shorter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        return min((word for word in words if not cnt - Counter(word)), key=len)
