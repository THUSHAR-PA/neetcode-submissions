class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        r = k
        l = 0
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp[nums[i]] <= k:
                return True 
            mp[nums[i]] = i
        return False