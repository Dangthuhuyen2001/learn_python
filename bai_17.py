"""Viết một chương trình chấp nhận đầu vào là một câu, đếm số chữ cái và chữ số trong câu """
string = input("Nhập chuỗi của bạn: ")

result = {'DIGIST':0, 'ALPHA':0, 'UNDEFINDE':0}

for leter in string:
    if leter.isdigit():
        result['DIGIST'] +=1
    elif leter.isalpha():
        result['ALPHA'] += 1
    else:
        result['UNDEFINDE'] += 1

print(result)