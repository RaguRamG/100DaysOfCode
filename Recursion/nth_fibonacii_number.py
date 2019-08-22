"""
The Fibonacci sequence is defined as follows: the first number of the sequence is 0,
the second number is 1, and the nth number is the sum of the (n - 1)th and (n - 2)th numbers.
Write a function that takes in an integer n and returns the nth Fibonacci number.
"""


def nth_fibonacii_number(n, fib):
    if n == 1:
        fib[n] = 0
        return 0
    if n == 2:
        fib[n] = 1
        return 1
    if fib[n]:
        return fib[n]
    fib[n] = nth_fibonacii_number(n - 1, fib) + nth_fibonacii_number(n - 2, fib)
    return fib[n]


n = 6
fib = [0] * (n + 1)
print nth_fibonacii_number(n, fib)
