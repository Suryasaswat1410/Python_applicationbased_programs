#Single Linked List

'''
class Node:
    def __init__(self,data):
        self.item = data
        self.ref = None
class LinkedList:
    def __init__(self):
        self.start_node = None
    def traverse_list(self):
        if self.start_node is None:
            print("List has no Elements")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.ref

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.ref = self.start_node
        self.start_node = new_node

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n = n.ref
        n.ref = new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no Element to Delete")
            return
        self.start_node = self.start_node.ref

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no Elements to Delete")
            return
        n = self.start_node
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete_element_by_value(self,x):
        if self.start_node is None:
            print("The list has no Element to Delete")
            return
        if self.start_node == x:
            self.start_node = self.start_node.ref
            return
        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x :
                break
            n = n.ref

        if n.ref is None:
            print("Item not found int the List")
        else:
            n.ref = n.ref.ref

    def search_item(self,x):
        if self.start_node is None:
            print("List has No Elements")
            return
        n = self.start_node
        while n is not None:
            if n.item == x:
                print("Item Found")
                return True
            n = n.ref
        print("Item not found")
        return False

    def get_count(self):
        if self.start_node is None:
            return 0;
        n = self.start_node
        count = 0;
        while n is not None:
            count = count+1
            n = n.ref
        return count

    def insert_at_index(self,index,data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        i = 1
        n = self.start_node
        while i < index-1 and n is not None:
            n = n.ref
            i = i+1
        if n is None:
            print("Index out of Bound")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node


new_linked_list = LinkedList()

new_linked_list.insert_at_end(5)
new_linked_list.insert_at_end(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
new_linked_list.insert_at_end(25)
new_linked_list.insert_at_end(30)
new_linked_list.insert_at_end(35)
new_linked_list.insert_at_end(40)
new_linked_list.insert_at_end(45)
print("The Inserted Elements are :")
new_linked_list.traverse_list()

new_linked_list.delete_at_start()
print("After Deletion at the Beginning :")
new_linked_list.traverse_list()

new_linked_list.delete_at_end()
print("After Deletion at the Ending :")
new_linked_list.traverse_list()

new_linked_list.delete_element_by_value(40)
print("After deleting 40 :")
new_linked_list.traverse_list()

new_linked_list.search_item(5)
new_linked_list.search_item(25)
print("The Number of Nodes:",new_linked_list.get_count())
new_linked_list.insert_at_index(3,8)
new_linked_list.traverse_list()


'''
