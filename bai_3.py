"""Viết một chương trình có thể tính giai thừa của một số cho trước. Kết quả được in thành chuỗi trên một dòng, phân tách bởi dấu phẩy.
Ví dụ, số cho trước là 8 thì kết quả đầu ra phải là 40320."""
"""Đệ quy tuyến tính"""

def giai_thua(n):
    if n == 0:
        return 1
    return n* giai_thua(n-1)

n = int(input("Nhap 1 so vao: "))
print(giai_thua(n))