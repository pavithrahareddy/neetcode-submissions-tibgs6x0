class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res = res + str(len(i)) + "#" + i
        return res


    def decode(self, s: str) -> List[str]:
        i,res = 0,[]
        while i<len(s):
            length = ""
            while s[i]!="#":
                length += (s[i])
                i = i + 1
            word = ""
            for char in range(i+1,i+1+int(length)):
                word += (s[char])
            res.append(word)
            i = i+1+int(length)
        return res
            

