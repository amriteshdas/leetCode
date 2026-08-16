class Solution(object):
    def reverseOnlyLetters(self, s):
        ans = []
        r = len(s) - 1

        for i in range(len(s)):
            if not s[i].isalpha():
                ans.append(s[i])
            else:
                while not s[r].isalpha():
                    r -= 1

                ans.append(s[r])
                r -= 1

        return "".join(ans)