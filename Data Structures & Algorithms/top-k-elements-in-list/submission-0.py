class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i,0)
        top = [] * len(nums)
        for j in count:
            top[count[j]].append(j)
        res = []
        for m in range(len(top)-1,-1,-1):
            for l in top[m]:
                res.append(l)
                if len(res)==k:
                    return res
                


        