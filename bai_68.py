"""Sap xep mang bang bubble sort"""

def nhapMang(arr, sophantu):
    for i in range(0, sophantu):
        print("Nhap gia tri cua phan tu a[",i,"] = " ,end = "")
        num = int(input())
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

if __name__ == '__main__':
    arr = []
    sophantu = int(input("Nhap so phan tu: "))

    nhapMang(arr,sophantu)

    print("Mang vua nhap la:")
    xuatMang(arr)

    print("Mang da sap xep tang dan la: ")
    print(bubbleSortIncrease(arr))

    print("Mang da sap xep giam dan la: ")
    print(bubbleSortDecrease(arr))

    print("Gia tri lon nhat trong mang la: ",findMaxValue(arr))

    print("Gia tri lon nhat trong mang la: ", findMinValue(arr))





