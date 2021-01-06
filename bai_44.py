"""Viết một chương trình Python nhận chuỗi nhập vào bởi người dùng,
in "Yes" nếu chuỗi là "yes" hoặc "YES" hoặc "Yes", nếu không in "No"."""
s = input ("Nhập chuỗi: ")
if s == "yes" or s == "YES" or s == "Yes":
    print ("Yes")
else:
     print ("No")