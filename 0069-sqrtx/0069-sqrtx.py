class Solution(object):
    def mySqrt(self, x):
        left = 1
        right = x
        mid = 0
        if x <2:
            return x

        while left <= right:
            mid = left + (right - left) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return right


        