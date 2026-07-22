class Solution(object):
    def containsDuplicate(self, nums):
        count = {}
        for x in nums:
            count[x] = count.get(x,0)+1
        if max(count.values())==1:
            return False
        else:
            return True
        