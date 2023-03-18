'''
#decision making statements

num=int(input("Enter a number"))
print(num,type(num))
if num%3==0 & num%5==0 :
    print("it is a multiple of both")
elif num%3==0:
    print("it is multiple of 3")
elif num%5==0:
    print("it is multiple of 5")
else :
    print("invalid")
    
#print(*no of objects,sep=' ',end='/n')
#for loop
#range function
#1 to 100
for i in range(1,101): #range(start,end,step)
    print(i,end=' ')
print()
#100 to 1
for i in range(100,0,-1): #range(start,end,step)
    print(i,end=' ')
print()
# odd number btn 1 to 100
for i in range(1,101,2):
    print(i,end=' ')
print()
#100 to 1
for i in range(99,0,-2):
    print(i,end=' ')
print()
# even number btn 1 to 100
for i in range(0,101,2):
    print(i,end=' ')
print()
#100 to 0
for i in range(100,-1,-2):
    print(i,end=' ')
print() '''

'''#break
for i in range(1,101):
 if i==50:
     break
 print(i,end=' ')
else :
    print("else")

#continue

for i in range(1,101):
 if i==50:
     continue
 print(i,end=' ')
#pass (it creates a empty statement)
for i in range(1,101):
 if i==50:
     pass
 print(i,end=' ')
#functions

def function1():
  print("its function1")
function1()
def function2(n1,n2):
  print("num1=",n1,"num2=",n2)
  #print()_str_-----Doubt
function2(10,20)
def function3(n1,n2):
    n3=n1+n2
    return n3
print("addition is ",function3(100,200))
def function4(n1,n2):
    n3=n1+n2
    return n3
print("addition is ",function4(10,20.2)) 
def function5(n1,n2):
    n3=float(n1)+n2
    return n3
print("addition is ",function5('10',20.2)) 

#catagories of functions
#based on arguments
#1.positional arguments
def function1(num1,num2,num3,num4):
   print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
#function1(10,20,30)TypeError: function1() missing 1 required positional argument: 'num4'
function1(10,20,30,40)
#2.keyword arguments
def function2(num1,num2,num3,num4):
   print("num1",num1,"num2",num2,"num3",num3,"num4",num4)
function2(num4=10,num1=20,num2=30,num3=40)
function2(num4=10,num1=20,num2=10,num3=40)
#3.default arguments
def function3(name,rollno,branch,collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("aditya",11,"CSE")
function3("SURYA",58,"ECE")
function3("random",13,"CSE")
function3("harsha",31,"CST")

def function3(name,rollno,branch="CSE",collegename="GIET"):
    print(name,rollno,branch,collegename)
function3("aditya",11)
function3("SURYA",58,"ECE")
function3("random",13)
function3("harsha",31,"CST")

#4.variable no of arguments
def function4(*var):#tuple=
    for i in var:
        print(i,end=' ')
function4(10,20)
print()
function4(10,20,30,40)
print()
function4(10,20,30,40,50,60)
print()
def add(*var):#tuple=
    sum1=0
    for i in var:#10,20
        sum1=sum1+i
    print(sum1)
add(10,20)
print()
add(10,20,30,40)
print()
add(10,20,30,40,50,60)
{ OR part
    return(sum1)
    print(add(10,20))
    print(add(10,20,30,40))
    print(add(10,20,30,40,50,60)) }
next qn 
#sample question 1

n1=int(input())
n2=int(input())
n3=int(input())
if n1==7 :
    print(n2*n3)
elif n2==7 :
    print(n3)
elif n3==7 :
    print(-1)
else :
    print(n1*n2*n3)


#sample question 2
def conversion(Amount INR,curr):
    if curr=="Euro" 

#sample question 3
adult=int(input("Enter the number of adults"))
children=int(input("Enter the number of children"))
total=(((adult*37550.0)+(children*37550.0/3))*1.07)*0.90
print(total) '''
#sample qn 4
def coinchange(coins,notes,totalamount) :
    if totalamount<((coins*1)+(notes*5)):
     notes=int(totalamount/5)  
     print(notes)
     coins=totalamount%5
     print(coins)
    else:
        print(-1)
coinchange(2,4,21)
coinchange(11,2,11)
coinchange(3,3,19)


    
