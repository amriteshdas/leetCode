class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        ans = []
        mnum = max(candies)
        for i in range(len(candies)):
            if candies[i]+ extraCandies < mnum:
                ans.append(False)
            else:
                ans.append(True)
        return ans

        