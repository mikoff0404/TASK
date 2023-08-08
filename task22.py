# Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания в
# се те числа, которые встречаются в обоих наборах.
# Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры

list1 = '2 4 6 8 10 12 10 8 6 4 2'
list2 = '3 6 9 12 15 18'

newlist1 = set(list1.split())
int_newlist1 = list(map(int, newlist1))
newlist2 = set(list2.split())
int_newlist2 = list(map(int, newlist2))

total_list = []

for idx in int_newlist1:
    if idx in int_newlist2:
        total_list.append(idx)

if len(total_list) == 0:
    print('повторяющихся чисел нет')

total_list = sorted(total_list)
for idx in total_list:
    print(idx, end=' ')






