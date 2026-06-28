class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmap={}
        if len(s2) < len(s1):
            return False

        for i in range(len(s1)):
            hashmap[s1[i]] = hashmap.get(s1[i],0)+1

        k = len(s1)
        l = 0
        for r in range(len(s2)):
            if s2[r] in hashmap:
                hashmap[s2[r]] -=1
            if r-l+1 > len(s1):
                if s2[l] in hashmap:

                    hashmap[s2[l]] +=1
                l+=1
            if r-l+1 == k:
                valid = True
                for value in hashmap.values():
                    if value != 0:
                        valid =False
                if valid ==True:
                    return True
        return False



