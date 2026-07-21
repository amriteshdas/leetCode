class Solution(object):
    def moveZeroes(self, nums):
        new_ans = []
        count = 0
        for x in nums:
            if x !=0:
                new_ans.append(x)
        
        count = len(nums) - len(new_ans)

            
        for _ in range(count):
            new_ans.append(0)
        nums[:] = new_ans
        