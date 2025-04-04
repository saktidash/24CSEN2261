def factorial(n):
    # If the number is negative, factorial doesn't exist
    if n < 0:
        return "Factorial does not exist for negative numbers"
    # If the number is 0 or 1, factorial is 1
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

# Example usage:
num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")
