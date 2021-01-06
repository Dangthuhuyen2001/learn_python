"""Định nghĩa một hàm có input là 2 chuỗi và in chuỗi có độ dài lớn hơn trong giao diện điều khiển.
 Nếu 2 chuỗi có chiều dài như nhau thì in tất cả các chuỗi theo dòng."""

def printLengStr(str1, str2):
    if len(str1) > len(str2):
        print(str1)
    else:
        print(str2)

str1 = input()
str2 = input()

printLengStr(str1,str2)