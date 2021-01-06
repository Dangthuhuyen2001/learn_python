"""Viết chương trình và in giá trị theo công thức cho trước: Q = √([(2 * C * D)/H])
(bằng chữ: Q bằng căn bậc hai của [(2 nhân C nhân D) chia H].
Với giá trị cố định của C là 50, H là 30.
D là dãy giá trị tùy biến, được nhập vào từ giao diện người dùng, các giá trị của D được phân cách bằng dấu phẩy."""
import math as m
class Bai9:

    def __init__(self):
        self.c = ""
        self.d = ""
        self.h = ""

    def get(self):
        self.c = int(input("Nhập giá trị của C:  "))
        self.d = int(input("Nhập giá trị của D:  "))
        self.h = int(input("Nhập giá trị của H:  "))

    def print(self):
        print("Số đó là",round(m.sqrt((2 * self.c * self.d) / self.h),2))

bai = Bai9()
bai.get()
bai.print()