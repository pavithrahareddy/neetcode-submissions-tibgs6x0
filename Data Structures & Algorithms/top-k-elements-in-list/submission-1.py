class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num,0)
        group = [[] for i in range(len(nums)+1)]
        for key in count:
            group[count[key]].append(key)
        res = []
        for i in range(len(group)-1,0,-1):
            for v in group[i]:
                res.append(v)
                if len(res)==k:
                    return res




        