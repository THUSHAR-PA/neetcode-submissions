class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap ={}
        for i in s:
            hashmap[i] = hashmap.get(i,0)+1
        for i in t:
            if hashmap.get(i,0) == 0:
                return False
            else:
                hashmap[i] -= 1
        for value in hashmap.values():
            if value != 0:
                return False
        return True