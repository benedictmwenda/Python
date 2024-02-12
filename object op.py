# Object Oriented Programming.

class People:  #blueprint
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = People("Qaqa", 20)
person2 = People("SpecQ", 19)

# people = People()
# people.name = "SpecQ"
print(f"Hi, my name is {person1.name}, I`m {person1.age} years old.")
