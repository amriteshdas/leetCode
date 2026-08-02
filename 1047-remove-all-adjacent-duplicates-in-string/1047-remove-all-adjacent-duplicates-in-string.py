class Solution(object):
    def removeDuplicates(self, s):
        st = []

        for ch in s:
            if not st or st[-1] != ch:
                st.append(ch)
            else:
                st.pop()

        return "".join(st)