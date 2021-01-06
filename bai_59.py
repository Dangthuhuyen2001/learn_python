"""Tương tự như bài 58, nhưng lần này ta sẽ viết hàm để lấy companyname."""
import re
def regex(emailAddress):

    pat2 = "(\w+)@((\w+)(.com))" #tao pattern cho input
    re2 = re.match(pat2,emailAddress) #tìm kiếm chuỗi tương úng với pattern
    return re2.group(2)

emailAddress = input()
print(regex(emailAddress))