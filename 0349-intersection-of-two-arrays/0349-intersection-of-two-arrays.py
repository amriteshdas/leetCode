class Solution(object):
    def intersection(self, nums1, nums2):
        ans = []
        for x in nums1:
            for y in nums2:
                if x == y:
                    if x not in ans:
                        ans.append(x)
        return ans
        