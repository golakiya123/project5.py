class Person:
    def __init__(self, n, a):
        self.n = n
        self.a = a

    def show(self):
        print("Name:", self.n)
        print("Age:", self.a)


class Employee(Person):
    def __init__(self, n, a, i, s):
        super().__init__(n, a)
        self.i = i
        self.s = s

    def show(self):
        super().show()
        print("ID:", self.i)
        print("Salary:", self.s)


class Manager(Employee):
    def __init__(self, n, a, i, s, d):
        super().__init__(n, a, i, s)
        self.d = d

    def show(self):
        super().show()
        print("Department:", self.d)


print("Python OOP Project: Employee Management System:")

print("\nchoose an opration:")
print("1. Create Person")
print("2. Create Employee")
print("3. Create Manager")
print("4. Show Details")
print("5. Exit")


while True:

    c = int(input("\nEnter Choice: "))

    if c == 1:
        n = input("Name: ")
        a = int(input("Age: "))

        p = Person(n, a)

        print("Person created with Name:", n, "and Age:", a)

    elif c == 2:
        n = input("Name: ")
        a = int(input("Age: "))
        i = input("ID: ")
        s = int(input("Salary: "))

        employee = Employee(n, a, i, s)

        print("Employee created with Name:", n,"Age:", a,"ID:", i,"and Salary:", s)

    elif c == 3:
        n = input("Name: ")
        a = int(input("Age: "))
        i = input("ID: ")
        s = int(input("Salary: "))
        d = input("Department: ")

        m = Manager(n, a, i, s, d)

        print("Manager created with Name:", n,"Age:", a,"ID:", i,"Salary:", s,"and Department:", d)

    elif c == 4:
        print("\n1. Person")
        print("2. Employee")
        print("3. Manager")

        sub = int(input("Enter Choice: "))

        if sub == 1:
            print("\nPerson Details:")
            p.show()

        elif sub == 2:
            print("\nEmployee Details:")
            employee.show()

        elif sub == 3:
            print("\nManager Details:")
            m.show()

        else:
            print("Invalid Choice")

    elif c == 5:
        print("Goodbye!!")
        break

    else:
        print("Invalid Choice")
