class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res =""
        
        for s in range(len(strs[0])):
            for i in strs:
                if s == len(i) or i[s] != strs[0][s]:
                    return res
            res += strs[0][s]
        return res
