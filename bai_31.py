"""Định nghĩa hàm có thể chấp nhận input là số nguyên và in "Đây là một số chẵn" nếu nó chẵn và in "Đây là một số lẻ" nếu là số lẻ."""

def printTypeofNum(num):
    if num % 2 == 0:
        print("đây là số chẵn")
    else:
        print("đây là số lẻ")

printTypeofNum(3)