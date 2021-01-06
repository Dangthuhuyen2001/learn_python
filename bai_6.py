"Viết một method tính giá trị bình phương của một số."
class Bai5():

    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = int(input("Nhập 1 số bất kỳ: "))

    def printString(self):
        print("Bình phương của số đó là: ",self.s**2)


strObj = Bai5()
strObj.getString()
strObj.printString()
