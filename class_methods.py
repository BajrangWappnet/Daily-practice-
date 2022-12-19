#creating class

class Employee:
    no_of_hoildays = 10
    no_of_vacations = 11

    name_of_company = "Wappnet Solution Pvt. Ltd."

    # Initializing Constructor 
    
    def __init__ (self, name, age, salary, role, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.role = role
        self.department = department

    
    def print_details(self):
        print(f"The name is {self.name}. Age of {self.name} is {self.age}.\nSalary is {self.salary} and department is {self.department}.")
        print(f"Role is {self.role}")


    @classmethod                   # To manupulate methods of class 
    def change_company_name(cls, new_company_name):
        cls.name_of_company = new_company_name




    # Creating object with name Bajrang
bajrang = Employee("Bajrang", 22, "5000", "Data Scientist","Main")  # He is the employee of Wappnet System Pvt. Ltd.
rakesh = Employee("Rakesh", 21, "500", "Data Engineer","Main")  # He is not the employee of wappnet System Pvt. Ltd.

# print(bajrang.salary)

print(f"Company of {bajrang.name} is {bajrang.name_of_company}")
print(f"Company of {rakesh.name} is {rakesh.name_of_company}")   # It will show company name as Wappnet System Pvt. ltd.

"""For Changing the class methods we use class method decorator which will change the class variable values """


rakesh.change_company_name("Pvt Solutions")

print(f"New Company name of {rakesh.name} is {rakesh.name_of_company}" )
    
