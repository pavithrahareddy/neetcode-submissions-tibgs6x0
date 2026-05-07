class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        temp = 1
        for i in range(0,len(nums)):
            pre[i] = temp
            temp = temp * nums[i]
        pos = [0] * len(nums)
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            pos[i] = temp
            temp = temp * nums[i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = pre[i]*pos[i]
        return res