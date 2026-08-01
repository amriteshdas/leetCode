class Solution(object):
    def isValid(self, s):
        st = []
        for b in s:
            if b=="(" or b=="[" or b=="{" :
                st.append(b)
            else:
                if len(st) == 0:
                    return False
                ch = st.pop()
                if (ch =="(" and b ==")") or (ch =="{" and b =="}") or (ch =="[" and b =="]"):
                    continue
                else:
                    return False

        return len(st)==0
        