# num = int(input('введите число '))
#
# for i in range(num):
#     count = 2 ** i
#     if  count < num:
#         print(count)

num = int(input('введите число '))

for i in range(num):
    count = 2 ** i
    if  count < num:
        print(count, end=', ')