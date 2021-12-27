# list 表示每个人的age， X 能向 Y 发起好友请求的条件如下 
#age[y] > 0.5 * age[x] + 7
#age[y] <= age[x]
# 求 总共会有多少条请求

# 排序 加 双指针
from typing import List
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        allow = [i for i in ages if i > 14]
        allow.sort()
        ans = 0

        def findnoless(i, j, target):
            left = i 
            right = j
            while left < right:
                mid = left + (right - left) // 2
                if allow[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        i = len(allow) - 1
        while i > 0:
            same = 1
            while i > 0 and allow[i] == allow[i - 1]:
                i -= 1
                same += 1
            end = findnoless(0, i, allow[i] * 0.5 + 7)

            ans += same * (i - end) + same * (same - 1)
            i -= 1
        return ans

# 排序 双指针 双指针 在遍历时 不断移动（单调递增）。指针差为符合当前年龄人数

# 由于年龄范围 不大，可以单独count 每个年龄人数，并计算 前缀人数 
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt = [0] * 121
        for age in ages:
            cnt[age] += 1
        pre = [0] * 121
        for i in range(1, 121):
            pre[i] = pre[i - 1] + cnt[i]
        
        ans = 0
        for i in range(15, 121):
            if cnt[i] > 0:
                bound = int(i * 0.5 + 8)
                ans += cnt[i] * (pre[i] - pre[bound - 1] - 1)
        return ans
