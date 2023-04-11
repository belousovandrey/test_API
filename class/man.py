# from base_person import Person,Warrior
import base_person
man = base_person.Person('Alex', 30, 180)
man.description_person()
warrior = base_person.Warrior('Konan', 32, 200)
print("Нового человека зовут : " + warrior.description_person())