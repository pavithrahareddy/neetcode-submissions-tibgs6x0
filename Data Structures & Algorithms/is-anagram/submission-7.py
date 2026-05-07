class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc = {}
        tc = {}
        if len(s)!=len(t):
            return False
        for i in range(0,len(s)):
            sc[s[i]] = 1 + sc.get(s[i],0)
            tc[t[i]] = 1 + tc.get(t[i],0)
        if sc!=tc:
            return False
        return True
        