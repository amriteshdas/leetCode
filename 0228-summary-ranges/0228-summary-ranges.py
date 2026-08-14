class Solution(object):
    def summaryRanges(self, nums):
        ans = []
        start = 0

        for i in range(1, len(nums) + 1):

            # End of a consecutive range
            if i == len(nums) or nums[i] != nums[i - 1] + 1:

                if start == i - 1:
                    ans.append(str(nums[start]))
                else:
                    ans.append(str(nums[start]) + "->" + str(nums[i - 1]))

                start = i

        return ans