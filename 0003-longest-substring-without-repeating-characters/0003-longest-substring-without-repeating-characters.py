class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left= 0
        right=0
        ans = set()
        mlen=0
        for right in range (len(s)):


            while s[right] in ans:
                ans.remove(s[left])
                left = left+1 
            ans.add(s[right])
            mlen = max(mlen, len(ans))
        return mlen
        