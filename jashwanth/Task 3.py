def fibonacci(n):
    if n <= 0:
        return "Input must be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    num = int(input("Enter the position (n) to find the nth Fibonacci number: "))
    result = fibonacci(num)
    print(f"The {num}th Fibonacci number is: {result}")
except ValueError:
    print("Please enter a valid integer.")