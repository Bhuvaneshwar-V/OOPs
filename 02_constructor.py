class Computer:
    
    def __init__(self):
        self.name="Navin"
        self.age=28
    
    def update(self):
        self.age=30
    
    def compare(self, other):
        if self.age==other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

# every time you create an object it is allocated to new space
# print(id(c1))
# print(id(c2))

c1.name="Rashi"
#c1.age=12

# c1.update()

# print(c1.name)
# print(c2.name)

if c1.compare(c2):
    print('They are same')
else:
    print('They are different')
