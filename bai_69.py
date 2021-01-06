"""Sap xep mang bang bubble sort"""
import random
import math

def nhapMang(arr, sophantu):
    for i in range(0, sophantu):
        num = random.randrange(1, 100)
        arr.append(num)

def xuatMang(arr):
    result = [i for i in arr]
    print(result)


def bubbleSortIncrease(arr):
    for passnum in range(len(arr)-1, 0, -1):
        for i in range(passnum):
            if arr[i] > arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr

def bubbleSortDecrease(arr):
    for passnum in range(len(arr)-1, 0, -1):
        for i in range(passnum):
            if arr[i] < arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
    return arr


def findMaxValue(arr):
    max = 0
    for i in range(len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max

def findMinValue(arr):
    min = arr[0]
    for i in range(len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min

def checkNT(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))):
       if num % i == 0:
         return False
    return True


def SNT(arr):
    nt = []
    for i in range(len(arr)):
        if checkNT(arr[i]):
            nt.append(arr[i])
    return nt

def xoaLap(arr):
    last = []
    dup = []
    for x in arr:
        if x not in dup:
            if x not  in last:
                last.append(x)
            else:
                last.remove(x)
                dup.append(x)
    return last


if __name__ == '__main__':
    arr = []
    sophantu = int(input("Nhap so phan tu: "))

    nhapMang(arr, sophantu)

    print("\n\nMang vua nhap la:")
    xuatMang(arr)

    print("\nMang da sap xep tang dan la: ")
    print(bubbleSortIncrease(arr))

    print("Mang da sap xep giam dan la: ")
    print(bubbleSortDecrease(arr))

    print("Mang da xoa lap: ")
    print(xoaLap(arr))

    print("\nGia tri lon nhat trong mang la: ", findMaxValue(arr))

    print("Gia tri lon nhat trong mang la: ", findMinValue(arr))

    print("\nNhung so nguyen to trong mang: " , ",".join(map(str, SNT(arr))))
