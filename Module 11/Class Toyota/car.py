from random import randint


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0


toyota_1 = Toyota()
toyota_1.current_speed = randint(0, 200)

toyota_2 = Toyota()
toyota_2.current_speed = randint(0, 200)

toyota_3 = Toyota()
toyota_3.current_speed = randint(0, 200)

print(toyota_1.current_speed, toyota_2.current_speed, toyota_3.current_speed)