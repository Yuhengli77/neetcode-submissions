class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        # first
        index1 = 0
        # second
        index2 = n-1

        while index1 < index2:
            if numbers[index1] + numbers[index2] < target:
                index1 += 1

            elif numbers[index1] + numbers[index2] > target:
                index2 -= 1

            else:
                return [index1 + 1, index2 + 1]