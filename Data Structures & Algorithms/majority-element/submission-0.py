class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        sor = sorted(hashmap.items(), key = lambda x:x[1],reverse = True)
        val = sor[0][0]    
        return val