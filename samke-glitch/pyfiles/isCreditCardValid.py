# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def isValidCreditCard(cardNumber):
    pattern = re.compile(r'^(?!.*(\d)(?:-?\1){3,})[4-6]\d{3}(?:-?\d{4}){3}$')
    return bool(pattern.match(cardNumber))


# Read the number of test cases from STDIN
num_test_cases = int(input())
# Process each test case
for _ in range(num_test_cases):
    # Read the credit card number from STDIN
    credit_card_number = input().strip()

    # Check if the credit card number is valid and print the result
    if isValidCreditCard(credit_card_number):
        print("Valid")
    else:
        print("Invalid") 

