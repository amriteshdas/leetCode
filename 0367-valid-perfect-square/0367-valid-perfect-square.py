class Solution(object):
    def isPerfectSquare(self, num):
        left = 1
        right = num
        if num<2:
            return True
        ans = 0.0
        while left<= right:
            mid = left+(right - left)/2
            if mid*mid == num:
                ans = mid
                break
            elif mid*mid <num:
                left = mid +1
            else:
                right = mid -1
        # else:
        #     ans = right
        return isinstance(ans, int)
        