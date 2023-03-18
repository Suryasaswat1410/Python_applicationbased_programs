'''
#qn 1
#write a python function , nearest_palindrome() which accepts a number & returns the nearest palindrome greater than the given number
#sample i/p:-99  1221
#sample o/p:-101  1331
number=int(input())
def nearest_palindrome(number):
    
    number=number+1
    s=str(number)
    if s==s[::-1]:
        return number
    else :
        return nearest_palindrome(number)
print(nearest_palindrome(number))

#qn 2
#the patient is stored in a list.The details of medical specialities are stored in a dictionary as follows:
#{"P":"Pediatrics","O":"Orthopedics","E"="ENT"}
#WAP function to find medical speciality visited by the max. number of patients & return the name of the speciality

def list(i,j):
    
    P=i.count('P')
    E=i.count('E')
    O=i.count('O')
    if P>E and P>O:
        n=j['P']
    elif E>O :
        n=j['E']
    else:
        n=j['O']
    return n
i=[301,'P',302,'P',305,'P',401,'E',605,'E']
j={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
n=list(i,j)
print(n)


#qn 3
#WAP program to display all the common characters between two strings.Return -1 if no matching
#Note:Ignore blank spaces if there are any
#perform case sensitive string comparision wherever necessary
#sample input                          sample out put
#"I like Python"
#"Java is a very popular language"       lieyon

inp1=str(input())
inp2=str(input())
new=""
for i in inp1:
    if i==' ':
        continue 
    for j in inp2 :
        if i==j:
            new=new+i  #adding two strings
            #new.append(i)

print(*set(new))#*set-->remove duplicate values
       

#class & object
class example:
    def __init__(self,num):
        self.num=num

    def set_num(self,num):
        self.num=num

    def get_num(self):
        return self.num

obj=example(10)
print(obj.get_num())
obj.set_num(15)
print(obj.get_num())

#class
class customer:
    def __init__(self):
        self.cust__id=100
        
#
c1=customer()
print(c1.cust__id)

class customer:
     def __init__(self,id):
         self.id=100

c1=customer(200)
print(c1.id)

#waht is the o/p of the following code snipper ?
class book:
    def __init__(self):
        self.title=None
my_fav=book()
my_fav.title="Head First Programming"
your_fav=book()
your_fav.title="Learn python the hard way"

my_fav.title="Learning Python"

print("My favourite book is :",my_fav.title)
print("Your's favourite book is :",your_fav.title)

#
class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
s1=shoe(1000,"Nike")
print(s1)
print(s1.price,s1.material)
print("The unique id of the object",id(s1))
#
class shoe:
    def __init__(self,price,material):
        self.price=price
        self.material=material
    def __str__(self):
        return "shoe with price :"+str(self.price)+"\nand material:"+self.material
s1=shoe(1000,"Nike")
print(s1)

#
class mobile:
    def __init__(self):
        print(id(self))
    def display(self):
        print("Displaying details")

    def purchase(self):
        self.display()
        print("calculating price")

#mobile().purchase()
m1=mobile()
print(m1)
m2=mobile()
print(m2)
print(m1)
print(m2)


#problem statement
class Mobile:
    def __init__(self, brand, price):
        self.brand= brand
        self.price = price
        self.total_price = None
    def purchase(self):
        if self.brand == "Apple":
            discount=10
        else:
            discount = 5
        self.total_price = self.price-self.price *(discount / 100)
        print("Total price of", self.brand, "mobile is", self.total_price)
    def amount_returned(self):
        return(self.price-self.total_price)

mob1=Mobile("Apple",200000)
mob2=Mobile("Samsung",100000)
mob1.purchase()
mob2.purchase()
print(mob1.amount_returned())
print(mob2.amount_returned())

#problem statement
class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id= cust_id
        self.name=name
        self.age=age
        self.wallet_balance = wallet_balance
    def update_balance (self, amount):
        if amount < 1000 and amount > 0:
            self.wallet_balance += amount
    def show_balance (self):
            print("The balance is ", self.wallet_balance)
c1=Customer(100, "Gopal", 24, 1000)
c1.update_balance(500)
c1.show_balance()
'''
#Analyze the below code & identify how many objects & reference variable will be there at the end of line 9
class Table:
    def _init_(self):
        self.no_of_legs=4
        self.glass_top=None
        self.wooden_top=None
dining_table=Table()
back_table=Table()#
front_table=back_table
back_table=dining_table
print(dining_table, back_table,front_table)
