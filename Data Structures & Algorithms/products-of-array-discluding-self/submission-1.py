class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfic = 1
        output = [1]*len(nums)
        for i in range(len(nums)):

            output[i] = output[i]*prefix
            prefix *= nums[i]
        for i in range(len(nums)-1,-1,-1):
            output[i] = output[i]*postfic
            postfic *= nums[i]
        return output