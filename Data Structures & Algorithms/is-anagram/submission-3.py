class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_dict = {}

        # if len(s) != len(t):
        #     return False

        for char in s:
            if char in anagram_dict:
                anagram_dict[char] += 1
            else:
                anagram_dict[char] = 1

        for char in t:
            if char in anagram_dict:
                anagram_dict[char] -= 1
            else:
                return False

        for key, val in anagram_dict.items():
            if val != 0:
                return False

        return True