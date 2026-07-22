class Solution(object):
    def removeElement(self, nums, val):
        ans = []
        for x in nums:
            if x != val:
                ans.append(x)
        
        
        nums[:] = ans

        