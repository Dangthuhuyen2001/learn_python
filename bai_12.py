"""Viết một chương trình chấp nhận chuỗi là các dòng được nhập vào, chuyển các dòng này thành chữ in hoa và in ra màn hình"""
lines = []
while True:
    s = input("Nhập 1 chuỗi coi: ")
    if s:
       lines.append(s.upper())
    else:
       break
for sentence in lines:
     print (sentence)