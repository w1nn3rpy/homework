
file_1 = open('task/group_1.txt', 'r', encoding='utf-8')
file_2 = open('task/Additional_info/group_2.txt', 'r', encoding='utf-8')

summa = 0
diff = 0
compose = 1

for i_line in file_1:
    info = i_line.split()
    if info:
        summa += int(info[2])
        diff -= int(info[2])

for i_line in file_2:
    info = i_line.split()
    if info:
        compose *= int(info[2])

file_1.close()
file_2.close()

print(summa)
print(diff)
print(compose)
