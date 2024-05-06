# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`. Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

# Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.
# В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        pass


class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Чирик-чирик")

    def eat(self):
        print("Птичка ест семечки")


class Mammal(Animal):
    def __init__(self, name, age, fur):
        super().__init__(name, age)
        self.fur = fur

    def make_sound(self):
        print("Опять понедельник")

    def eat(self):
        print("Млекопитающие едят еду")


class Reptile(Animal):
    def __init__(self, name, age, skin):
        super().__init__(name, age)
        self.skin = skin

    def make_sound(self):
        print("Шшшшшш....")

    def eat(self):
        print("Рептилии едят яйца")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = {}

    def add_animal(self, animal, name, age, parameter):
        if animal == "bird":
            animal = Bird(name, age, parameter)
        elif animal == "mammal":
            animal = Mammal(name, age, parameter)
        elif animal == "reptile":
            animal = Reptile(name, age, parameter)
        else:
            print("Такого животного нет")
            return
        self.animals.append(animal)


    def add_employee(self, name, age, parameter, profession):
        mammal = Mammal(name, age, parameter)
        self.employees.update({mammal: profession})


class ZooKeeper(Zoo):
    def feed_animal(self):
        print("Животное накормлено")
class Veterinarian(Zoo):
    def heal_animal(self):
        print("Животное вылечено")
def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
def zoo_info(zoo):
    print(f'В зоопарке {len(zoo.animals)} животных и {len(zoo.employees)} сотрудников.')




animals = [Bird("Синичка", 2, "Синяя"), Mammal("Иван", 35, "Залысина"), Reptile("Ящерица", 3, "Красная")]
animal_sound(animals)

zoo = Zoo()
zoo.add_animal("bird", "Синичка", 2, "Синяя")
zoo.add_animal("reptile", "Ящерица", 3, "Красная")
zoo.add_employee("Иван", 35, "Залысина", ZooKeeper())

zoo_info(zoo)

for employee, profession in zoo.employees.items():
    print(f"{employee.name}, возраст {employee.age}, профессия: {profession.__class__.__name__}")
