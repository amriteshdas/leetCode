class Solution(object):
    def transpose(self, matrix):
        r= len(matrix)
        c=len(matrix[0])
        ans= []

        ans = [[0 for _ in range(r)] for _ in range(c)]

        for i in range(r):
            for j in range(c):
                ans[j][i]=matrix[i][j]

        return ans
        