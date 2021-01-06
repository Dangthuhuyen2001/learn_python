"""Viết chương trình Python dùng filter() để tạo danh sách chứa các số chẵn trong đoạn [1,20]."""

def func():

    result = filter(lambda i:i%2==0,range(1,21))
    print(list(result))

func()