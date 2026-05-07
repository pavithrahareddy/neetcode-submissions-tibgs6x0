class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "#" + i
        return res


    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i <len(s):
            l = ""
            while s[i]!="#":
                l = l+s[i]
                i=i+1
            new = i+1+int(l)
            res.append(s[i+1:new])
            i = new
        return res


