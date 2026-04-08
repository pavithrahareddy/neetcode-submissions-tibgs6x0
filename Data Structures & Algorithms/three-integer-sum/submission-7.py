class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = 0
        res = []
        while i<len(nums)-2:
            j,k = i+1,len(nums)-1
            while j<k:
                tot = nums[i]+nums[j]+nums[k]
                if tot == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j = j+1
                    k = k-1
                    while j<k and nums[j-1]==nums[j]:
                        j = j+1
                    while j<k and nums[k+1]==nums[k]:
                        k = k-1
                elif tot>0:
                    k = k-1
                else:
                    j = j+1
            i = i+1
            while i<len(nums) and nums[i]==nums[i-1]:
                i = i+1
        return res
                
                


        