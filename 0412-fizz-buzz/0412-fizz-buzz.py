class Solution(object):
    def fizzBuzz(self, n):
        num = 1
        ans = []
        for i in range(n):
            if num%3 == 0 and num%5 == 0:
                ans.append("FizzBuzz")
            elif num%3 == 0:
                ans.append("Fizz")
            elif num%5 == 0:
                ans.append("Buzz")
            else:
                ans.append(str(num))
            num +=1
        return ans

        