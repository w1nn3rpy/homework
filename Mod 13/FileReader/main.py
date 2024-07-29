def file_reader(file):
    for line in file:
        for numbers in line.split():
            yield numbers


with open('numbers.txt', 'r') as text:
    result = 0
    for nums in file_reader(text):
        result += int(nums)
    print(result)

