nums = open('numbers.txt', 'r')
result = open('answer.txt', 'w')
summ = 0
temp = [num.replace('\n', '') for num in nums]

for num in temp:
    if num.isdigit():
        summ += int(num)

result.write(str(summ))

nums.close()
result.close()