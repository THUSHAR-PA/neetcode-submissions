class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0)+1
        for i,n in hashmap.items():
            if n > 1:
                return i
        