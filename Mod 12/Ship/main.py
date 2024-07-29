class Ship:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return 'Это корабль {}'.format(self.model)

    def sail(self):
        print('Корабль {} поплыл'.format(self.model))


class WarShip(Ship):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def attack(self):
        print('Корабль {} атакует с помощью оружия "{}"'.format(self.model, self.gun))


class CargoShip(Ship):
    def __init__(self, model):
        super().__init__(model)
        self.tonnage = 0

    def load(self):
        print('Загружаем корабль {}'.format(self.model))
        self.tonnage += 1
        print('Текущая загруженность: {}'.format(self.tonnage))

    def unload(self):
        if self.tonnage > 0:
            print('Разгружаем корабль {}'.format(self.model))
            self.tonnage -= 1
            print('Текущая загруженность: {}'.format(self.tonnage))
        else:
            print('Нечего разгружать.')


warship = WarShip('Аврора', 'Гаубица')
cargoship = CargoShip('Шлюпка')

print(warship)
print(cargoship)

warship.sail()
warship.attack()

cargoship.sail()
cargoship.load()
cargoship.unload()
cargoship.unload()