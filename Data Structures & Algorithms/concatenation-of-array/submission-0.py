class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l = 2*n
        ans = [0]*l
        for i in range(len(nums)):
            ans[i] = nums[i]
        for i in range(len(nums)):
            ans[i+n] = nums[i]
        return ans