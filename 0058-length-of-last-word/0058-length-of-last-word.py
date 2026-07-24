class Solution(object):
    def lengthOfLastWord(self, s):
        text=s.strip().split()[-1]
        return len(text)
        