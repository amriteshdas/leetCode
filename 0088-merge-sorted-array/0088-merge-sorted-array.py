class Solution(object):
    def merge(self, nums1, m, nums2, n):
        marge= []
        for i in range(m):
            if m == 0:
                break
            else:
                marge.append(nums1[i])
        
        for j in range(n):
            if n == 0:
                break
            else:
                marge.append(nums2[j])
        marge.sort()
        nums1[:] = marge

        