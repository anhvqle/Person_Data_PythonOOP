from Person import Person
class Customer(Person):
    def __init__(self, firstName, lastName, email, IDNumber):
        self.IDNumber = IDNumber
        Person.__init__(self, firstName, lastName, email)

    def getIDNumber(self):
        return self.IDNumber
    def display(self):
        print("First Name: ", self.firstName, "\nLast Name: ", self.lastName, "\nEmail: ", self.email, "\nID: ",self.IDNumber)
        print()