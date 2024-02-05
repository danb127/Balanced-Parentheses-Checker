from BalancedParentheses import BalancedParentheses
from BalancedParentheses import Stack
from BalancedParentheses import Queue

def main():
    checker = BalancedParentheses()
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.print_stack()  # Changed from print(stack)
    stack.pop()
    stack.print_stack()  # Changed from print(stack)
    
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    queue.print_queue()  # Changed from print(queue)
    queue.dequeue()
    queue.print_queue()  # Changed from print(queue)
    
    userString = None
    while userString != "quit":
        userString = input("Enter a string to check for balanced parenthesis: ")
        if checker.isBalanced(userString):
            print("Balanced!")
        else:
            print("Not balanced!")
    
if __name__ == "__main__":
    main()

