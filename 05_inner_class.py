class Student:

    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll_no)
        self.lap.show()

    class Laptop():
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'i5'
            self.ram = 8

        def show(self):
            print(self.brand, self.cpu, self.ram)
        

s1 = Student('Navin', 3)
s2 = Student('Jerry', 4)

s1.show()

# lap1 = s1.lap
# lap2 = s2.lap

# print(id(lap1))
# print(id(lap2))

#lap1 = Student.Laptop()
#print(lap1)