class Human:
    def __init__(self, age):
        self.age = age

    def say_hello(self):
        print("hello, i am {}".format(self.age))


human = Human(age=35)
human.say_hello()


class HumanExtended(Human):
    def __init__(self, age, name ):
        super().__init__(age)
        self.name = name

human2 = HumanExtended(age=56, name="john")

