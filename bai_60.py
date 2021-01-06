"""Viết một chương trình chấp nhận chuỗi từ được phân tách bằng khoảng trống và in các từ chỉ gồm chữ số."""
import re

def findNumInStr(str):
    return re.findall("\d+",str)

str = input("Nhap chuoi: ")
print(findNumInStr(str))
