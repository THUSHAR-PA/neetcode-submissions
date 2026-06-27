class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = set()
        l = 0
        max_length = 0
        for i in range(len(s)):
            while s[i] in sub_string:
                sub_string.remove(s[l])
                l+=1
            sub_string.add(s[i])
            length = len(sub_string)
            max_length = max(max_length,length)


            
        return max_length


        