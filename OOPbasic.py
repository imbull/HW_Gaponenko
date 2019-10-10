class Animal(object):

    def __init__(self):
        self.name = 'Undefined'

    def display(self) -> str:
        return self.name

    def sound(self) -> str:
        pass


class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'Dog'

    def sound(self) -> str:
        return 'Gav'

    def display(self) -> str:
        return super().display() + ': Animal - ' \
               + str(self.name) + '; sound - ' + str(self.sound())


class Cat(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'Cat'

    def sound(self) -> str:
        return 'Meow'

    def display(self) -> str:
        return super().display() + ': Animal - ' \
               + str(self.name) + '; sound - ' + str(self.sound())


class Ant(Animal):

    def __init__(self):
        super().__init__()
        self.name = 'Atn'

    def sound(self) -> str:
        return 'not sound'

    def display(self) -> str:
        return super().display() + ': Animal - ' \
               + str(self.name) + '; sound - ' + str(self.sound())


if __name__ == "__main__":

    dog = Dog()
    print(dog.display())

    cat = Cat()
    print(cat.display())

    ant = Ant()
    print(ant.display())
