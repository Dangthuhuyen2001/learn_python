"""Định nghĩa class có tên là Hinhchunhat được xây dựng bằng chiều dài và chiều rộng.
Class Hinhchunhat có method để tính diện tích."""

class Rectangle():

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        s = self.length * self.width
        return print("Dien tich cua duong tron co chieu dai {0}, chieu rong {1} la {2}".format(self.length,self.width,s))


leng = int(input("Nhap chieu dai cua hinh chu nhat: "))
width = int(input("Nhap chieu rong cua hinh chu nhat: "))
rec = Rectangle(leng,width)
rec.area()
