class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "#" + i
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        newl = 0
        while i<len(s):
            l = ""
            while s[i]!="#":
                l = l + s[i]
                i = i + 1
            newl = int(l)
            res.append(s[i+1:i+1+newl])
            i = i + 1 +newl
        return res


