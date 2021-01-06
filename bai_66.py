"""Hãy viết chương trình sử dụng list comprehension để in dãy Fibonacci dưới dạng tách biệt bằng dấu ",",
 n được người dùng nhập vào."""


def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nhap n: "))
values = [str(fibonacci(x)) for x in range(0, n + 1)]
print (",".join(values))
