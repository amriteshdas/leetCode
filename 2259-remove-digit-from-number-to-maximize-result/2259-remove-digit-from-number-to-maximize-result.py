class Solution(object):
    def removeDigit(self, number, digit):
        ans = []
        for i in range(len(number)):
            if number[i] == digit:
                temp = number[:i] + number[i+1:]
                ans.append(int(temp))

        return str(max(ans))
        