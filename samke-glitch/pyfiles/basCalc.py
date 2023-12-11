#!/usr/bin/python3
"""
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operand = 0
        # for the final result
        result = 0
        sign = 1 # 1 for positive, -1 for negative

        for char in s:
            if char.isdigit():
                operand = operand * 10 + int(char)
            elif char == '+':
                result += sign * operand
                operand = 0
                sign = 1
            elif char == '-':
                result += sign * operand
                operand = 0
                sign = -1
            elif char == '(':
                # save the current result and sign on the stack
                stack.append((result, sign))
                result = 0
                sign = 1
            elif char == ')':
                prevResult, prevSign = stack.pop()
                result += sign * operand
                result = prevResult + prevSign * result
                operand = 0
        result += sign * operand
        return result
