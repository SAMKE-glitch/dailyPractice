from itertools import groupby

def compressString(s):
    compressedString = ""
    
    for key, group in groupby(s):
        count = len(list(group))
        compressedString += f"({count}, {key}) "
    return compressedString
    
inputString = input().strip()
outputString = compressString(inputString)
print(outputString)
