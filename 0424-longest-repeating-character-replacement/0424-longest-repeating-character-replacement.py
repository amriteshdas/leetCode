class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        freq = {}
        ans = 0
        mfreq=0


        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0)+1
            mfreq = max(mfreq,freq[s[right]] )

            while (right-left+1) - mfreq >k:
                freq[s[left]] -=1
                left +=1
            ans = max(ans, right-left+1)

        return ans
        