

class Prime:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 1

    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        self.current += 1
        while self.current <= self.max_num:
            is_prime = True

            for i in range(2, int(self.current ** 0.5) + 1):
                if self.current % i == 0:
                    is_prime = False
                    break

            if is_prime:
                return self.current
            self.current += 1
        raise StopIteration


test = Prime(50)
for i_num in test:
    print(i_num, end=' ')
