# Write a Python program that finds the factorial of a number using recursion and returns the result. 
# (Example - If number = 5, factorial = 5*4*3*2*1 = 120)

num = int(input("Enter a random number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(num)

print(f"The factorial of {num} is {result}")