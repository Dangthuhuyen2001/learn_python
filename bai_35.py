"""Định nghĩa một hàm có thể tạo ra một dictionary chứa key là những số từ 1 đến 20 (bao gồm cả 1 và 20)
và các giá trị bình phương của key. Hàm chỉ cần in các key."""
def printValueofDic():
    d = dict()
    for i in range(20):
        d[i] = i**2

    print([key for key in d])

printValueofDic()