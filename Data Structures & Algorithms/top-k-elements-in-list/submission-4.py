class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        d = {}
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        bucket = [[] for _ in range(len(nums)+1)]

        # put number in buket based on their frequency
        for num, freq in d.items():
            bucket[freq].append(num)

        # scan from high freq to low
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result

