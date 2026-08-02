class Solution(object):
    def backspaceCompare(self, s, t):
        st = []
        ss=[]
        for ch in s:
            if ch != "#":
                st.append(ch)
            elif st:
                st.pop()

        for ch in t:
            if ch != "#":
                ss.append(ch)
            elif ss:
                ss.pop()

        return ss == st


        