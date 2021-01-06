"""Viết chương trình để đọc chuỗi ASCII và chuyển đổi
nó sang một chuỗi Unicode được mã hóa bằng UTF-8."""
# -*- coding: utf-8 -*-

str = input()
str2 = str.encode("utf-8")
print(type(str2))
