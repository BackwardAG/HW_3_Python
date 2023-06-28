#Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
#в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N 
#– количество элементов в массиве. В последующих  строках записаны 
#N целых чисел Ai. Последняя строка содержит число X

#*Пример:*
# 5
#   1 2 3 4 5
#   3
#   -> 1


N = abs(int(input('Enter an amount of elements in a list: ')))
A_entered = input('Enter list elements by space: ').split()
A_num = list(map(int, A_entered))
if len(A_num) != N:
    print('The entered elements do not correspond to the declared quantity!')
else:
    X = int(input('Enter the number X to be found in the list:: '))
    count = 0
    for i in range(N):
        if A_num[i] == X:
            count += 1
    print(f' {X} occurs in the list {count} time') 