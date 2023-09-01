# Class Method :
# a)
class Student :
    college = "DTU"
    principal = "Dr. Chand"

    @classmethod
    def cm(cls) :
        print(f'college name is {cls.college}')
        print(f'principal name is {cls.principal}')

Student.cm()

#s1 = Student()
#s1.cm()


# b) modify static variable values using class method :
class Student :
    college = "DTU"
    principal = "Dr. Chand"

    @classmethod
    def cm(cls) :
        print(f'College name is {cls.college}')

    @classmethod
    def modify(cls) :
        cls.college = "DCE"

Student.cm()
Student.modify()
Student.cm()


# c) delete ststic variable values using class method :
class Student :
    college = "DTU"
    principal = "Dr. Chand"

    @classmethod
    def cm(cls) :
        print(f'College name is {cls.college}')

    @classmethod
    def modify(cls) :
        cls.college = "DCE"

    @classmethod
    def delete(cls) :
        del cls.principal

Student.cm()
Student.modify()
Student.cm()
Student.delete()

print(Student.__dict__)


# d)
class Student :
    college = "DTU"
    principal = "Dr. Chand"

    @classmethod
    def cm(cls) :
        print(f'College name is {cls.college}')

    @classmethod
    def modify(cls) :
        cls.college = "DCE"

    @classmethod
    def delete(cls) :
        del cls.principal

    @classmethod
    def create(cls) :
        cls.address = "ctc"

Student.cm()
Student.modify()
Student.cm()
Student.delete()
Student.create()

print(Student.__dict__)



# e) call class method inside another class method :
class Student :
    college = "DTU"
    principal = "Dr. Chand"

    @classmethod
    def cm(cls) :
        print(f'College name is {cls.college}')
        Student.delete()

    @classmethod
    def delete(cls) :
        del cls.principal


Student.cm()

print(Student.__dict__)

