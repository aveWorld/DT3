from tabulate import tabulate
from itertools import permutations

def method_Borda(mat, candidate):
    Sum = 0
    for i in range(0, len(mat)):    
        for j in range(1, len(mat[0])):
            if mat[i][j] == candidate:
                if mat[i].index(candidate) == 1:
                    Sum += mat[i][0] * 2
                elif mat[i].index(candidate) == 2:
                    Sum += mat[i][0] * 1
                elif mat[i].index(candidate) == 3:
                    Sum += mat[i][0] * 0
    return Sum

def show(table):
    show = tabulate(table, tablefmt='fancy_grid')
    print(show)

def method_Condorce(mat, candidate_1, candidate_2):
    res1 = 0
    res2 = 0
    for i in range(0, len(mat)):
        if mat[i].index(candidate_1) < mat[i].index(candidate_2):
            res1 += mat[i][0]
        else:
            res2 += mat[i][0]
    res = [res1, res2]
    STR = ""
    if res.index(max(res)) == 0:
        STR = candidate_1 + ' > ' + candidate_2
    else:
        STR = candidate_2 + ' > ' + candidate_1
    return STR, res

def determine_result(str1, str2, str3):
    if str1[len(str1) - 1] == str2[0]:
        str1_str2 = str1 + ' > ' + str2[len(str2) - 1]
        if str1_str2[0] == str3[0] and str1_str2[len(str1_str2) - 1] == str3[len(str3) - 1]:
            print(str1_str2)
            print('Переможцем за методом Кондорсе є кандидат ', str1_str2[0])
        else:
            print('Разом ці твердження суперечливі. Неможливо прийняти якесь узгоджене рішення')    

mat = []
with open ('laboratorna 3.txt', 'r') as file:
    for line in file:
        strip = line.strip()
        split = strip.split(' ')
        for i in range(0, len(split)):
            if split[i].isdigit():
                split[i] = int(split[i])
        mat.append(split)

A = method_Borda(mat, 'A')
B = method_Borda(mat, 'B')
C = method_Borda(mat, 'C')

table_enter = []
for i in range(0, len(mat)):
    table_enter.append(mat[i])
print("Індивідуальне завдання:")
show(table_enter)

table_Borda = [['A', A], ['B', B], ['C', C]]
print("Результати Борда:")
show(table_Borda)

res_Borda = max(A, B, C)
if res_Borda == A:
    print('Переможцем за методом Борда є кандидат А з кількістю голосів:', res_Borda)
elif res_Borda == B:
    print('Переможцем за методом Борда є кандидат B з кількістю голосів:', res_Borda)
elif res_Borda == C:
    print('Переможцем за методом Борда є кандидат C з кількістю голосів:', res_Borda)

str_A_B, A_B = method_Condorce(mat, 'A', 'B')
str_B_C, B_C = method_Condorce(mat, 'B', 'C')
str_A_C, A_C = method_Condorce(mat, 'A', 'C')

table_Condorce = [['A > B\nB > A', str(A_B[0]) + "\n" + str(A_B[1]), str_A_B],
                  ['B > C\nC > B', str(B_C[0]) + "\n" + str(B_C[1]), str_B_C],
                  ['A > C\nC > A', str(A_C[0]) + "\n" + str(A_C[1]), str_A_C]]
print("Результати Кондорсе:")
show(table_Condorce)

all_str = [str_A_B, str_B_C, str_A_C]
all_str = list(permutations(all_str))

for i in range(0, len(all_str)):
    determine_result(all_str[i][0], all_str[i][1], all_str[i][2])


