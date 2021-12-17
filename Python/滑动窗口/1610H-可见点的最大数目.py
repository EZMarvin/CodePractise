# 输入 点 List + 主角点 + 可视角度 / 求最多能同时看到几个点
# 极点 + 滑动窗口
from math import atan2
from math import pi
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        relativeToX = []
        sameCnt = 0
        for node in points:
            if node == location:
                sameCnt += 1
# 重点1 : atan2
            else:
                relativeToX.append(atan2(node[1]- location[1], node[0] - location[0]))
        
        relativeToX.sort()
        n = len(relativeToX)
# 跨象限情况 处理
        relativeToX += [deg + 2 * pi for deg in relativeToX]

        maxCnt = 0
        right = 0
        degree = angle * pi / 180
# 滑动窗口
        for i in range(n):
            while right < n * 2 and relativeToX[right] <= relativeToX[i] + degree:
                right += 1
            maxCnt = max(maxCnt, right - i)
        return maxCnt + sameCnt
