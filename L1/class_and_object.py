class Human:
    def __init__(self, age, name, gender):
        self.age = age
        self.name = name
        self.gender = gender

    def get_name(self):
        return self.name


human_1 = Human(age=25, name = 'John', gender='male')
print(human_1.get_name())



