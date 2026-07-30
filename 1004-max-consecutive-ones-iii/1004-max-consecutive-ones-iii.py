class Solution(object):
    def longestOnes(self, nums, k):
        n=len(nums)
        maximum = 0
        left= 0
        right = 0
        zero = 0
        while right<n:
            if nums[right]==0:
                zero+=1
            while zero >k:
                if nums[left]==0:
                    zero -=1
                left +=1
            maximum = max(maximum,right-left+1)
            right +=1



        return maximum
        