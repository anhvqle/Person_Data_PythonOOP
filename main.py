from Customer import Customer
from Employee import Employee
from Person import Person
while True:
    inp = input("Customer or employee? (c/e): ")
    print()
    print("DATA ENTRY")
    if inp == "c":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        while True:
            email_address = input("Email: ")
            if not '@' in email_address:
                print("Enter a valid email address")
            else:
                break;
        ID_number = input("Number: ")
        customer_object = Customer(first_name, last_name, email_address, ID_number)
        print()
        print("CUSTOMER")
        customer_object.display()
    elif inp == "e":
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email_address = input("Email: ")
        SSN_number = input("SSN: ")
        employee_object = Employee(first_name, last_name, email_address, SSN_number)
        print()
        print("EMPLOYEE")
        employee_object.display()

    ending = input("Continue? (y/n): ")
    print()
    if ending == "y":
        continue
    elif ending == "n":
        print("Bye!")
        break