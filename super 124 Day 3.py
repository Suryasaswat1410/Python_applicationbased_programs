#list comprehension

#for loop version
result=[]
for i in range(11):
    result.append(i)
print(result)
#list comprehension method
print([i for i in range (11)])
#for loop version --->odd elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
print(result)
#list comprehension method---->odd elements
print([i for i in range(11) if i%2!=0])
#list comprehension method---->even elements
print([i for i in range(11) if i%2==0])

#for loop version--->odd elements & square of even elements
result=[]
for i in range(11):
    if i%2!=0:
        result.append(i)
    else :
        result.append(i**2)
print(result)
#list comprehension--->odd elements & square of even elements
print([i if i%2!=0 else i**2 for i in range(11)])
 


#qn 1
#mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#using for loop-->odd square it & even cube it
result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

for i in mat :
    for j in i:
        if j%2==0:
            result.append(j**3)
        else :
            result.append(j**2)
print(result)
#using list comprehension
print([j**2 if j%2!=0 else j**3 for i in mat for j in i])

result=[]
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
#output in matrix format using for loop
for i in mat :
    new=[]
    for j in i:
        if j%2==0:
            new.append(j**3)
        else :
            new.append(j**2)
    result.append(new)
print(result)
#output in matrix format using for list comprehension
print([[j**2 if j%2!=0 else j**3 for j in i] for i in mat])

#qn 2
#for each element in list_b,get the number & its position(index) in mylist as are turn list of tuples
#mylist=[9,3,6,1,5,0,8,2,4,7]
#list_b=[6,4,6,1,2,2]

mylist=[9,3,6,1,5,0,8,2,4,7]
list_b=[6,4,6,1,2,2]
result=[]
for i in list_b:
    result.append((i,mylist.index(i)))
print(result)
print(*set(result))#*set---removing the duplicate value
#list comprehension method
print([(i,mylist.index(i)) for i in list_b])
#dictionary function
result={}
for i in list_b:
    result[i]=mylist.index(i)
print(result)

#qn 3
#The goal is to tokenize the 5 sentences into words , excluding the stop words
#sentences=["a new world record was set","in the holy city of ayodhya","on the eve of diwali on tuesday",
#"with over three lakh diya or earthen lamps","lit up simultaneously on the banks of sarayu river"]
#stopwords=['for','a','of','the','and','to','in','on','with']

sentences=["a new world record was set",
           "in the holy city of ayodhya","on the eve of diwali on tuesday",
           "with over three lakh diya or earthen lamps",
           "lit up simultaneously on the banks of sarayu river"]
stopwords=['for','a','of','the','and','to','in','on','with']
result=[]
for i in sentences:
    new_data=[]
    for j in i.split():
        if j not in stopwords:
            new_data.append(j)
    result.append(new_data)
        
print(result)
#list comperhesion method
print([[word for word in sentence.split()
       if word not in stopwords]for sentence in sentences])


#qn 4
#input:a string of comma seprated numbers,the 5 & 8 are present in the list.Assume that 8 always comes after 5.
#case1:num1=add all the nos which donot lies btn. 5&8
#case2:num2=number formed by concanating all the numbers from 5 to 8
#output= sum of num1 & num2
ara=list(map(int,input().split(",")))
num1=sum(ara[:ara.index(5)])+sum(ara[ara.index(8)+1:])
print(num1)
l=ara[ara.index(5):ara.index(8)+1]
print(l)
num2=""
for i in l:
    num2+=str(i)
print(int(num2)+num1)

#qn 5
#string rotation
#input: rhtd:246 , ghftd:1246
#here every string is associated with a number separated by :
#-->if sum of squares of digits is even the rotate the string by 1
#-->if sum of squares of digits is odd the rotate the string left by 2 position

def sumSqrDigit(num):
    X = int(num)
    N = 0
    while(X>0):
        rev = X%10
        rev *= rev
        N += rev
        X = X//10
    return N
def rotateRight(string):
        n=''
        x=''
        n+=string[-1]
        x+=string[:-1:]
        x=n+x
        return x
def rotateLeft(string):
        n=''
        x=''
        n+=string[:2]
        x+=string[2:]
        x+=n
        return x
series = input().split(':')
for i in series:
    if(i.isdigit()):
        n=i
    else:
        stg=i
if(sumSqrDigit(n)%2==0):
    print(rotateRight(stg))
else:
    print(rotateLeft(stg))

#qn 6
#given a number n , write a program to find the sum of the largest prime factor of each of 9 consecutive numbers starting from n
#g(n)=f(n)+f(n+1)+f(n+2)+f(n+3)+f(n+4)+f(n+5)+f(n+6)+f(n+7)+f(n+8)
#where g(n) is sum & f(n) is the largest prime factor of n

def find_factors(num):
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
            return factors
def is_prime(num, i):
     if(i==1):
            return True
     elif(num%i==0):
            return False
     else:
            return(is_prime(num,i-1))
def find_largest_prime_factor(list_of_factors):
    large=[]
    for i in list_of_factors:
        if is_prime(i,i//2)==True:
            large.append(i)
            return max(large)
def find_f(num):
    f=find_factors(num)
    l=find_largest_prime_factor(f)
    return l

def find_g(num):
    sum=0
    consicutive=[i for i in range(num,num+9)]
    for i in consicutive:
        largest_prime_factor=find_f(i)
        sum=sum+largest_prime_factor
        return sum
print(find_g(10))
        
