# 取暖 input house位置列表 + 取暖器位置列表 / 求 最短可以覆盖所有house的供暖距离
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        houses.sort()

        nearheater = 0
        while nearheater < len(heaters) - 1 and heaters[nearheater] < houses[0]:
            nearheater += 1
        
        if nearheater == len(heaters) - 1:
            return houses[-1] - heaters[-1]
        
        ans = min(houses[0] - heaters[nearheater - 1], heaters[nearheater] - houses[0])
        if ans == houses[0] - heaters[nearheater - 1]:
            nearheater = nearheater - 1
        
        for index,house in enumerate(houses):
            
            if house <= heaters[nearheater] + ans:
                continue
            
            if nearheater == len(heaters) - 1:
                if index != len(houses)-1:
                    continue
                ans = house - heaters[nearheater]
                break
            
            nextheater = nearheater + 1
            while nextheater < len(heaters)-1 and heaters[nextheater] < house:
                nextheater += 1

            if (heaters[nextheater] - house) > (house - heaters[nearheater]):
                ans = house - heaters[nearheater]
            else:
                nearheater = nextheater
                ans = heaters[nearheater] - house
        
        return ans
                
# 二分 + 排序
# 查看每个house在heater中的最短供暖距离，
s = Solution()
a = [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923]
b = [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]

print(s.findRadius(a,b))
            
            