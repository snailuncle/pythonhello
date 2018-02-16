('the answer', 42), b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
('the answer', 42)('the answer', 42)('the answer', 42)('the answer', 42)('the answer', 42)('the answer', 42)