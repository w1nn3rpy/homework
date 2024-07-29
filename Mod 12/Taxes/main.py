class Property:
    def __init__(self, worth):
        self.worth = worth

    def math_tax(self):
        return 0


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def math_tax(self):
        return self.worth / 1000


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def math_tax(self):
        return self.worth / 2


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def math_tax(self):
        return self.worth / 500


def main():
    money = float(input('Введите количество ваших денег: '))
    apartment_worth = float(input('Введите стоимость квартиры: '))
    car_worth = float(input('Введите стоимость машины: '))
    country_worth = float(input('Введите стоимость дома: '))

    apartment = Apartment(apartment_worth)
    car = Car(car_worth)
    country = CountryHouse(country_worth)

    apartment_tax = apartment.math_tax()
    car_tax = car.math_tax()
    country_tax = country.math_tax()

    print('Налог на квартиру: {}'.format(apartment_tax))
    print('Налог на машину: {}'.format(car_tax))
    print('Налог на дом: {}'.format(country_tax))

    total_tax = apartment_tax + car_tax + country_tax
    print('Общий налог: {}'.format(total_tax))

    balance = money - total_tax
    if balance >= 0:
        print('Вам хватает денег на оплату налогов, ваш остаток: {}'.format(balance))
    else:
        print('Вам не хватает {} для оплаты налогов.'.format(abs(balance)))


main()