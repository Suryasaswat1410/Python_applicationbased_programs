#Deletion of Binary Tree

'''
class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)
def insert(node,key):
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node

def minValueNode(node):
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root,key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left,key)
    elif key > root.key:
        root.right = deleteNode(root.right,key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right,temp.key)
    return root

root = None
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 3)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)
 
print("Inorder traversal of the given tree")
inorder(root)
 
print("\nDelete 3")
root = deleteNode(root, 3)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 8")
root = deleteNode(root, 8)
print("Inorder traversal of the modified tree")
inorder(root)
 
print("\nDelete 4")
root = deleteNode(root, 4)
print("Inorder traversal of the modified tree")
inorder(root)

'''

#Merge List
'''
WAP function which accepts two linked lists containing interger data and an
integer , n and merges the two linked lists, such that list2 is merged with
list1 after n number of nodes.
Note :- Assume the value of n1 will always be less than or equal to the no.of
nodes in list1.

Sample Input
list1 = 1->2->4->3->5
list2 = 9->8->11

Experted Output
n = 2 
1->2->9->8->11->4->3->5
'''

'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedList:
    def __init__(self):
        self.head = None

    def push(self,new_data):
        new_data = Node(new_data)
        new_data.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        print(temp.data,end='')
        temp = temp.next

list1=Linkedlist()
list2=Linkedlist()
list1.push(1)
list1.push(4)
list1.push(3)
list1.push(5)
list2.push(9)
list2.push(8)
list2.push(11)
n=int(input())
list3=[]
for i in list1:
    if list1[i]==n:
        list1.(list2)
        
list1.printlist()
list2.printlist()


'''
#No.of Males and Females in Queue

'''
class Queue:
    def __init__(self,max_size):
        self.__rear=-1
        self.__front=0
        self.__max_size=max_size
        self.__element=[None]*self.__max_size
       
    def is_full(self):
        if(self.__rear==self.__max_size-1):
            return True
        return False
    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False
    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.__rear+=1
            self.__element[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            data=self.__element[self.__rear]
            self.__front+=1
        return data
    def display(self):
        for index in range(self.__front,self.__rear+1):
              print(self.__element[index])
    def get_max_marks(self):
        return self.__max_size
    def gender(self):
        count=0
        count1=0
        if(self.is_empty()):
            print("Queue is empty")
        for index in range(self.__front,self.__rear+1):
            if self.__element[index]=="Male":
                count+=1
            elif self.__element[index]=="Female": 
                count1+=1
        return count,count1
                
queue1=Queue(5)
queue1.enqueue("Male")
queue1.enqueue("Female")
queue1.enqueue("Female")
queue1.enqueue("Female")
queue1.enqueue("Male")
print(queue1.gender())

'''





