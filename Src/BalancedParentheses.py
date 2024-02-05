# Daniel Baker
# CS 3310 Data and File Structures
# James Rhodes
# 09 / 15 / 23

# Get data and the reference to next Node
class Node:
    # Initialize Node object
    def __init__(self, data):
        self.data = data # Initialize node data, store the actual data
        self.next = None # Initialize the next pointer to None, signifying end of the list initially


# LinkedList to manage Nodes, backbone for Stack and Queue class
class LinkedList:
    # Initializing an empty list with a head pointing to None
    def __init__(self):
        self.head = None # Initializing head node to None, intializing the empty list

    # Method to add new node to end of the list, essential to adding elements to are stack or queue
    def append(self, data):
        new_node = Node(data) # Creating new node with data
        if self.head is None: # If list is empty, setting new node as the head of the list
            self.head = new_node
            return
        last_node = self.head # Starting traversal from head
        while last_node.next: # Continuing as long as the next node exists
            last_node = last_node.next # Moving to next node in the list
        last_node.next = new_node # Adding new node to the end of the list

    # Method to remove and return the data from the head node
    def pop(self):
        if self.head is None: # If list is empty, returning None
            return None
        temp = self.head # Storing the current head temporarily
        self.head = self.head.next # Setting the next node as the new head
        return temp.data # Returning the data from the original head node
    
    # Method to check if the list is empty, returns True if empty, False otherwise
    def is_empty(self):
        return self.head is None
    
    # Method to print the list
    def print_list(self):
        if self.head is None:
            print("List is empty")
            return
        current_node = self.head
        while current_node:
            print(current_node.data, end = " ")
            current_node = current_node.next
        print()
        
        
    
# Stack class based on LinkedList class, handles LIFO operation
class Stack:
    # Initializing empty LinkedList to use as the underlying data structure
    def __init__(self):
        self.list = LinkedList()
    
    # Method for pushing data onto the stack, we use append method from LinkedList class to add an element to the end of the list
    def push(self, data):
        self.list.append(data)
        
    # Method for popping data off the stack, we use pop method from LinkedList class to remove and return the data from the head node
    def pop(self):
        return self.list.pop()
    
    # Method for checking if the stack is empty, we check if the head node is None
    def is_empty(self):
        return self.list.is_empty()
    
    # Method for printing the stack, we use the print_list method from LinkedList class
    def print_stack(self):
        self.list.print_list()
        

# Queue class based on LinkedList class, handles FIFO operation
class Queue:
    # Initializing empty LinkedList to use as the underlying data structure
    def __init__(self):
        self.incoming = LinkedList()
        self.outgoing = LinkedList()
    
    # Method for pushing data onto the queue, we use append method from LinkedList class to add an element to the end of the list
    def enqueue(self, data):
        self.incoming.append(data)
    
    # Method for popping data off the queue, we use pop method from LinkedList class to remove and return the data from the head node
    def dequeue(self):
        if self.outgoing.is_empty():
            while not self.incoming.is_empty():
                self.outgoing.append(self.incoming.pop())
        return self.outgoing.pop()
    
    # Method for checking if the queue is empty, we check if the head node is None
    def is_empty(self):
        return self.incoming.is_empty() and self.outgoing.is_empty()
    
    # Method for printing the queue, we use the print_list method from LinkedList class
    def print_queue(self):
        self.incoming.print_list()
        self.outgoing.print_list()
    
# Function to check if the parentheses are balanced
class BalancedParentheses:
    def __init__(self):
        self.stack = Stack()
        self.queue = Queue()
    
    def check_parentheses(self, string):
        for char in string:
            if char == "(":
                self.stack.push(char)
            elif char == ")":
                if self.stack.is_empty():
                    return False
                self.stack.pop()
        return self.stack.is_empty()
    
    def check_brackets(self, string):
        for char in string:
            if char == "[":
                self.stack.push(char)
            elif char == "]":
                if self.stack.is_empty():
                    return False
                self.stack.pop()
        return self.stack.is_empty()
    
    def check_braces(self, string):
        for char in string:
            if char == "{":
                self.stack.push(char)
            elif char == "}":
                if self.stack.is_empty():
                    return False
                self.stack.pop()
        return self.stack.is_empty()
    
    def check_all(self, string):
        return self.check_parentheses(string) and self.check_brackets(string) and self.check_braces(string)
    
    def isBalanced(self, string):
        return self.check_all(string)  


    
        
    