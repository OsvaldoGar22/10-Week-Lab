
# Exercise 1 - Pet Class
#
# class Pet:
#     def __init__(self, name, animal_type, age):
#         self.__name = name
#         self.__animal_type = animal_type 
#         self.__age = age 
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_animal_type(self, animal_type):
#         self.__animal_type = animal_type 
#
#     def set_age(self, age):
#         self.__age = age 
#
#     def get_name(self):
#         return self.__name
#
#     def get_animal_type(self):
#         return self.__animal_type
#
#     def get_age(self):
#         return self.__age
#
#
# name = input("What is your pet's name? ")
# animal_type = input("What type of animal is that? ")
# age = input("How old is your pet? ")
#
# my_pet = Pet(name, animal_type, age)
#
# print("Here is the information you entered:")
# print(f"Pet Name: {my_pet.get_name()}")
# print(f"Animal Type: {my_pet.get_animal_type()}")
# print(f"Age: {my_pet.get_age()}")

#------------------------------------------------------------------

# Exercise 2 - Car Class

# class Car:
#     def __init__(self, year_model, make, speed):
#         self.__year_model = year_model
#         self.__make = make
#         self.__speed = speed
#
#     def set_year_model(self, year_model):
#         self.__year_model = year_model
#
#     def set_make(self, make):
#         self.__make = make
#
#     def set_speed(self, speed):
#         self.__speed = speed 
#
#     def get_year_model(self):
#         return self.__year_model
#
#     def get_make(self):
#         return self.__make
#
#     def get_speed(self):
#         return self.__speed
#     
#     def accelerate(self):
#         self.__speed += 5
#
#     def brake(self):
#         if self.__speed >= 5:
#             self.__speed -= 5
#         else:
#             self.__speed = 0
#
# year_model = input("What is the model year of your car: ")
# make = input("What is the make of your car: ")
# speed = 0
#
# my_car = Car(year_model, make, speed)
#
# print("Accelerating:")
# for i in range(5):
#     my_car.accelerate()
#     print(f"Current speed: {my_car.get_speed()}")
#
# print("Braking:")
# for i in range(5):
#     my_car.brake()
#     print(f"Current speed: {my_car.get_speed()}")

#------------------------------------------------------------------

# Exercise 3 - Personal Information Class

# class Info:
#     def __init__(self, name, address, age, phone_number):
#         self.__name = name
#         self.__address = address 
#         self.__age = age 
#         self.__phone_number = phone_number 
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_address(self, address):
#         self.__address = address 
#         
#     def set_age(self, age):
#         self.__age = age
#
#     def set_phone_number(self, phone_number):
#         self.__phone_number = phone_number 
#
#     def get_name(self):
#         return self.__name
#
#     def get_address(self):
#         return self.__address
#
#     def get_age(self):
#         return self.__age
#
#     def get_phone_number(self):
#         return self.__phone_number
#
# person1 = Info("David", "123 Hello Street", 22, "123-344-5786")
# person2 = Info("Ivan", "370 Bye Hill", 28, "221-843-5322")
# person3 = Info("Brian", "813 Brain Lane", 29, "428-324-9822")
#
# print("Person 1:")
# print(f"Name: {person1.get_name()}")
# print(f"Address: {person1.get_address()}")
# print(f"Age: {person1.get_age()}")
# print(f"Phone Number: {person1.get_phone_number()}")
# print()
#
# print("Person 2:")
# print(f"Name: {person2.get_name()}")
# print(f"Address: {person2.get_address()}")
# print(f"Age: {person2.get_age()}")
# print(f"Phone Number: {person2.get_phone_number()}")
# print()
#
# print("Person 3:")
# print(f"Name: {person3.get_name()}")
# print(f"Address: {person3.get_address()}")
# print(f"Age: {person3.get_age()}")
# print(f"Phone Number: {person3.get_phone_number()}")

#------------------------------------------------------------------

# Exercise 4 - Employee Class
#
# class Employee:
#     def __init__(self, name, id_number, department, job_title):
#         self.__name = name
#         self.__id_number = id_number
#         self.__department = department
#         self.__job_title = job_title
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_id_number(self, id_number):
#         self.__id_number = id_number
#
#     def set_department(self, department):
#         self.__department = department
#
#     def set_job_title(self, job_title):
#         self.__job_title = job_title
#
#     def get_name(self):
#         return self.__name
#
#     def get_id_number(self):
#         return self.__id_number
#
#     def get_department(self):
#         return self.__department
#
#     def get_job_title(self):
#         return self.__job_title
#
# emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
# emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
# emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")
#
#
# print("Employee 1:")
# print(f"Name: {emp1.get_name()}")
# print(f"ID Number: {emp1.get_id_number()}")
# print(f"Department: {emp1.get_department()}")
# print(f"Job Title: {emp1.get_job_title()}")
# print()
#
# print("Employee 2:")
# print(f"Name: {emp2.get_name()}")
# print(f"ID Number: {emp2.get_id_number()}")
# print(f"Department: {emp2.get_department()}")
# print(f"Job Title: {emp2.get_job_title()}")
# print()
#
# print("Employee 3:")
# print(f"Name: {emp3.get_name()}")
# print(f"ID Number: {emp3.get_id_number()}")
# print(f"Department: {emp3.get_department()}")
# print(f"Job Title: {emp3.get_job_title()}")

#------------------------------------------------------------------

# Exercise 5 - Retailtem Class
#
# class RetailItem:
#     def __init__(self, description, units, price):
#         self.__description = description
#         self.__units = units
#         self.__price = price
#
#     def set_description(self, description):
#         self.__description = description
#
#     def set_units(self, units):
#         self.__units = units 
#
#     def set_price(self, price):
#         self.__price = price
#
#     def get_description(self):
#         return self.__description
#
#     def get_units(self):
#         return self.__units
#
#     def get_price(self):
#         return self.__price
#
# item1 = RetailItem("Jacket", 12, 59.95)
# item2 = RetailItem("Designer Jeans", 40, 34.95)
# item3 = RetailItem("Shirt", 20, 24.95)
#
# print("Item 1:")
# print(f"Description: {item1.get_description()}")
# print(f"Units in Inventory: {item1.get_units()}")
# print(f"Price: {item1.get_price()}")
# print()
#
# print("Item 2:")
# print(f"Description: {item2.get_description()}")
# print(f"Units in Inventory: {item2.get_units()}")
# print(f"Price: {item2.get_price()}")
# print()
#
# print("Item 3:")
# print(f"Description: {item3.get_description()}")
# print(f"Units in Inventory: {item3.get_units()}")
# print(f"Price: {item3.get_price()}")
# print()

#------------------------------------------------------------------

# Exercise 6 - Patient Charges

class Patient:
    def __init__(self, first_name, middle_name, last_name, address, city, state, zip_code, phone_number, emergency_contact_name, emergency_contact_phone):
        self.__first_name = first_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone_number = phone_number
        self.__emergency_contact_name = emergency_contact_name
        self.__emergency_contact_phone = emergency_contact_phone

    def get_first_name(self):
        return self.__first_name

    def get_middle_name(self):
        return self.__middle_name

    def get_last_name(self):
        return self.__last_name

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone_number(self):
        return self.__phone_number

    def get_emergency_contact_name(self):
        return self.__emergency_contact_name

    def get_emergency_contact_phone(self):
        return self.__emergency_contact_phone

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_middle_name(self, middle_name):
        self.__middle_name = middle_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_emergency_contact_name(self, emergency_contact_name):
        self.__emergency_contact_name = emergency_contact_name

    def set_emergency_contact_phone(self, emergency_contact_phone):
        self.__emergency_contact_phone = emergency_contact_phone


class Procedure:
    def __init__(self, procedure_name, procedure_date, practitioner_name, procedure_charges):
        self.__procedure_name = procedure_name
        self.__procedure_date = procedure_date
        self.__practitioner_name = practitioner_name
        self.__procedure_charges = procedure_charges

    def get_procedure_name(self):
        return self.__procedure_name

    def get_procedure_date(self):
        return self.__procedure_date

    def get_practitioner_name(self):
        return self.__practitioner_name

    def get_procedure_charges(self):
        return self.__procedure_charges

    def set_procedure_name(self, procedure_name):
        self.__procedure_name = procedure_name

    def set_procedure_date(self, procedure_date):
        self.__procedure_date = procedure_date

    def set_practitioner_name(self, practitioner_name):
        self.__practitioner_name = practitioner_name

    def set_procedure_charges(self, procedure_charges):
        self.__procedure_charges = procedure_charges

patient = Patient(
    first_name="David",
    middle_name="M.",
    last_name="Joe",
    address="123 Hello St",
    city="Riverside",
    state="CA",
    zip_code="92044",
    phone_number="123-344-5786",
    emergency_contact_name="Ivan Gold",
    emergency_contact_phone="324-555-5678"
)

# Create three instances of the Procedure class with sample data
procedure1 = Procedure(
    procedure_name = "Physical Exam",
    procedure_date = "2024-11-12",
    practitioner_name = "Dr. Irvine",
    procedure_charges = 250.0
)

procedure2 = Procedure(
    procedure_name = "X-ray",
    procedure_date = "2024-11-13",
    practitioner_name = "Dr. Jamison",
    procedure_charges = 500.0 
)

procedure3 = Procedure(
    procedure_name = "Blood Test",
    procedure_date = "2024-11-14",
    practitioner_name = "Dr. Smith",
    procedure_charges = 200.0
)

print("Patient Information")
print("")

print(f"Name: {patient.get_first_name()} {patient.get_middle_name()} {patient.get_last_name()}")
print(f"Address: {patient.get_address()}")
print(f"City: {patient.get_city()}")
print(f"State: {patient.get_state()}")
print(f"ZIP Code: {patient.get_zip_code()}")
print(f"Phone Number: {patient.get_phone_number()}")
print(f"Emergency Contact: {patient.get_emergency_contact_name()}")
print(f"Emergency Contact Phone: {patient.get_emergency_contact_phone()}")
print()

print("Procedures")
print("")

print("Procedure 1:")
print(f"Name: {procedure1.get_procedure_name()}")
print(f"Date: {procedure1.get_procedure_date()}")
print(f"Practitioner: {procedure1.get_practitioner_name()}")
print(f"Charges: ${procedure1.get_procedure_charges():,.2f}")
print()

print("Procedure 2:")
print(f"Name: {procedure2.get_procedure_name()}")
print(f"Date: {procedure2.get_procedure_date()}")
print(f"Practitioner: {procedure2.get_practitioner_name()}")
print(f"Charges: ${procedure2.get_procedure_charges():,.2f}")
print()

print("Procedure 3:")
print(f"Name: {procedure3.get_procedure_name()}")
print(f"Date: {procedure3.get_procedure_date()}")
print(f"Practitioner: {procedure3.get_practitioner_name()}")
print(f"Charges: ${procedure3.get_procedure_charges():,.2f}")
print()

total_charges = (
    procedure1.get_procedure_charges() +
    procedure2.get_procedure_charges() +
    procedure3.get_procedure_charges()
)

print(f"Total Charges: ${total_charges:,.2f}")
















