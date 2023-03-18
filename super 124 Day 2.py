'''
#list-->ordered--default index

list1=[]
print(list1,type(list1))
list2=[10,20,30,40]
print(list2,type(list2))
list3=[10,20.2,30+3j,True]
print(list3,type(list3))
list5=[101,201,301,402]
print(list5,type(list5))
list5.append(501)#add
print(list5,type(list5))
list5.extend([601,702,801])#extend
print(list5,type(list5))
list5.insert(0,51)#index,value
print(list5,type(list5))
list5.insert(3,61)#index,value
print(list5,type(list5))
list5.remove(801)
print(list5,type(list5))
list5.pop()#remove last element
print(list5,type(list5))
list5.pop(0)#remove 0th element
print(list5,type(list5))
del list5[1]#delete the particular position
print(list5,type(list5))

#sample qn 1
#wap which accepts a sentence & find out the number of letters & digits are present

def function(str1):
    letter=0
    digit=0
    for i in str1:
        if i.isalpha():#read the number of letters
            letter=letter+1
            
        elif i.isdigit():#read the number of digits
            digit=digit+1
        else :
            continue

    return [letter,digit]
print(function("Infosys 123"))
print(function("ABCDEFG")) 

#sample qn 2
#WAP to find pair of numbers which accepts a ;list of positive integers with no repeatations &returns count of pairs of numbers in the list that adds upto n
#returns count of pairs of numbers in the list that adds upto n


def listpair(list,n):

     count=0
     for x in list : #[1,2,7,4,5,6,0,3]
         index=list.index(x)+1 #index=1
         for y in range (index,len(list)):
             if x+list[y]==n:
                 count+=1
     return count
list=[1,2,7,4,5,6,0,3]
n=6
print(listpair(list,n))
list=[3,4,1,8,5,9,0,6]
n=9
print(listpair(list,n)) 

#sample qn 3
#WAP function which accepts a string & returns a string made of the first 2 & last 2 characters of given string
#if length is less than 2 return -1

def function1(str):
    if len(str)<2:
        return -1
    else:
        return str[0:2]+str[-2:]
print(function1("w3resource"))
print(function1("w3"))
print(function1("A")) 

#sample qn 4
#WAP function to add 'ing' at the end of the a given string
#if already ends with ing then add ly
#if string size 2 print as it is

def function2(string):
    length=len(string)
    if length>2 :
       if string[-3:]=='ing':
           string +='ly'
       else :
           string +='ing'
    return string
print(function2("sleep"))
print(function2("amazing"))
print(function2("is")) 


#sample qn 5
#Wap function to check a number which accepts a whole number & return true if
#1.the number & its double should have same number of digits
#2.both numbers should have same digit but it is in different order

def check(num):
    num1=str(num*2)
    num=str(num)
    count=0
    for x in num :
        if x in num1:
            count+=1
            
        else :
            return False
    if count==len(num):
        return True
print(check(4377))
print(check(125874))
print(check(243))  

#sample qn 6
#a treacher is generating marks of her class ,assume that the marks of 10 stuents r aviable in a tuple out of 25.
#find_more_than_avarege
#generate_frequency
#sort_marks
#list=(12,18,25,24,2,5,18,20,20,21)
def find_more_than_average(tup):
    avg=sum(tup)/len(tup)
    count=0
    for i in tup:
        if (i>avg):
            count+=1
    print(count*10)
def generate_freq(tup):
    l=[]
    for i in range(0,26):
        l.append(tup.count(i))
    print(l)
def sort_marks(tup):
    print(sorted(list(tup)))
tup=tuple(map(int,input().split()))
find_more_than_average(tup)
generate_freq(tup)      
sort_marks(tup)

#sample qn 7
#repfesent a small bilingual (english-swedish)glossry given as a python dictionary
#{"marry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
def translate(dict1,list1):
    list2=[]
    for i in list1:
        list2.append(dict1[i])
    return list2
dict1={"merry":"god","christmas":"jul","and":"och","happy":"gott","new":"nytt","year":"ar"}
list1=["merry","christmas"]
print(translate(dict1,list1))'''


#sample qn 8
#find no of distinct subarrays in an array of position integers such that sum of subarray is an odd integer,
#two subarray are considered different
#if they start or end at diferent index input
#1
#3
#1 2 3
#[1] [1,2] [1,2,3] [2] [2,3] [3]
#4
n1=int(input("Enter a value for n1"))
n2=int(input("Enter a value for n2"))
result=[]
for i in range(n1,n2+1):
    result.append(i)
print(result)
result=[i for i in range(n1,n2+1)]
print(result) 






