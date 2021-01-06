"""Viết chương trình sắp xếp tuple (name, age, score) theo thứ tự tăng dần, name là string, age và height là number. Tuple được nhập vào bởi người dùng. Tiêu chí sắp xếp là:
Sắp xếp theo name sau đó sắp xếp theo age, sau đó sắp xếp theo score. Ưu tiên là tên > tuổi > điểm."""

from operator import itemgetter, attrgetter

# Bài tập Python 22 Code by Quantrimang.com
l = []
while True:
    s = input()
    if not s:
        break
    l.append(tuple(s.split(",")))
print(sorted(l, key=itemgetter(0, 1, 2)))
