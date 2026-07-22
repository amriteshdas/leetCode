class Solution(object):
    def majorityElement(self, nums):
        count={}
        for x in nums:
            count[x] = count.get(x,0) + 1

        return max(count, key=count.get)
        