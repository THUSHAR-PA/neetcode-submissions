class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] > nums[i]:
                    a = nums[j]
                    nums[j] = nums[i]
                    nums[i] = a 
        