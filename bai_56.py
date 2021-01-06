def throw():
    return 5/0

try:
    throw()
except ZeroDivisionError:
     print ("Chia một số cho 0!")
except Exception as problem:
     print ('Bắt được một exception')
finally:
     print ('Phép tính bị hủy')