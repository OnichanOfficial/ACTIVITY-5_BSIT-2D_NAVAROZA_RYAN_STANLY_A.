# Analysis

## Analysis Question
Briefly explain why the linked‑list stack pushes at the head instead of the tail and why the array queue must be circular.

## Written Analysis
A linked‑list stack pushes and pops at the head because the head can be accessed in constant O(1) time. If the operations were done at the tail of a singly‑linked list, the program would need to traverse the entire list first, resulting in slower O(n) time. Therefore, the head is used as the top of the linked‑list stack for better efficiency.

An array‑based queue must be circular because repeated dequeue operations leave unused empty slots at the front of the array. Without circular wrapping, these slots are wasted or the program must shift all elements left, which takes O(n) time. Using modulo arithmetic allows the front and rear indices to wrap back to the start of the array, reusing empty slots while keeping enqueue and dequeue operations O(1). A size counter is also used so the program can correctly distinguish between an empty queue and a full queue instead of relying only on front being equal to rear.

## Additional Discussion
The ArrayStack uses a top index starting at −1 to show that it is empty. The CircularArrayQueue uses both a front index and a size counter to manage wrap‑around properly. The LinkedQueue keeps both front and rear pointers so enqueue happens at the rear and dequeue happens at the front in constant time. These design choices follow the LIFO rule for stacks and the FIFO rule for queues while maintaining efficient performance.
