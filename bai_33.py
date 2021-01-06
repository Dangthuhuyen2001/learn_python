"""Định nghĩa một hàm có thể in dictionary chứa các key là số từ 1 đến 20 (bao gồm cả 1 và 20) và các giá trị bình phương của chúng."""

def printDic():
    d = dict()
    for i in range(20):
        d[i] = i**2
    print(d)

printDic()