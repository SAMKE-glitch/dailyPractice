class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                topElement = stack.pop() if stack else '#'
                if mapping[char] != topElement:
                    return False
            else:
                stack.append(char)
        return not stack
