"""Viết chương trình tính: f(n)=f(n-1)+100 khi n>0 và f(0)=1,
 với n là số được nhập vào (n>0)."""

def tinhF(n):
    if n == 0:
        return 0
    return tinhF(n - 1) + 100

print(tinhF(5))