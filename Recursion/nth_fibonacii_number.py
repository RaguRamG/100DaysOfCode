"""
The Fibonacci sequence is defined as follows: the first number of the sequence is 0,
the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
Write a function that takes in an integer n and returns the nth Fibonacci number.
"""


def nth_fibonacii_number(n):
    if n == 1:
        return 0
    if n == 2:
        return 1

    return nth_fibonacii_number(n - 1) + nth_fibonacii_number(n - 2)


n = 19
print nth_fibonacii_number(n)
