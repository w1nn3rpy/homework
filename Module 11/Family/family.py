class Family:
    name = 'Common'
    money = 35000
    have_a_house = False

    def info(self):
        print('Our family\nName: {}\nMoney: {}\nHave a house: {}'.format(
            self.name, self.money, self.have_a_house
        ))

    def earn_money(self, amount):
        self.money += amount
        print('Family earned money! Current balance: {}'.format(self.money))

    def buy_a_house(self, price, discount=0):
        print('Try to buy house')
        if self.money >= price - (price / 100 * discount):
            self.money -= price - (price / 100 * discount)
            self.have_a_house = True
            print('House purchased! Current balance: {}'.format(self.money))
        else:
            print('Not enough money!')


fam = Family()
fam.info()
fam.buy_a_house(35100, 10)
fam.earn_money(50000)