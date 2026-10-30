# main.py
from array_stack import ArrayStack
from linked_stack import LinkedStack
from circular_array_queue import CircularArrayQueue
from linked_queue import LinkedQueue

def menu():
    print("\n===== STACK & QUEUE LAB MENU =====")
    print("1. Test ArrayStack")
    print("2. Test LinkedStack")
    print("3. Test CircularArrayQueue")
    print("4. Test LinkedQueue")
    print("5. Exit")
    return input("Choose option: ")


def test_array_stack():
    cap = int(input("Enter ArrayStack capacity: "))
    s = ArrayStack(cap)
    while True:
        print("\n--- ArrayStack Menu ---")
        print("a push | b pop | c peek | d print | e back")
        opt = input("Choose: ").lower()
        try:
            if opt == 'a':
                val = input("Enter value: ")
                s.push(val)
                print("State:", s)
            elif opt == 'b':
                print("Popped:", s.pop())
                print("State:", s)
            elif opt == 'c':
                print("Peek:", s.peek())
            elif opt == 'd':
                print("State:", s)
            elif opt == 'e':
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error:", e)


def test_linked_stack():
    s = LinkedStack()
    while True:
        print("\n--- LinkedStack Menu ---")
        print("a push | b pop | c peek | d print | e back")
        opt = input("Choose: ").lower()
        try:
            if opt == 'a':
                val = input("Enter value: ")
                s.push(val)
                print("State:", s)
            elif opt == 'b':
                print("Popped:", s.pop())
                print("State:", s)
            elif opt == 'c':
                print("Peek:", s.peek())
            elif opt == 'd':
                print("State:", s)
            elif opt == 'e':
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error:", e)


def test_circular_queue():
    cap = int(input("Enter CircularArrayQueue capacity: "))
    q = CircularArrayQueue(cap)
    while True:
        print("\n--- CircularArrayQueue Menu ---")
        print("a enqueue | b dequeue | c peek_front | d print | e back")
        opt = input("Choose: ").lower()
        try:
            if opt == 'a':
                val = input("Enter value: ")
                q.enqueue(val)
                print("State:", q)
            elif opt == 'b':
                print("Dequeued:", q.dequeue())
                print("State:", q)
            elif opt == 'c':
                print("Peek front:", q.peek_front())
            elif opt == 'd':
                print("State:", q)
            elif opt == 'e':
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error:", e)


def test_linked_queue():
    q = LinkedQueue()
    while True:
        print("\n--- LinkedQueue Menu ---")
        print("a enqueue | b dequeue | c peek_front | d print | e back")
        opt = input("Choose: ").lower()
        try:
            if opt == 'a':
                val = input("Enter value: ")
                q.enqueue(val)
                print("State:", q)
            elif opt == 'b':
                print("Dequeued:", q.dequeue())
                print("State:", q)
            elif opt == 'c':
                print("Peek front:", q.peek_front())
            elif opt == 'd':
                print("State:", q)
            elif opt == 'e':
                break
            else:
                print("Invalid choice")
        except Exception as e:
            print("Error:", e)


def main():
    while True:
        choice = menu()
        if choice == "1":
            test_array_stack()
        elif choice == "2":
            test_linked_stack()
        elif choice == "3":
            test_circular_queue()
        elif choice == "4":
            test_linked_queue()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid main menu choice")


if __name__ == "__main__":
    main()
