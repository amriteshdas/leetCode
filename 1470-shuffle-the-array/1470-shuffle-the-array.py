class Solution(object):
    def shuffle(self, nums, n):

        ans = []
        l = 0
        r = n
        for i in range(n):
            ans.append(nums[l])
            ans.append(nums[r])
            l +=1
            r +=1
        return ans


        