class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #2^n
        res = []
        edge = 1
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                if (i < 2 or j == 0 or j == i):
                    temp.append(edge)
                else:
                    temp.append(res[i-1][j] + res[i-1][j-1])
            res.append(temp)

        #n = 5
        # 1 n-1

        return res
        