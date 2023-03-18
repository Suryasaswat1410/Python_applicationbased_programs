'''
#problem statement
WeCare insurance company wants to calculate premium of vehicles.
Vehicles are of two types - "Two Wheeler" and "Four Wheeler".
Each vehicle is identified by vehicle id, type, cost and premium amount.
Premium amount is 2% of the vehicle cost for two wheelers and 6% of
the vehicle cost for four wheelers. Calculate the premium amount and
display the vehicle details.

Write a Python program to implement the class chosen with its 
attributes and methods.

Note:
Consider all instance variables to be private and methods to 
be public.
Include getter and setter methods for all instance variables 
Display appropriate error message, if the vehicle type is invalid.
Perform case sensitive string comparison 
Represent few objects of the class, initialize instance variables 
using setter methods, invoke appropriate methods and test your program.
#end
'''

def check_type(type):
    vehicle_type=['TwoWheeler', 'FourWheeler']
    if type not in vehicle_type:
            return 0
    return 1
class Vehicle:
    def __init__(self):
        self.__vehicle_cost=None
        self.__vehicle_id=None
        self.__vehicle_type=None
        self.__premium_amount=None
    def set_vehicle_id(self,vehicle_id):
        self.__vehicle_id=vehicle_id
    def set_vehicle_type(self,vehicle_type):
        if check_type(vehicle_type):
            self.__vehicle_type=vehicle_type
        else:
            return "invalid Vehicle DETAILS"
    def set_vehicle_cost(self,vehicle_cost):
        self.__vehicle_cost=vehicle_cost
    def get_vehicle_id(self):
        return self.__vehicle_id
    def get_vehicle_type(self):
        return self.__vehicle_type
    def get_vehicle_cost(self):
        return self.__vehicle_cost
    def set_premium_amount(self,premium_amount):
        self.__premium_amount=premium_amount
    def get_premium_amount(self):
        return self.__premium_amount
    def calculate_premium(self):
        if self.__vehicle_type=="TwoWheeler":
            self.__premium_amount=self.__vehicle_cost*2/100
        elif self.__vehicle_type=="FourWheeler":
            self.__premium_amount=self.__vehicle_cost*6/100
        else:
            print("Invalid Vehicle Type")
    def display_vehicle_details(self):
        print(self.__vehicle_type, self.__vehicle_cost, (self.__premium_amount))
v1 = Vehicle()
v1.set_vehicle_type(input())
v1.set_vehicle_cost(int(input()))
v1.calculate_premium()
v1.display_vehicle_details()
'''
###
#problem statement 2
A university wants to automate their admission process. Students are admitted based on marks scored in a qualifying exam.
A student is identified by student id, age and marks in qualifying exam.
Data are valid, if:
    Age is greater than 20
    Marks is between 0 and 100 (both inclusive)
    A student qualifies for admission, if
    Age and marks are valid and Marks is 65 or more.
Write a python program to represent the students seeking admission in the university.
RULES TO FOLLOW:
The details of student class are given below.
Class name: Student
--Attributes: (private)
               student_id
               marks
               age
Methods
(public)_init_()
     Create and initialize all instance variables to None
validate_marks()
     If data is valid, return true. Else, return false
validate_age()
     check_qualification()    Validate marks and age.
If valid, check if marks is 65 or more.
   if so return true
   else return false
   else return false
setter methods Include setter methods for all instance variables to get its values
getter methods Include getter methods for all instance variables to get its values


Continuing with the previous scenario, a student eligible for admission has to choose a course and pay the fees for it.
If they have scored more than 85 marks in qualifying exam, they get 25% discount on fees.

Valid course ids and fees are given below:

course id   fees
1001        25575.0
1002        15500.0
#end
###
'''
class Student:
    def init(self):
        self.__student_id = None
        self.__age = None
        self.__marks = 0
        self.__course_id = None
        self.__fees = None

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def get_course_id(self):
        return self.__course_id

    def get_fees(self):
        return self.__fees

    def validate_marks(self):
        if (self.__marks >= 0 and self.__marks <= 100):
            return True
        else:
            return False

    def validate_age(self):
        if (self.__age > 20):
            return True
        else:
            return False

    def check_qualification(self):
        if (self.__age > 20 and self.__marks >= 65 and self.validate_marks()):
            return True
        else:
            return False

    def choose_course(self, course_id):
        if (self.check_qualification() and (course_id == 1001 or course_id == 1002)):
            self.__course_id = course_id
            if (course_id == 1001):
                self.__fees = 25575.0
            elif (course_id == 1002):
                self.__fees = 15500.0
            if (self.__marks > 85):
                self.__fees = self.__fees - (self.__fees * 25 / 100)
            return True
        return False


maddy = Student()
maddy.set_student_id(1001)
maddy.set_age(21)
maddy.set_marks(84)
if (maddy.check_qualification()):
    print("Student has qualified")
    if (maddy.choose_course(1002)):
        print("Course allocated")
    else:
        print("Invalid course id")
else:
    print("Student has not qualified")



'''
###
#problem statement 3
PizzaForYou is a pizza store which sells different kinds of pizzas based on customer's order.40 min
Customer can either collect the order in person or opt for a door delivery.
Write a python program based on the class diagram given below.
Customer class:
validate_quantity(): A customer can order 1 to 5 pizzas
If quantity is valid, return true. Else return false
Pizzaservice class:
Initialize static variable counter to 100
Attribute, additional_topping is a boolean value which indicates whether additional topping is required or not.
True – additional topping is required, False – additional topping is not required
validate_pizza_type(): Customers can order "small" or "medium" type pizzas
If pizza type is valid, return true. Else return false
calculate_pizza_cost(): Calculate pizza cost
Validate pizza type and quantity
If valid,
Identify pizza cost based on details mentioned in the table
Set attribute, pizza_cost with the calculated pizza cost
Auto-generate service_id starting from 101 prefixed by first letter of pizza type. Example – S101, s102, m103, S104, M105 etc
If invalid, set pizza_cost to -1
PizzaType	Cost/Pizza(in Rs)	Additional topping cost/Pizza       (in Rs), if applicable
Small	150	35
Medium	200	50
Door delivery class:
validate_distance_in_kms(): Minimum distance for door delivery is 1km and maximum is 10kms
Validate distance_in_kms
If valid, return true. Else, return false
calculate_pizza_cost: Calculate pizza cost
Validate distance in kms
If valid,
Calculate pizza cost (Hint: Invoke overridden method in parent class)
If pizza_cost is not -1, identify delivery charge based on details mentioned below and add it to attribute, pizza_cost
Distance in kms	Delivery Charge in km(in Rs)
For first 5 kms	5
For remaining 5 kms	7
Else, set pizza_cost to -1
Note: Perform case insensitive string comparison
For testing:
Create objects of Pizzaservice and Doordelivery classes
Invoke calculate_pizza_cost() on Pizzaservice and Doordelivery objects
Display the details
'''

class Customer:
    def __init__(self, customer_name, quantity):
        self.__customer_name = customer_name
        self.__quantity = quantity

    def get_customer_name(self):
        return self.__customer_name

    def get_quantity(self):
        return self.__quantity

    def validate_quantity(self):
        if self.__quantity >= 1 and self.__quantity <= 5:
            return True
        return False


class Pizzaservice:
    counter = 100

    def __init__(self, customer, pizza_type, additional_topping=False):
        self.__service_id = None
        self.__customer = customer
        self.__pizza_type = pizza_type
        self.__additional_topping = additional_topping
        self.pizza_cost = None

    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small", "medium"]:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and self.__customer.validate_quantity():
            Pizzaservice.counter += 1
            if self.__pizza_type.lower() == "small":
                self.pizza_cost = 150 * self.__customer.get_quantity()
                if self.__additional_topping == True:
                    self.pizza_cost += 35 * self.__customer.get_quantity()
                self.__service_id = "S" + str(Pizzaservice.counter)
            if self.__pizza_type.lower() == "medium":
                self.pizza_cost = 200 * self.__customer.get_quantity()
                if self.__additional_topping == True:
                    self.pizza_cost += 50 * self.__customer.get_quantity()
                self.__service_id = "M" + str(Pizzaservice.counter)
        else:
            self.pizza_cost = -1

    def get_service_id(self):
        return self.__service_id

    def get_customer(self):
        return self.__customer

    def get_pizza_type(self):
        return self.__pizza_type

    def get_additional_topping(self):
        return self.__additional_topping


class Doordelivery(Pizzaservice):

    def __init__(self, customer, pizza_type, additional_topping, distance_in_kms):
        super().__init__(customer, pizza_type, additional_topping)
        self.__delivery_charge = None
        self.__distance_in_kms = distance_in_kms

    def validate_distance_in_kms(self):
        if self.__distance_in_kms >= 1 and self.__distance_in_kms <= 10:
            return True
        return False

    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.__distance_in_kms <= 5:
                    self.__delivery_charge = self.__distance_in_kms * 5
                else:
                    self.__delivery_charge = 25 + (self.__distance_in_kms - 5) * 7
                self.pizza_cost += self.__delivery_charge
        else:
            self.pizza_cost = -1

    def get_delivery_charge(self):
        return self.__delivery_charge

    def get_distance_in_kms(self):
        return self.__distance_in_kms
c=Customer("surya",4)
p=Pizzaservice(c,"medium",False)
d=Doordelivery(c,"medium",False,5)
print("Customer name:",c.get_customer_name())
print("Quantity is:",c.get_quantity())
print("valid quantity:",c.validate_quantity())
print("valid pizza type:",p.validate_pizza_type())
print("valid distance in kms:",d.validate_distance_in_kms())


