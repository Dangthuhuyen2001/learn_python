"""Viết một chương trình chấp nhận đầu vào là chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy, kiểm tra xem chúng có chia hết cho 5 không.
Sau đó in các số chia hết cho 5 thành dãy phân tách bởi dấu phẩy.
0100,0011,1010,1001"""
value = []
items = [x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if intp % 5 ==0:
        value.append(p)
print(','.join(value))