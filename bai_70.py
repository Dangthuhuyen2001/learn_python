import math

def binary_search(li, value):
    bottom = 0  #gia tri tư dau
    top = len(li) - 1  #gia tri cao nhat
    index = -1  #vi tri ket qua

    while bottom < top and index == -1:
        mid = int(math.floor((top + bottom) / 2))  #gia tri giua
        if value == li[mid]:
            index = mid
        elif value > li[mid]:  # neu value can tim lon hon gia tri mid
            bottom = mid + 1   #chuyen bottom = mid +1
        else:
            top = mid  #be hon thi top lui lại bằng mid

    return index

if __name__ == '__main__':
    li = [2, 5, 7, 9, 11, 17, 222]

    value = int(input("Nhập giá trị cần tìm: "))

    if binary_search(li, value) == -1:
        print("Không có giá trị nào bằng {0} trong list ".format(value))
    else:
        print("Giá trị {0} nằm ở vị trí li[{1}]".format(value, binary_search(li, value)))
