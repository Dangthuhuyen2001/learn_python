"""Định nghĩa một hàm có thể tạo và in list chứa các giá trị bình phương của các số từ 1 đến 20 (tính cả 1 và 20)."""
def powList():
    A = [i**2 for i in range(1,21)]
    return A

print(powList())
