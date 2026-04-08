class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for i in strs:
            res = res + str(len(i)) + '#' + i
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i<len(s):
            length = ''
            while s[i]!='#':
                length = length + s[i]
                i = i + 1
            res.append(s[i+1:i+1+int(length)]) 
            i  = i+1+int(length)
        return res


