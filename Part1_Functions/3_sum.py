# https://www.w3schools.com/python/python_casting.asp / https://www.w3schools.com/python/python_scope.asp
# Write a function add(a, b) that returns the sum of the two numbers.
# Ask the user for two numbers (as input), convert them to integers, call the function, and print the result.
    
# Write your code here:
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2)
print(f"Sum: {result}")
