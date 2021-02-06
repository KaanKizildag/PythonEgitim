class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year


p1 = Person(name = 'Melike',year = 2000)
p2 = Person(year = 2000 ,name = "Berkay")

print(p1.name)
print(p2.year)

print(p1.__sizeof__())