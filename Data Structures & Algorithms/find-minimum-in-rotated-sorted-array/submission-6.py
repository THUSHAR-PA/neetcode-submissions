class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mini = float("inf")
        while l <= r:
            mid = (l+r)//2
            mini = min(mini,nums[mid])
            if nums[r] <= nums[mid] :
                if l == mid and nums[r] < nums[mid]:
                    return nums[r]
                l = mid + 1
            elif nums[l] <= nums[mid] or nums[r]>nums[mid]:
                r = mid - 1

        return mini            
