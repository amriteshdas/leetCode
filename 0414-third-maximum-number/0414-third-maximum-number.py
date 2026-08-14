class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        ans = sorted(nums)
        if len(ans)<3:
            return ans[-1]
        else:
            return ans[-3]

        