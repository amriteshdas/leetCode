class Solution(object):
    def matrixReshape(self, mat, r, c):
        m=len(mat)
        n= len(mat[0])

        if m*n != r*c:
            return mat
        
        flat = []
        result = []

        for i in range(m):
            for j in range(n):
                flat.append(mat[i][j])
        
        for i in range(r):
            row = []
            for j in range(c):
                row.append(flat[i*c+j])
            result.append(row)

        return result