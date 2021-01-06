"""Định nghĩa một hàm có thể tạo list chứa các giá trị bình phương của các số từ 1 đến 20 (bao gồm cả 1 và 20) và in 5 mục đầu tiên trong list."""

def subPow():
    powSub = []
    for i in range(1,21):
        powSub.append(i**2)
    print(powSub[:5])

subPow()
