"""Viết chương trình sử dụng generator để
in số chẵn trong khoảng từ 0 đến n,
cách nhau bởi dấu phẩy, n là số được nhập vào."""

#dùng yield

def generatorChan(nums):
    i = 0
    while i <= nums:
        if i % 2 == 0:
            yield i #dung generator
        i += 1

nums = int(input(""))
result = [str(i) for i in generatorChan(nums)]
print("Nhung so chan trong list la: ",",".join(result))
