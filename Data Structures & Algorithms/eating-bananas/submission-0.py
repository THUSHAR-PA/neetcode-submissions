class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        res = r 
        while l <=r:
            hrs = 0
            mid = (l+r)//2
            for i in piles:
                hrs+= math.ceil(i/mid)
            if hrs > h:
                l = mid + 1
            else :
                res = min(res,mid)
                print(res)
                r = mid - 1
        return res
            
