"""Định nghĩa một class có tên là Circle có thể được xây dựng từ bán kính. Circle có một method có thể tính diện tích."""
import math

class Circle():

    def __init__(self,r):
        self.r= r

    def area(self):
        s = (math.pi * self.r**2)
        return print("Dien tich cua duong tron co ban kinh {0} la {1}".format(self.r,round(s,2)))

r = int(input("Nhap ban kinh duong tron: "))
Circle = Circle(r)
print(Circle.area())

