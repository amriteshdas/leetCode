class Solution(object):
    def strStr(self, haystack, needle):
        for i in range(len(haystack)):
            p = 0

            if haystack[i] == needle[0]:
                while p < len(needle) and i + p < len(haystack):
                    if haystack[i + p] == needle[p]:
                        p += 1
                    else:
                        p = 0
                        break

                if p == len(needle):
                    return i

        return -1