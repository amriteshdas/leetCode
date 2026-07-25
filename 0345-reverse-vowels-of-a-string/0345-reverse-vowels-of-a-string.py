class Solution(object):
    def reverseVowels(self, s):
        arr = list(s)

        left = 0
        right = len(arr) - 1

        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        arr = list(s)
        while left < right:
            if arr[left] not in vowels:
                left += 1

            elif arr[right] not in vowels:
                right -=1

            else:
                arr[left], arr[right] = arr[right], arr[left]

                left += 1
                right -= 1
        return "".join(arr)

        