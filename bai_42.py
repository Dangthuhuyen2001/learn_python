"""Viết một chương trình để tạo tuple khác, chứa các giá trị là số chẵn trong tuple (1,2,3,4,5,6,7,8,9,10) cho trước."""

def tup():
    tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    suptp =[i for i in tp if i%2 == 0]
    print(tuple(suptp))
tup()