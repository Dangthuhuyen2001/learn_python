"""Viết chương trình để giải 1 câu đố cổ của Trung Quốc:
 Một trang trại thỏ và gà có 35 đầu, 94 chân,
 hỏi số thỏ và gà là bao nhiêu?"""

def giaido(dau, chan):
    kl = "Khong co ket qua phu hop !!"
    for dauTho in range(dau + 1):
        dauGa = dau - dauTho
        if 2*dauGa + 4*dauTho == chan:
            print("So tho la", dauTho,"\n so ga la",dauGa)
    return kl


dau = 35
chan = 94
r = giaido(dau, chan)
print(r)