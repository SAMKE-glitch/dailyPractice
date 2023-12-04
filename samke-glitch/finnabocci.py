#!/usr/bin/python3
"""
module to print cubesof a finnaboci
"""

cube = lambda x: x ** 3

def fibonacci(n):
    """Method to generate fibonnaci
    return: A fibonacci sequence list
    """
    fibSequence = []
    # iterating through n
    for i in range(n):
        # base case if i is zero
        if i == 0:
            fibSequence.append(0)
        # base case when i = 1
        elif i == 1:
            fibSequence.append(1)
        else:
            # get next number for finabocci
            nextNumber = fibSequence[-1] + fibSequence[-2]
            # appending the next number to fibonacci sequence
            fibSequence.append(nextNumber)
    return fibsequence
