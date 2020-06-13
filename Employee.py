from Person import Person
class Employee(Person):
    def __init__(self, firstName, lastName, email, SSN):
        self.SSN = SSN
        Person.__init__(self, firstName, lastName, email)

    def getSSN(self):
        return self.SSN

    def display(self):
        print("First Name: ", self.firstName, "\nLast Name: ", self.lastName, "\nEmail: ", self.email, "\nSSN: ", self.SSN)
        print()
