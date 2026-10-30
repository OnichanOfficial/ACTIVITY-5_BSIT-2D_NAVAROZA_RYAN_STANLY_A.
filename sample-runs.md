# Sample Runs Documentation

## 1. ArrayStack Sample Run
### Normal Operation

===== STACK & QUEUE LAB MENU =====
 
1. Test ArrayStack
​
2. Test LinkedStack
​
3. Test CircularArrayQueue
​
4. Test LinkedQueue
​
5. Exit
Choose option: 1
 
Enter ArrayStack capacity: 3
 
--- ArrayStack Menu ---
a push | b pop | c peek | d print | e back
Choose: a
Enter value: A
State: ['A']
 
Choose: a
Enter value: B
State: ['A', 'B']
 
Choose: a
Enter value: C
State: ['A', 'B', 'C']
 
Choose: b
Popped: C
State: ['A', 'B']
 
Choose: c
Peek: B
 
Choose: d
State: ['A', 'B']
 
Choose: e

### Overflow
Choose: a
Enter value: D
Error: Stack overflow: cannot push to full ArrayStack


### Underflow
Choose: b
Popped: B
State: ['A']
 
Choose: b
Popped: A
State: []
 
Choose: b
Error: Stack underflow: cannot pop empty ArrayStack


## 2. LinkedStack Sample Run
### Normal Operation
===== STACK & QUEUE LAB MENU =====
Choose option: 2
 
--- LinkedStack Menu ---
a push | b pop | c peek | d print | e back
Choose: a
Enter value: X
State: ['X']
 
Choose: a
Enter value: Y
State: ['Y', 'X']
 
Choose: b
Popped: Y
State: ['X']
 
Choose: c
Peek: X
 
Choose: d
State: ['X']
 
Choose: e


### Underflow
Choose: b
Popped: X
State: []
 
Choose: b
Error: Stack underflow: cannot pop empty LinkedStack


## 3. CircularArrayQueue Sample Run
### Normal Operation + Wrap‑Around
===== STACK & QUEUE LAB MENU =====
Choose option: 3
 
Enter CircularArrayQueue capacity: 3
 
--- CircularArrayQueue Menu ---
a enqueue | b dequeue | c peek_front | d print | e back
Choose: a
Enter value: 1
State: ['1']
 
Choose: a
Enter value: 2
State: ['1', '2']
 
Choose: a
Enter value: 3
State: ['1', '2', '3']
 
Choose: b
Dequeued: 1
State: ['2', '3']
 
Choose: a
Enter value: 4
State: ['2', '3', '4']
 
Choose: b
Dequeued: 2
State: ['3', '4']
 
Choose: c
Peek front: 3
 
Choose: d
State: ['3', '4']
 
Choose: e


### Overflow
Choose: a
Enter value: 5
State: ['3', '4', '5']
 
Choose: a
Enter value: 6
Error: Queue overflow: cannot enqueue full CircularArrayQueue


### Underflow
Choose: b
Dequeued: 3
State: ['4', '5']
 
Choose: b
Dequeued: 4
State: ['5']
 
Choose: b
Dequeued: 5
State: []
 
Choose: b
Error: Queue underflow: cannot dequeue empty CircularArrayQueue


## 4. LinkedQueue Sample Run
### Normal Operation
===== STACK & QUEUE LAB MENU =====
Choose option: 4
 
--- LinkedQueue Menu ---
a enqueue | b dequeue | c peek_front | d print | e back
Choose: a
Enter value: P
State: ['P']
 
Choose: a
Enter value: Q
State: ['P', 'Q']
 
Choose: a
Enter value: R
State: ['P', 'Q', 'R']
 
Choose: b
Dequeued: P
State: ['Q', 'R']
 
Choose: c
Peek front: Q
 
Choose: d
State: ['Q', 'R']
 
Choose: e


### Underflow
Choose: b
Dequeued: Q
State: ['R']
 
Choose: b
Dequeued: R
State: []
 
Choose: b
Error: Queue underflow: cannot dequeue empty LinkedQueue


## Notes
- Linked structures do not produce overflow since they use dynamic memory.
- Take actual screenshots of running the program for final submission.
