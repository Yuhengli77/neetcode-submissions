class Solution:
    def isValid(self, s: str) -> bool:
        # if not even
        n = len(s)
        if n % 2 != 0:
            return False

        open_parentheses = {
            ')' : '(',
            '}': '{',
            ']': '['
        }
        

        stack = []

        for char in s:
            # if not empty and stack.top() == curr, pop
            if stack and char in open_parentheses and stack[-1] == open_parentheses[char]:
                stack.pop()
            else:
                stack.append(char)

        if not stack:
            return True

        else:
            return False

        