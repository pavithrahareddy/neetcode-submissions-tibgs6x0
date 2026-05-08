class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights)-1
        res = 0
        while i<j:
            prod = min(heights[i],heights[j])*(j-i)
            res = max(res,prod)
            if heights[i]<=heights[j]:
                i = i+1
            else:
                j = j-1
        return res

        
        