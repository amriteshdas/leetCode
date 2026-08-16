class Solution(object):
    def isPalindrome(self, x):
        nums = str(x)
        l = 0
        r = len(nums) - 1
        while l<=r:
            if nums[l] != nums[r]:
                return False
            l +=1
            r -=1
        else:
            return True 
        