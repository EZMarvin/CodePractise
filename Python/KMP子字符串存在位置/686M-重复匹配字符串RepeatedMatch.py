# 给出字符串a & b，求a最小的重复次数，使得b出现在新字符串中。
# -1 如果不存在


class Solution:
    def strstr(self, a: str, b: str) -> int:
        n,m = len(a),len(b)
        if m == 0:
            return 0
        
        pi = [0] * m
        j = 0
        for i in range(1,m):
            while j > 0 and b[i] != b[j]:
                j = pi[j-1]
            if b[i] == b[j]:
                j+=1
            pi[i] = j
        
        i, j = 0, 0
        while i - j < n:
            while j > 0 and a[i] != b[j]:
                j = pi[j-1]
            if a[i % n] == b[j]:
                j += 1
            if j == m:
                return i - m + 1 
            i += 1
        return -1

    def repeatedStringMatch(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        index = self.strstr(a, b)
        if index == -1:
            return -1
        if n - index >= m:
            return 1
        return (m + index - n - 1) // n + 2