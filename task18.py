# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

#     5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input('Введите количество элементов массива: '))
list_1 = []

for i in range(n):
    list_1.append(i + 1)
print(list_1)

x = int(input('Введите число X: '))
list_2 = []
for i in range(n):
    if abs(list_1[i] - x) <= 1:
        list_2.append(list_1[i])
#print(f"Число чуть меньшее чем Х: {list_2[0]}")
print(f"Число равное (максимально близкое) Х: {list_2[1]}")
#print(f"Число чуть большее чем Х: {list_2[3]}")