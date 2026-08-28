class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = l = 1
        n = len(nums)
        while r < n:
            if nums[r-1] != nums[r]:
                nums[l] = nums[r]
                l+=1
            r+=1
        return l