#
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner
#
# @smart_div
# def div(a,b):
#     print(a/b)
#
# div(6,4)
#
#
#
# def update(n):
#     return n*2
#
#
# nums = [3,2,6,8,4,6,2,9]
# dub =list(map(update, nums))
# print(dub)\


class Category:
    def __init__(self, name):
        self.name = name
