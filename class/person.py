class Person():
    """Модель человека"""

    def __init__(self, name, age):
        """Инициализация атрибутов человека(параметров)"""
        self.name = name
        self.age = age
        print("Человек создан")

    def sing(self):
        """Просим человека спеть"""
        print(self.name + " поет")

    def dance(self):
        """Просим человека танцевать"""
        print(self.name + " танцует")

man = Person('Andrey', 30)
woman = Person('Nasty',25)

man.dance()
woman.sing()