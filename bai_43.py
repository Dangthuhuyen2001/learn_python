"""Viết một chương trình để tạo ra và in tuple chứa các số chẵn được lấy từ tuple (1,2,3,4,5,6,7,8,9,10)."""

def tup():
    tupl = (1,2,3,4,5,6,7,8,9,10)
    result = [i for i in tupl if i%2==0]
    print("tuple chứa các số chẵn :",tuple(result))

tup()