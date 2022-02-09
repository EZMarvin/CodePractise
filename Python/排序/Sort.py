
from typing import List
from collections import defaultdict 

class Solution:
    def quickSort(self, l : List[int]) -> List[int]:
        if len(l) <= 1:
            return l
        pivot = l[0]
        left = [x for x in l[1:] if x < pivot]
        right = [x for x in l[1:] if x >= pivot]
        return self.quickSort(left) + [pivot] + self.quickSort(right)

    def quick(self, arr : List[int], l:int, r:int) -> None:
        if r-l <= 1:
            return
        p = self.partation(arr, l, r)
        self.quick(arr, l, p - 1)
        self.quick(arr, p + 1, r)
        return l

    def partation(self, l : List[int], start : int, end : int) -> int:
        pivot = l[start]
        while start < end:
            while start < end and l[end] >= pivot:
                end -= 1
            l[start] = l[end]
            while start < end and l[start] <= pivot:
                start += 1
            l[end] = l[start]
        l[start] = pivot
        return start

    def mergeSort(self, l : List[int]) -> List[int]:
        if len(l) <= 1:
            return l
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]
        left = self.mergeSort(left)
        right = self.mergeSort(right)
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        if not left:
            return right
        if not right:
            return left
        result = []
        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        result += left
        return result + right
    

 
class Graph: 
    def __init__(self,vertices): 
        self.graph = defaultdict(list) 
        self.V = vertices
  
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    def topologicalSortUtil(self,v,visited,stack): 
  
        visited[v] = True
  
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        stack.insert(0,v) 
  
    def topologicalSort(self): 
        visited = [False]*self.V 
        stack =[] 
  
        for i in range(self.V): 
            if visited[i] == False: 
                self.topologicalSortUtil(i,visited,stack) 
  
        print (stack) 

s=Solution()
#print(s.quickSort([3,2,1,5,4]))
l = [3,2,1,5,4]
#s.quick(l, 0, len(l) - 1)
l = [[0 for _ in range(5)] * 5]
print(l)
    
        