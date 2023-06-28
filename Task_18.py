#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент 
#к заданному числу X. Пользователь в первой строке вводит натуральное число N 
#– количество элементов в массиве. В последующих  строках записаны N целых 
#чисел Ai. Последняя строка содержит число X

#*Пример:*

#5
#    1 2 3 4 5
#    6
#    -> 5

N = abs(int(input('Enter the amount of elements for list А: ')))
A_entered = input('Enter list elements separated by space:: ').split()
A_num = list(map(int, A_entered))
if len(A_num) != N or N == 0:
    print('The entered elements do not correspond to the declared quantity!')
else:
    X = int(input('Enter the X number to compare the list items with: '))
    min = abs(X - A_num[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A_num[i])
        if count < min:
            min = count
            index = i
    print(f' {A_num[index]} in list A is the closest to {X}, difference equals {abs(X - A_num[index])}')