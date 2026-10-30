# Stacks and Queues Laboratory Activity
**Title:** Stacks and Queues: Array vs Linked List

## 📌 Project Overview
This laboratory implements four fundamental data structures following the specifications from Module 5:
1. **ArrayStack** – Fixed‑size array‑based stack
2. **LinkedStack** – Linked‑list‑based stack operating at the head
3. **CircularArrayQueue** – Circular array‑based queue with wrap‑around
4. **LinkedQueue** – Linked‑list‑based queue using front + rear pointers

The program includes a menu‑driven driver that lets users perform operations and prints the state after each action. It properly raises exceptions for overflow and underflow.

## 📂 Files Included
- `array_stack.py` – ArrayStack implementation
- `linked_stack.py` – LinkedStack implementation
- `circular_array_queue.py` – CircularArrayQueue implementation
- `linked_queue.py` – LinkedQueue implementation
- `menu_driver.py` – Main menu program
- `analysis.md` – Written analysis for the lab

## 💻 Requirements
- Python 3.x installed
- No extra libraries needed

## ▶️ How to Run
1. Save all files inside one folder.
2. Open VS Code / Terminal and navigate to that folder.
3. Run the main driver:
```bash
python menu_driver.py

3. Choose from the menu:
 
- 1 = Test ArrayStack
​
- 2 = Test LinkedStack
​
- 3 = Test CircularArrayQueue
​
- 4 = Test LinkedQueue
​
- 5 = Exit
 
4. Inside each sub‑menu:
 
- Stacks: Push, Pop, Peek, Print
​
- Queues: Enqueue, Dequeue, Peek Front, Print
​
- The program shows the current state after each operation
​
- Overflow and underflow errors are displayed
 
Features
 
- ArrayStack uses top index starting at -1
​
- LinkedStack operates only at the head for O(1) efficiency
​
- CircularArrayQueue uses modulo arithmetic for wrap‑around and a size counter
​
- LinkedQueue maintains both front and rear pointers
​
- Exception handling for overflow and underflow
​
- Menu‑driven interface
​
- Prints state after each operation
 
Sample Runs
 
- ArrayStack: Enter capacity first; pushing beyond capacity causes overflow
​
- LinkedStack: No fixed capacity; popping empty stack causes underflow
​
- CircularArrayQueue: Enter capacity first; enqueuing past the end demonstrates wrap‑around
​
- LinkedQueue: No fixed capacity; dequeuing empty queue causes underflow
 
Author
 
[NAVAROZA, RYAN STANLY A. ]
[BSIT-2D]
[Activity-5_BSIT-2D_NAVAROZA_RYAN_STANLY_A.]
