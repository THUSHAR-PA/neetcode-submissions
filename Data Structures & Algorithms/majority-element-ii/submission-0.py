class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {}
        a = []
        for i in nums:
            hashmap[i] = 1 + hashmap.get(i,0)
        length = len(nums)
        print (hashmap)
        for i,n in hashmap.items():
            if n > length // 3 :
                a.append(i)
        return a                