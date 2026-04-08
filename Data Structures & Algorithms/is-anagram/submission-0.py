class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        i,j = 0,len(s)-1
        while i<j:
            if s[i]!=t[j]:
                return False
            i = i+1
            j =j-1