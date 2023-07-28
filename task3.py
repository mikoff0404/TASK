sum = int(input('введите сумму двух натуральных чисел '))
mult = int(input('введите произведение двух натуральных чисел '))

diskr = (sum * sum - 4 * mult)
if diskr >= 0:
    x1 = int((sum + diskr ** 0.5) / 2)
    x2 = sum - x1
    print(f'исходные числа {x1} и {x2}')
else: print('дискриминант отрицателен')

