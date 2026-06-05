"""Factorial calculator with recursion."""
import math

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    for i in range(1, 6):
        result = factorial(i)
        print(f"{i}! = {result}")

if __name__ == '__main__':
    main()
