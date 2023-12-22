# Enter your code here. Read input from STDIN. Print output to STDOUT

"""
You are given a string .
Your task is to verify that  is a floating point number.

In this task, a valid float number must satisfy all of the following requirements:

Number can start with +, - or . symbol.
For example:
✔
+4.50
✔
-1.0
✔
.5
✔
-.7
✔
+.4
✖
-+4.5

Number must contain at least  decimal value.
For example:
✖
12.
✔
12.0  

Number must have exactly one . symbol.
Number must not give any exceptions when converted using .
"""
import re

def isValidFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main():
    n = int(input().strip())
    for i in range(n):
        s = input().strip()
        # check if the string starts with +, -, or . and contains exactly one . symbol
        if re.match(r'^[+-]?\d*\.\d+$', s):
            print(isValidFloat(s))
        else:
            print(False)
if __name__ == '__main__':
    main()
