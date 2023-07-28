

class Person:
    "this is a person class"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        print(self.name)


Person("yassine", 28).print_name()