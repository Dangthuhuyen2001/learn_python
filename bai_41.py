"""Với tuple (1,2,3,4,5,6,7,8,9,10) cho trước, viết một chương trình in một nửa số giá trị đầu tiên trong 1 dòng và 1 nửa số giá trị cuối trong 1 dòng."""

def printTup():
    tp = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    tp1 = tp[:5]
    tp2 = tp[5:]
    print("\n",tp1,"\n",tp2)

printTup()