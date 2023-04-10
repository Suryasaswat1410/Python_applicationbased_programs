#Linear Search

'''
def linearSearch(array,n,x):
    for i in range(0,n):
        if (array[i] == x):
            return i
    return -1
array = [2,4,0,1,9]
#x = 0 #key
x = int(input("Enter an Element :"))
n = len(array)
result = linearSearch(array,n,x)
if(result == -1):
    print("Elements not Found")
else:
    print("Element found at Index: ",result)
'''

#Binary Search

'''
def binarySearch(array,x,low,high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] <x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
array=[3,4,5,6,7,8,9]
x = int(input("Enter an Element :"))
res=binarySearch(array,x,0,len(array)-1)
if res != -1:
    print("Element is present at index : " + str(res))
else:
    print("Not found")

'''

#Tree Traversals
#Inorder => Left,Root,Right
#Preorder => Root,Left,Right
#Postorder => Left,Right,Root

'''
class Node:
    def __init__(self,item):
        self.left = None
        self.right = None
        self.val = item

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->",end='')
        inorder(root.right)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->",end='')
def preorder(root):
    if root:
        print(str(root.val) + "->",end='')
        postorder(root.left)
        postorder(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
print("Inorder traversal")
inorder(root)
print("\nPreorder traversal")
preorder(root)
print("\nPostorder traversal")
postorder(root)

'''


#Binary Search Tree Traversal

'''
class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->",end=' ')
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root,10)
root = insert(root,14)
root = insert(root, 4)
print("Inorder Traversal :",end =' ')
inorder(root)

'''

#Train Comp
'''
class Comp:
    def __init__(self,name,tot_cap,num_pass):
        self.name = name
        self.tot_cap = tot_cap
        self.num_pass = num_pass

class Train:
    def _init_(self, train_name, comp_list):
        self.train_name = train_name
        self.comp_list = comp_list

    def get_train_name(self):
        return train_name
    
    def get_comp_list(self):
        return comp_list
    
    def count_comp(self):
        return len(comp_list)

    def check_vacancy(self):
        count = 0
        for Comp in comp_list:
            if Comp.num_pass <= Comp.tot_cap * 0.5:
                count += 1
            return count
        

list=Comp()
c1=Comp("SL",250,400)
c2=Comp("2AC",125,280)
c3=Comp("3AC",120,300)
c4=Comp("FC",160,300)
c5=Comp("1AC",100,210)
list.atend(c1)
list.atend(c2)
list.atend(c3)
list.atend(c4)
list.atend(c5)

t1=train("Rajadhani",list)
t1.count_compartment()
t1.check_vacancy()
t1.get_comp()
print(t1.get_train_name())
'''

#Train Compartment
'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class linkedList:
    def __init__(self):
        self.headval=None
    def listPrint(self):
        temp=self.headval
        while temp is not None:
            print(temp.data.comp_name,temp.data.t_seat,temp.data.n_pass)
            print()
            temp=temp.next

    def atHead(self,data):
        newnode=node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            newnode.next=self.headval
            self.headval=newnode
    def atEnd(self,data):
        newnode=Node(data)
        if(self.headval==None):
            self.headval=newnode
        else:
            temp=self.headval
            while(temp.next != None):
                temp=temp.next
            temp.next=newnode

    def length(self):
        cnt=0
        temp=self.headval
        while temp is not None:
            cnt+=1
            temp=temp.next
        print(cnt)
   
class Train:
    def __init__(self,tname,c_list):
        self.tname=tname
        self.c_list=c_list

    def get_train_name(self):
        return self.tname
    
    def get_compartment(self):
        self.c_list.listPrint()

    def count_compartment(self):
        self.c_list.length()
    
    def check_vacancy(self):
        temp=self.c_list.headval
        cnt=0
        while temp is not None:
            if(temp.data.t_seat-temp.data.n_pass >= temp.data.t_seat//2):
                cnt+=1
            temp=temp.next
        print(cnt)

class Compartment:
    def __init__(self,comp_name,n_pass,t_seat):
        self.comp_name=comp_name
        self.t_seat=t_seat
        self.n_pass=n_pass


list1=linkedList()
c1=Compartment("SL",250,400)
c2=Compartment("2AC",125,280)
c3=Compartment("3AC",120,300)
c4=Compartment("FC",160,300)
c5=Compartment("1AC",100,210)
list1.atEnd(c1)
list1.atEnd(c2)
list1.atEnd(c3)
list1.atEnd(c4)
list1.atEnd(c5)

t1=Train("Raja Rani",list1)
t1.count_compartment()
t1.check_vacancy()
t1.get_compartment()
print(t1.get_train_name())

'''
