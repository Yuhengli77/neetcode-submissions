class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # if matrix[0][0] == target:
        #     return True

        # if matrix[0][0] > target:
        #     return False

        # m = len(matrix)
        # n = len(matrix[0])


        # left = 0
        # right = m

        # while left < right:
        #     mid = (left + right) // 2
        #     if matrix[mid][0] > target:
        #         right = mid

        #     else:
        #         left = mid + 1

        # # now left is the first row > target

        # row = left - 1

        # left = 0
        # right = n - 1

        # while left <= right:
        #     mid = (left + right) // 2
        #     if matrix[row][mid] == target:
        #         return True

        #     elif matrix[row][mid] < target:
        #         left = mid + 1

        #     else:
        #         right = mid -1


        # return False

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2
            if matrix[mid//n][mid%n] == target:
                return True

            elif matrix[mid//n][mid%n] < target:
                left = mid + 1

            else: right = mid - 1


        return False

