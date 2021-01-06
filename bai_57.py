"""Định nghĩa một class exception tùy chỉnh, nhận một thông báo là thuộc tính."""


class MyError(Exception):

    def __init__(self, msg):
        self.msg = msg


error = MyError("Có gì đó sai sai!")
print(error)