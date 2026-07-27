class Solution(object):
    def maxProduct(self, nums):
        ans=0
        fans=0
        for i in range(len(nums)):
            for j in range(i+1,(len(nums))):
                p=nums[i]*nums[j]
                if p>ans:
                    ans = p
                    fans=(nums[i]-1)*(nums[j]-1)

        return fans
                    

        