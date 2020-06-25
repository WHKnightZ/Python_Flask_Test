import timeit

lst = ["func1", "func2", "func3", "func4"]

for item in lst:
    t = timeit.timeit(item + "(arr)", setup="from ex.ex1 import arr, " + item, number=100)
    print(item, ":", t)
