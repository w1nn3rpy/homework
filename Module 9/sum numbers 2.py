def iter_num(nums):
    summ = 0
    for line in nums:
        for char in line:
            if char.isdigit():
                summ += int(char)
    return summ


nums = open('numbers1.txt', 'r')
answer = open('answer1.txt', 'w')

answer.write(str(iter_num(nums)))

nums.close()
answer.close()