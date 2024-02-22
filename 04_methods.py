class Student:
 
    school = 'Telsuko' # class variable

    def __init__(self, m1, m2, m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3


    # instance method
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    # accessor
    def get_m1(self):
        return self.m1 
    
    # mutator
    def set_m1(self, value):
        self.m1 = value

    @classmethod
    # class method
    def getSchool(cls):
        return cls.school
    
    @staticmethod
    def info():
        return "This is a student class"

s1 = Student(34, 57, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(Student.getSchool())
print(Student.info())
