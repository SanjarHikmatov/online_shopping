lst = [3,0, 6, 1, 0, 8, 1, 0]
# for i in range(len(lst)):
#     for j in range(0, len(lst) - i - 1):
#          if lst[j] > lst[j + 1]:
#             lst[j], lst[j + 1] = lst[j + 1], lst[j]
#     if lst[0] == 0:
#         # lst[0] = ''
#         lst[-1] + 0
# print(lst)

#
# lst = lst[-1] + 44
# print(lst)

lst = [3, 0, 6, 1, 0, 8, 1, 0]

for i in range(len(lst)):
    for j in range(0, len(lst) - i - 1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

    if lst[j] == 0:
        lst = [x for x in lst if x != 0] + [c for c in lst if c == 0]

print(lst)

















