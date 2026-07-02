class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap ={}
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        for value in hashmap.values():
            if value > 1:
                return True
        return False