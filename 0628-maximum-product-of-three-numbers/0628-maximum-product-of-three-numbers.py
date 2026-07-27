class Solution(object):
    def maximumProduct(self, nums):
        fans = 0
        lans = 0
        nums=sorted(list(nums))
        lans = nums[-1]*nums[-2]*nums[-3]
        fans = nums[0]*nums[1]*nums[-1]
        if lans>fans:
            return lans
        else:
            return fans
        