class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()

        for num in nums:
            s.add(num)

        # s is a set with our numbers
        longest = 0
        count = 1
        for num in nums:
            # starting of a sequence
            if (num - 1) not in s:
                while (num + 1) in s:
                    count += 1
                    num += 1

            # end of counting that sequence
            # store longest seq's count
            if count > longest:
                longest  = count
            # reset our counting
            count = 1

    
        return longest
