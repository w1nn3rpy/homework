def fact(num):
    if num == 1:
        return 1
    num = num * fact(num - 1)
    return num


print(fact(996))
