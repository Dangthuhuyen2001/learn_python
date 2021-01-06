"""Giả sử rằng chúng ta có vài địa chỉ email dạng username@companyname.com,
 hãy viết một chương trình để in username của địa chỉ email cụ thể.
 Cả username và companyname chỉ bao gồm chữ cái."""
import re
def regex(emailAddress):

    pat2 = "(\w+)@((\w+)(.com))" #tao pattern cho input
    re2 = re.match(pat2,emailAddress) #tìm kiếm chuỗi tương úng với pattern
    return re2.group(1)


emailAddress = input()
print(regex(emailAddress))