# program5.py
# Stack operations: PUSH, POP, PEEK

stack = []  # using Python list as stack

def push():
    element = input("Enter element to PUSH: ")
    stack.append(element)
    print(f"{element} pushed to stack")

def pop_element():
    if not stack:
        print("Stack is empty! Cannot POP.")
    else:
        print(f"Element popped: {stack.pop()}")

def peek():
    if not stack:
        print("Stack is empty! No element to PEEK.")
    else:
        print(f"Top element: {stack[-1]}")

def display():
    print("Current Stack:", stack)

while True:
    print("\n--- STACK OPERATIONS ---")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. DISPLAY STACK")
    print("5. EXIT")

    choice = input("Enter your choice: ")

    if choice == '1':
        push()
    elif choice == '2':
        pop_element()
    elif choice == '3':
        peek()
    elif choice == '4':
        display()
    elif choice == '5':
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
