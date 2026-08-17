class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine = list(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] not in magazine:
                return False

            magazine.remove(ransomNote[i])

        return True