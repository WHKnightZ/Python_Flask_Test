# def func0():
#     print("None")
#
# def func1(f):
#     return func0
#
# @func1
# def func2():
#     print("Yes")
#
# func2()

# def func1(f):
#     def f2(x, y):
#         if x==True:
#             return f(x, y)
#         else:
#             print("None")
#     return f2
#
# @func1
# def func2(x, y):
#     print("Yes")
#
# func2(False, "Khanh")

# def func0():
#     print("None")
#
# def func1(g):
#     print(g)
#     def dd(f):
#         return func0
#
#     return dd
#
# @func1("asd")
# def func2():
#     print("Yes")
#
# func2()

# a=[]
# b=a
#
# print(id(a))
# print(id(b))
#
# a.append(1)
# print(id(a))
# print(id(b))
#
# a=[]
# print(id(a))
# print(id(b))
#
# a=[1,2,3,4,'44']
#
# print(id(a[0]))
# print(id(a[1]))
# print(id(a[2]))
# print(id(a[3]))
# print(id(a[4]))

class A:
    def __init__(self):
        pass

a=A()
b=A()

a="66"
print(hex(id(a)))
a+="dd"
print(hex(id(a)))