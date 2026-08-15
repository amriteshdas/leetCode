class Solution(object):
    def sortArrayByParity(self, nums):
        el=[]
        ol=[]
        for i in range(len(nums)):
            if nums[i]&1==0:
                el.append(nums[i])
            else:
                ol.append(nums[i])
        ans= el+ol
        return ans
        