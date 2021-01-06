"""Sử dụng một danh sách để lọc các số lẻ từ danh sách được người dùng nhập vào."""


values = input("Nhập dãy số của bạn, cách nhau bởi dấu phẩy: ")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))
