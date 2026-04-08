class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        scounts = defaultdict(list)
        for s in strs:
            count = [0]*26
            for i in s:
                count[ord(i)-ord('a')] = 1 + count[ord(i)-ord('a')]
            scounts[tuple(count)].append(s)
        return list(scounts.values())

            
        