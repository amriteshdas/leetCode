class Solution(object):
    def largestAltitude(self, gain):
        s= 0
        ans = []
        ans.append(0)
        for i in range(len(gain)):
            s = s+gain[i]
            ans.append(s)
        return max(ans)
        