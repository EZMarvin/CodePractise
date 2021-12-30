
class KMP:
    
    def __init__(self,pat) -> None:
        self.pat = pat
        l = len(pat)
        self.dp = [[0 for _ in range(26)] for _ in range(l)]

        self.dp[0][ord(pat[0]) - ord('a')] = 1

        # shadow 状态表示与当前状态有相同的前缀，目的是尽可能少回退
        shadow = 0
        for i in range(1,l):
            for j in range(26):
                self.dp[i][j] = self.dp[shadow][j]
            self.dp[i][ord(pat[i]) - ord('a')] = i + 1
            shadow = self.dp[shadow][ord(pat[i]) - ord('a')]
    
    def search(self,s : str) -> int:
        m = len(self.pat)
        n = len(s)

        status = 0

        for i in range(n):
            status = self.dp[status][ord(s[i]) - ord('a')]
            if status == m:
                return i - m + 1
        return -1

t = KMP('test')
print(t.search('abteatestvc'))
