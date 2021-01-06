"""Viết một chương trình tính giá trị của a+aa+aaa+aaaa với a là số được nhập vào bởi người dùng."""
num = int(input("Nhập Số a:"))
n1 = int( "%s" % num )
n2 = int( "%s%s" % (num,num) )
n3 = int( "%s%s%s" % (num,num,num) )
n4 = int( "%s%s%s%s" % (num,num,num,num) )
# Bài tập Python 18, Code by Quantrimang.com
print ("Tổng cần tính là: ",n1+n2+n3+n4)