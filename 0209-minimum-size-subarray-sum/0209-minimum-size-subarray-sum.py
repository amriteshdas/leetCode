class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        right = 0
        sumt=0
        mlen = 9999999999999
        while right<len(nums):
            sumt = sumt + nums[right]
            while sumt>=target:
                mlen=min(mlen,right-left+1)
                sumt -= nums[left]
                left+=1
               
            right +=1
        if mlen==9999999999999:
            return 0
        else:
            return mlen

        