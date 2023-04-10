#Selection Sort

'''
def selectionSort(array,size):
    for step in range(size):
        min_index = step
        for i in range(step+1,size):
            if array[i] < array[min_index]:
                min_index = i
        (array[step],array[min_index]) = (array[min_index],array[step])

data = [20,12,10,15,2]
size = len(data)
selectionSort(data,size)
print("No.of Array's :",size)
print("Sorted Array  in Ascending Order :",data)

'''

#Quick Sort
'''
def partitation(array,low,high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot :
            i = i + 1
            (array[i],array[j] == array[j],array[i])
    (array[i+1],array[high]) = (array[high],array[i+1])
    return i+1

def quickSort(array,low,high):
    if low<high:
        pi = partitation(array,low,high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

data = [8, 7, 6, 1, 0, 9, 2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
'''

#Coorg Fruit Farm
'''
class FruitInfo:
    fruit_name_list = ['Apple', 'Guava', 'Orange', 'Grape', 'Sweet Lime']
    fruit_price_list = [200, 80, 70, 110, 60]

    def get_fruit_price(fruit_name):
        if fruit_name in FruitInfo.fruit_name_list:
            index = FruitInfo.fruit_name_list.index(fruit_name)
            return FruitInfo.fruit_price_list[index]
        else:
            return -1

class Purchase:
    counter = 101

    def __init__ (self, customer, fruit_name, quantity):
        self.__purchase_id = 'P' + str(Purchase.counter)
        Purchase.counter += 1
        self.__customer = customer
        self.__fruit_name = fruit_name
        self.__quantity = quantity

    def calculate_price(self):
        price_per_kg = FruitInfo.get_fruit_price(self.__fruit_name)
        if price_per_kg == -1:
            return -1

        total_price = price_per_kg * self.__quantity

        if price_per_kg == max(FruitInfo.fruit_price_list) and self.__quantity > 1:
            total_price *= 0.98  # 2% discount
        elif price_per_kg == min(FruitInfo.fruit_price_list) and self.__quantity >= 5:
            total_price *= 0.95  # 5% discount

        if self.__customer == 'wholesale':
            total_price *= 0.9  # 10% discount

        return total_price

    def get_purchase_id(self):
        return self.__purchase_id

    def get_customer(self):
        return self.__customer

    def get_fruit_name(self):
        return self.__fruit_name

    def get_quantity(self):
        return self.__quantity

class Customer:
    def __init__(self, customer_name):
        self.__customer_name = customer_name

    def get_customer_name(self):
        return self.__customer_name


customer1 = Customer('Litu')
purchase1 = Purchase(customer1.get_customer_name(), 'Apple', 2)
print(purchase1.calculate_price())

customer2 = Customer('Harsha')
purchase2 = Purchase(customer2.get_customer_name(), 'Grape', 6)
print(purchase2.calculate_price())

customer3 = Customer('Sumit')
purchase3 = Purchase(customer3.get_customer_name(), 'Mango', 4)
print(purchase3.calculate_price())

'''

# BakeHouse Owner

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def _init_(self):
        self.head = None
        
    def add(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next is not None:
                curr_node = curr_node.next
            curr_node.next = new_node
            
    def reverse(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node
                           

class BakeHouse:
    def __init__(self):
        self.occupied_table_list = []

    def get_occupied_table_list(self):
        return self.occupied_table_list

    def allocate_table(self):
        if len(self.occupied_table_list) == 0:
            table_number = 1
            self.occupied_table_list.append(table_number)
            return table_number
        else:
            for i in range(len(self.occupied_table_list)):
                if i == len(self.occupied_table_list) - 1:
                    table_number = self.occupied_table_list[i] + 1
                    self.occupied_table_list.append(table_number)
                    return table_number
                elif self.occupied_table_list[i+1] - self.occupied_table_list[i] > 1:
                    table_number = self.occupied_table_list[i] + 1
                    self.occupied_table_list.insert(i+1, table_number)
                    return table_number

    def deallocate_table(self, table_number):
        if table_number in self.occupied_table_list:
            self.occupied_table_list.remove(table_number)
        else:
            print(f"Table {table_number} is not occupied.")


bh = BakeHouse()
print(bh.get_occupied_table_list())
print(bh.allocate_table())

print(bh.get_occupied_table_list()) 
print(bh.allocate_table())

print(bh.get_occupied_table_list())
bh.deallocate_table(2)
print(bh.get_occupied_table_list())
print(bh.allocate_table())
print(bh.get_occupied_table_list())
print(bh.allocate_table())
print(bh.get_occupied_table_list())
print(bh.allocate_table())
print(bh.get_occupied_table_list())
print(bh.allocate_table())
print(bh.get_occupied_table_list())
bh.deallocate_table(3)
print(bh.get_occupied_table_list())


'''


'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SortList:  
    def __init__(self):  
        self.head = None  
        self.tail = None  
          
    def addNode(self, data):  
        newNode = Node(data) 
          
        if(self.head == None):  
            self.head = newNode  
            self.tail = newNode  
        else:  
            self.tail.next = newNode  
            self.tail = newNode  
              
    def sortList(self):  
        current = self.head  
        index = None
        l=[] 
        if(self.head == None):  
            return 
        else:  
            while(current != None):  
                index = current.next  
                  
                while(index != None):  
                    if(current.data > index.data):  
                        temp = current.data  
                        current.data = index.data  
                        index.data = temp
                    index = index.next
                current = current.next  
                l.append(index) 
            
    def display(self):  
        current = self.head
        if(self.head == None):  
            print("List is empty")
            return
        while(current != None):  
            print(current.data)  
            current = current.next
        return " "
    def replace(self,data):
        current = self.head
        while(current.next.next != None):
            current = current.next
        current.next.item=data
        return curent.next.item
    def deallocation(self,x):
              if self.head is None:
                  print("The list has no element to delete")
                  return
              if self.head.data==x:
                  self.head=self.head.next
                  return
              n=self.head
              while n.next is not None:
                  if n.next.data==x:
                      break
                  n=n.next
              if n.next==None:
                  print("item not found in the list")
              else:
                  n.next=n.next.next
    def allocation(self,index,data):
        if index==1:
            Newnode=Node(data)
            Newnode.next=self.head
            self.head=Newnode
        i=1
        n=self.head
        while i<index-1 and n is not None:
            i+=1
            n=n.ref
        if n is None:
            print("index out of range")
        else:
            Newnode=Node(data)
            Newnode.next=n.next
            n.next=Newnode     

sList = SortList();    
sList.addNode(9);  
sList.addNode(7);  
sList.addNode(2);  
sList.addNode(5);  
sList.addNode(4);  
print(sList.display())  
sList.deallocation(2)
print(sList.display()) 
sList.allocation(1,2)
print(sList.display())
'''

#Chocolate
'''
class ChocolateCamp:
    def __init__(self, child_id, chocolates_received):
        self.child_id = child_id
        self.chocolates_received = chocolates_received
    
    def calculate_total_chocolates(self):
        total_chocolates = sum(self.chocolates_received)
        return total_chocolates
    
    def reward_child(self, child_id_rewarded, extra_chocolates):
        if extra_chocolates < 1:
            print("Extra chocolates is less than 1")
            return
        try:
            index = self.child_id.index(child_id_rewarded)
            self.chocolates_received[index] += extra_chocolates
        except ValueError:
            print("Child id is invalid")
            return
        print("Updated chocolates received list:", self.chocolates_received)


child_id = (10, 20, 30, 40, 50)
chocolates_received = [12, 5, 3, 4, 6]

camp = ChocolateCamp(child_id, chocolates_received)
print("Total chocolates received by all children:", camp.calculate_total_chocolates())

camp.reward_child(20, 3)  
camp.reward_child(60, 5)
camp.reward_child(30, -2)
'''


#Frequency

'''
class Node:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, word, freq):
        new_node = Node(word, freq)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.word, current_node.freq)
                current_node = current_node.next

text = input("Enter some text: ")
text = text.lower()
words = text.split()
linked_list = LinkedList()
for word in words:
    current_node = linked_list.head
    while current_node is not None:
        if current_node.word == word:
            current_node.freq += 1
            break
        current_node = current_node.next
    else:
        linked_list.insert(word, 1)

max_freq = 0
max_word = ""
current_node = linked_list.head
while current_node is not None:
    if current_node.freq > max_freq:
        max_freq = current_node.freq
        max_word = current_node.word
    elif current_node.freq == max_freq:
        if len(current_node.word) > len(max_word):
            max_word = current_node.word
    current_node = current_node.next
print(max_word, max_freq)

'''

#Check_anagram()

'''
def check_anagram(data1,data2):
    
    st1=data1.lower()
    st2=data2.lower()
    if len(data1)!=len(data2): 
        return False
    
    list1=[]
    list2=[]
    for i in st1:  
        list1.append(i)
    for i in st2:
        list2.append(i)
    flag=1 
    for i in range(0,len(data1)):  
        if list1[i]==list2[i]:
            flag=0 
            break
        
    if flag==0:
        return False
    
    list1.sort()
    list2.sort()
    
    if list1==list2:  
        return True 
    else:
        return False
print(check_anagram("eat","ate"))
print(check_anagram("dfoo","food"))

'''
