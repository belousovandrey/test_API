class Person():
    """Создаем человека"""

    def __init__(self, name, age, height):
        """Инициализируем человека"""
        self.name = name
        self.age = age
        self.height = height
        self.weight = 100

    def description_person(self):
        """Получение описания человека"""
        description = self.name + ', ему ' + str(self.age) + ', его рост  ' + str(self.height) + ', его вес  ' + str(
            self.weight)
        print("Нового человека зовут : " + description)

    def get_weight(self):
        """Получение веса человека"""
        print("Вес нашего человека : " + str(self.weight))

    def update_weight(self, kg):
        """Изменение веса человека"""
        self.weight = kg


class Warrior(Person):
    """Создаем класс воин"""

    def __init__(self, name, age, height):
        """Инициализируем атрибуты класса родителя"""
        super().__init__(name, age, height)
        self.rage = 100

    def get_rage(self):
        """Получение заряд ярости"""
        print("заряд ярости равен : " + str(self.weight))

    def description_person(self):
        """Переопределение метода родителя"""
        description = self.name + ', ему ' + str(self.age) + ', его заряд ярости  ' + str(self.rage)
        # print("Нового человека зовут : " + description)
        return description


warrior = Warrior('Konan', 32, 200)
# warrior.get_rage()
# warrior.description_person()
print("Нового человека зовут : " + warrior.description_person())

# warrior.update_weight(150)
# print(warrior.rage)

# man = Person('Alex', 30, 180)
# man.description_person()
# man.weight = 110
# man.update_weight(110)
# man.get_weight()
