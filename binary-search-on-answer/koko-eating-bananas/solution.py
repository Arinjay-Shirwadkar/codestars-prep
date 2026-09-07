import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,u = 1,max(piles)
        while l<=u:
            mid = l+(u-l)//2
            hours=0
            hours =sum((pile+ mid- 1)//mid for pile in piles)
            if hours<=h:
                optimal = mid
                u=mid-1
            else:
                l=mid+1
        return optimal