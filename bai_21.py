"""Viết chương trình tính số tiền thực của một tài khoản ngân hàng dựa trên
 nhật ký giao dịch được nhập vào từ giao diện điều khiển."""
import sys
netAmout = 0
while True:
    s = input("Nhập nhật ký giao dịch: ")
    if not s:
        break
    value = s.split(" ")
    operation = value[0]
    amount = int(value[1])
    if operation == 'D':
        netAmout += amount
    if operation == 'W':
        netAmout -= amount
    else:
        pass
print('Số tiền hiện có: {0}'.format(netAmout))