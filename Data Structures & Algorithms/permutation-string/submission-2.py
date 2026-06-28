class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        hashmap={}
        for ch in s1:
            hashmap[ch] = hashmap.get(ch,0)+1
        l =0 
        k =len(s1)
        for r in range(len(s2)):
            if s2[r] in hashmap:
                hashmap[s2[r]] -= 1
            if r-l+1 > k:
                if s2[l] in hashmap:
                    hashmap[s2[l]] += 1
                l+=1
            if r-l+1 == k:
                valid = True
                for value in hashmap.values():
                    if value != 0:
                        valid = False
                if valid == True:
                    return True
        return False
                
