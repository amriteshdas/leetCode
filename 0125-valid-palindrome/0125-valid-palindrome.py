class Solution(object):
    def isPalindrome(self, s):
        ans = []

        for x in s:
            if x.isalnum():
                ans.append(x.lower())

        return ans == ans[::-1]