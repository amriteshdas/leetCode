class Solution(object):
    def nextGreatestLetter(self, letters, target):

        for i in range(len(letters)):
            if target<letters[i]:
                return letters[i]
        else:
            return letters[0]


        