class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            count = [0]*26
            for letter in word:
                count[ord(letter)-ord('a')] = 1 + count[ord(letter)-ord('a')]
            groups[tuple(count)].append(word)
        return list(groups.values())