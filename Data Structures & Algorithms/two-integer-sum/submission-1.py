class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0,len(nums)):
            if target-nums[i] in seen:
                return list([seen[target-nums[i]],i])
            seen[nums[i]] = i
        