"""Định nghĩa một class có ít nhất 2 method:
getString: để nhận một chuỗi do người dùng nhập vào từ giao diện điều khiển.
printString: in chuỗi vừa nhập sang chữ hoa.
Thêm vào các hàm hiểm tra đơn giản để kiểm tra method của class."""

class Bai5():

    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = str(input("Nhập chuỗi bất kỳ: "))

    def printString(self):
        print(self.s.upper())


strObj = Bai5()
strObj.getString()
strObj.printString()
