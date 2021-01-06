"""Viết chương trình Python sử dụng map() để tạo list chứa giá trị bình phương của các số trong đoạn [1,20]."""
def func():
    result = map(lambda i:i**2 , filter(lambda i:i%2==0, range(1,21)))
    print(list(result))

func()