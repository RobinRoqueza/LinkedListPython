#Author: Robin Roqueza
#Cochlear Singly Linked List questions

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

# Methods

    # Function to add new node
    def add_node(self, new_element):
        new_node = Node(new_element)
        if self.head is None:
            self.head = new_node
            return
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = new_node

    # Remove node based on value
    def delete_node(self, key):
        temp_node = self.head
        if temp_node is not None:
            if temp_node.data == key:
                self.head = temp_node.next
                temp_node = None
                return
        while temp_node is not None:
            if temp_node.data == key:
                break
            prev = temp_node
            temp_node = temp_node.next
        if temp_node is None:
            return
        prev.next = temp_node.next

    # Function to print linked list
    def print_linked_list(self):
        temp_node = self.head
        if temp_node is not None:
            while temp_node is not None:
                print(temp_node.data, end=" ")
                temp_node = temp_node.next
            print()
        else:
            print("Linked List is empty.")

    # Function to return number of nodes in linked list
    def number_of_nodes(self):
        temp_node = self.head
        counter = 0
        if temp_node is not None:
            while temp_node is not None:
                counter += 1
                temp_node = temp_node.next
            return counter
        else:
            return counter

    # Function to reverse linked list
    def reverse_linked_list(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head = prev_node


# Main

MyList = LinkedList()

# Add 10 nodes at the end of the list.
for x in range (10):
    MyList.add_node(x)

# Linked list before reverse
print("Linked List contents: ")
MyList.print_linked_list()


# Linked list after reverse
print("Reverse Linked List contents: ")
MyList.reverse_linked_list()
MyList.print_linked_list()

