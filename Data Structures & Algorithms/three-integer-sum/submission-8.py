class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        i = 0
        j = i+1
        k = len(nums)-1 
        nums.sort()
        res = []
        while j<k:
            if nums[i]+nums[j]+nums[k] == 0:
                res.append([nums[i],nums[j],nums[k]])
            if nums[i]+nums[j]+nums[k] < 0:
                j = j+1
            if nums[i]+nums[j]+nums[k] > 0:
                k = k-1
        return res