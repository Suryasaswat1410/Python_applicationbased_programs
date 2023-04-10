#Single Linked List
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next= None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def push(self,new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

list1 = LinkedList()
list1.push(20)
list1.push(4)
list1.push(15)
list1.push(85)
print("Given Linked List:")
list1.printList()
list1.reverse()
print("\nReversed Linked List")
list1.printList()
'''


#Double Linked List
'''
class Node:
    def __init__(self,value):
        self.previous = None
        self.data = value
        self.next= None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def length(self):
        temp = self.head
        count = 0
        while temp is not None:
            temp = temp.next
            count += 1
        return count

    def insertAtBeginning(self,value):
        new_node =Node(value)
        if self.isEmpty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insertAtEnd(self,value):
        new_node = Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            new_node.previous = temp

    def insertAtPostion(self,value,position):
        temp = self.head
        count = 1
        while temp is not None:
            if count == position-1:
                break
            count += 1
            temp = temp.next
        if position == 1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linked list. Cannot insert at {} position".formate(position,position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.previous = temp
            temp.next.previous = new_node
            temp.next = new_node
         

    def printLinkedList(self):
        temp = self.head
        while temp is not None:
            print(temp.data,sep = ",")
            temp = temp.next

    def deleteFromBeginning(self):
        if self.isEmpty():
            print("Linked list is Empty. Cannot delete elements")
        elif self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.previous = None

    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked list is Empty. Cannot delete elements")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.previous.next = None
            temp.previous = None

    def deleteFromPosition(self,position):
        if self.isEmpty():
            print("Linked list is Empty. Cannot delete elements")
        elif position==1:
            self.insertAtBeginning()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count==position:
                    break
                temp=temp.next
                count=+1
            if temp is None:
                print("There are less than {} elements in linked list. Cannot delete element.".format(position))
                return
            elif temp.next is None:
                self.deleteFromLast()
                return
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
            temp.next = None
            temp.previous = None
            
            
n = DoublyLinkedList()
print(n.isEmpty())
print("Insert at First")
n.insertAtBeginning(5)
n.printLinkedList()

#print("Insert at Beginning")
n.insertAtBeginning(15)
n.insertAtBeginning(45)
n.insertAtBeginning(65)

print("Insert at Position")
n.insertAtPostion(22,3)
n.printLinkedList()

print("Insert at End")
n.insertAtEnd(10)
n.insertAtEnd(20)
n.insertAtEnd(30)
n.insertAtEnd(40)
n.printLinkedList()

print("Delete at Beginning")
n.deleteFromBeginning()
n.printLinkedList()

print("Delete at the last")
n.deleteFromLast()
n.printLinkedList()

print("Delete By Position")
n.deleteFromPosition(3)
n.printLinkedList()

print("No.of Nodes:",n.length())

'''

#Postfix Expression

'''
class Evaluate:
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
    def isEmpty(self):
        return True if self.top == -1 else False
    def peek(self):
        return self.array[-1]
    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"
    def push(self,op):
        self.top += 1
        self.array.append(op)
    def evaluatePostfix(self,exp):
        for i in exp:
            if i.isdigit():
                self.push(i)
            else:
                val1 = self.pop()
                val2 = self.pop()
                self.push(str(eval(val2 + i + val1)))
        return int(self.pop())

if __name__ == '__main__':
    exp = "231*+9-"
    obj = Evaluate(len(exp))
    print("Postfix Evaluation : %d" %(obj.evaluatePostfix(exp)))

'''

