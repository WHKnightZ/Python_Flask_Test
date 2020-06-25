arr = [0] * 1000000


def func1(arr):
    for i in range(1000000):
        arr[i] = 1


def func2(arr):
    for i in range(len(arr)):
        arr[i] = 1


def func3(arr):
    l = len(arr)
    for i in range(l):
        arr[i] = 1


def func4(arr):
    for i in arr:
        i = 1
