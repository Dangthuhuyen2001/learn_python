"""Viết một chương trình tính 1/2 + 2/3 + 3/4 + ... + n/(n + 1)
 với một n là số được nhập vào (n> 0)."""

def tinh(n):

    sumNum = 0.0
    for i in range(1, n + 1):
        sumNum += float(float(i)/(i+1))
    return sumNum

print(round(tinh(5),2))

