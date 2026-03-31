class Solution:
    @staticmethod
    def bisect(row, target):
        l, r = 0, len(row) - 1
        while l <= r:
            m = (l + r) // 2
            if target < row[m]:
                r = m - 1
            elif target > row[m]:
                l = m + 1
            else:
                return True
        return False


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[m][-1]:
                l = m + 1
            elif target < matrix[m][0]:
                r = m - 1
            else:
                #  matrix[m][0] <= target <= matrix[m][-1]:
                return self.bisect(matrix[m], target)
        return False


        