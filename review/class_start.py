

class Person:
    "this is a person class"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        "print name"
        return self.name

    def description(self):
        "print description"
        return f"{self.name} is {self.age} years old"


person = Person("yassine", 28)
print(person.description())