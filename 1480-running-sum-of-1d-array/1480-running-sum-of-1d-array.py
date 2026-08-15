class Solution(object):
    def runningSum(self, nums):
        ans  = []
        s = 0
        for i in range(len(nums)):
            s = s + nums[i]
            ans.append(s)
        return ans

        