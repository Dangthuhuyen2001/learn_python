"""Viết một chương trình chấp nhận đầu vào là một câu, đếm chữ hoa, chữ thường."""
string = input("Nhập chuỗi của bạn: ")

result = {'Uppercase':0, 'Lowercase':0, 'UNDEFINDE':0}

for leter in string:
    if leter.isupper():
        result['Uppercase'] +=1
    elif leter.islower():
        result['Lowercase'] += 1
    else:
        result['UNDEFINDE'] += 1

print(result)