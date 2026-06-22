class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 1
        num_set = set()
        if len(nums) == 0:
            return 0
        for i in nums:
            num_set.add(i)
        for i in nums:
            length = 1
            
            current = i
            current_next = i+1
            if i-1 in num_set:
                continue
            while current_next in num_set:
                length +=1
                current = current_next
                current_next +=1
                max_length = max(max_length,length)
        return max_length

            