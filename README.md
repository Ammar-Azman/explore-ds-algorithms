# Why bother to learn?
- To build algorithmic mindset.
- To build a problem solving skills in an algorithmics point of view. 
- To explore every possibility in algorithms.

# Big-O notation
- Pronounce as "big-ouh"
- Mathematical representation to calculate the speed of execution with terms:
    - Time complexity
    - Space complexity
- Algorithm Complexity Analysis
    - Analysis to conclude the complexity of the algorithm

# Data Structure
## 1. Linked List
- Characteristics:
    - List that is linked by pointer (memory)
    - Manipulating the memory by establish a link from one node to another
- Another variants: Double Linked List
- Implementation with Python:
    - By utilizing the characteristic of OOP `Class` where object is allocated to the memory to save the values. 
    - By manipulating the memory, we an create a pointer towards any nodes, which then create a Linked List.

## 2. Hash Map/Table
- Implementing `Dict` in Python 
- Using a function to hash the value of the key towards particular memory.
- Problem to solve:
    - The memory allocation when using list by hashing the value and 
    can be directly accessed by it, instead of allocate the value with memory by indexing. 
- Problem with Hashing
    - Collision
        - Definition: Collision happened when the hash function returned the same index on differet
        key given, cause the data to share the same index. 
        - Solutions:
            1. Chaining
            2. Linear Probing

## 3. Stack
- Characteristics:
    - Data stored in stack; putting book in a box.
    - LIFO - Last In First Out
- Search element by value - `O(n)`
- Cases:
    - Scoping other functions within other
- Problem to solve:
    - Python using dynamic array, where the size of the memory area in the list
    can be increased if the amount of element is exceed the size. 
    - Python will find available memory area that has size that exceed the current size, 
    and copy the information on it. 
    - The problem if we have millions of data, as of the process of handling the huge
    information, where Python need to allocate memory and copy all of it which is costly. 
    - Hence, Stack is not recommended. 
- Solution: 
    - Using `collection.deque`

## 4.Queue
- Characteristics:
    - Data stored in queue; like queueing to buy ticket.s
    - FIFO - First in First Out
- Allows system to have loose coupling
- Implementation with Python:
    - Can use list or `collection.deque`
    - For list, it would have an issue due to dynamic array. That's why it used `collection.deque` to solve the problem and create the architecture that mimic
    the queue algorithm. 

## 5.Tree
- Non-hierarchical data
- Terms
    - Root node - root of the tree (level 0)
    - Node - intermediate/middle tree - have children node (parents to children, children to ancestor) (level 1)
    - Lead node - does'nt have childer node (children to parents) (level 2)
- Code-wise
    - Using instance attribute to add properties such - `children` and `parents` can create
    a tree in ds-algo. 

## 6. Binary Tree
- Characteristics:
    - Child only has maximum 2 nodes (binary tree)
    - Left child node **should** less than the parents node, vice versa on the right node

## 7. Graph 
- Multiple path between nodes (compared to Tree)
- variant of Tree
- Weighted path - shortest path 
- Implementation
    - maps - finding shortest path
    - internet 
    - facebook - connecting people

# Algorithms
## 1. Recursion
- Characteristics:
    - A function that call itself within the function
- Components:
    1. Base case - what function do
    2. Exit case - exit once complete
    3. Recurse itself - call itself
- How it works in Python:
    - Recursive functions will call itself, from the first line until the 
    the its function name, until it exit.
    - Note that during recursive time, the value will be stored within the memory. The value
    then will be used after the recursive ended on the next line (which is the function return value).
    - After recursive ended, it will execute the next line and doing **stack unwinding** (featching the value that it has saved within the memory), hence return value of the function.
    - If the function is called 2 times within itself, it might be the 2nd call would call
    the first one and execute the 1st (recursive) function too. 
- It might be not necessary to understand how Python unwind the stack, but we just need to ensure the recursion components is established within the function. (imo)

## Searching Algorithms
### 2. Binary Search Tree
- Pre-requisite: Recursion
- Characteristics:
    - Using Binary Tree data structure
- Complexity:
    - Search complexity: `O(log n)`
    - Insert complexity: `O(log n)`
- Problem to solve
    - Speed up searching algo
        - reducing search space by half (binary) every tim
    - implementing `set` in Python
- Pseudocode
    - Insert child
        - Left hand side child node must have less value than its parent, while the right hand
        vise versa.
        - No child means `null` child

    - Delete child (all deletion should preserved the binary tree principal - 1- left should less than right)
        1. Delete node with no child
        2. Delete node with 1 child
        3. Delete node with 2 childs
            - Method 1
                - look on right subtree
                - find min value from right subtree
                - copy value node to the node-to-delete
                - remove the node-to-delete 
            - Method 2
                - Find maximum from the left subtree of the node-to-delete
                - copy the value to the node-to-delete
                - delete the maximum value
- Searching Algoritms:
    1. Breadth First Search (BFS)
    2. Depth First Search (DFS) (traversal)
        - In order traversal
            - left subtree --> root --> right subtree 
        - Pre order traversal
            - root --> left subtree --> right subtree 
        - Post order traversal
            - left subtree --> right subtree --> root
- Complete binary tree
    - all level except possibly the last are completely filled and all nodes are left as possible

### 3. Binary search
- Linear search
    - Search one by one - O(n)
    - if n = 100k hence, searching is one by one (iteration)
    - Less effective for huge inputs 
- Binary search
    - Searching by iteratively divide the inputs by 2
    - **Required sorted list**
    - Mathematically;
        - 1st iteration = n/2
        - 2nd iteration = n/2^2
        - 3rd iteraion = n/2^3
        - Hence
            - iteration = n/n^k
                - K = log n 
                    - Hence -> O(log n)

### 4. Breadth First search (BFS)
- can be apply on Binary Tree and Graph

### 5. Depth First search (DFS)
- can be apply on Binary Tree and Graph

    

## Sorting Algorithms
### 1. Bubble Sort
- Like bubble, it will move from bottom to the upper 
- In bubble sort, max value will move and until it located to the top
- Algorithm use: `temp` variable
- New insight:
    - It is possible to improve algorithms performance by adding logics, 
    improve the iterations, and etc etc.

### 2. Quick Sort
- Sorting by batch/slice (?)
- Divide and Conquer Problem
- Putting the pivot value to correct part - called partitioning
- 2 types partitioning schemes:
    1. Hoare partiton (personal notes: I found 2 version of Hoare algorithms and not sure which one is correct. v1: from Wikipedia, v2: from visual on youtube. The following algorithm is coming from CodeBasics channel which has been taken from Wikipedia)
        - Components:
            - *pivot pointer* - i
            - *start pointer* - j
            - *end pointer*
        - Algorithm:
            1. Set pivot as the most left value (index [0])
            2. Set the *start pointer* on the right side of *pivot*. 
            3. Set the *end pointer** on the end of the list. 
            4. If start < end
                -  Comparing pivot with start 
                    - *start pointer* check from left to right
                    - check if value less than pivot, if yes continue, elif not, stop. (scanning the big element)
                -  Comparing pivot with end
                    - *end pointer* check from right to left
                    - check if value is bigger than pivot, if yes continue, elif not, stop. (inverse rule) (scanning the small element)
                6. Swap the *start pointer* value and *end pointer* value. 
                7. Iterate step 4 and 5, until *end pointer* intercept the *start pointer*. 
            8. Else
                - Swap the *end pointer* value with the *pivot pointer* value. 
            9. Now, there is left and right partition. The pivot value is changed (new), but the index is still the same which is 0, for both left and right partition. 
            10. Iterate step 4 - 9  for the left partition and right partition, which will partition more, 
            more, more until all is sorted.
        - Notes:
            - Basically the pivot can be started any position in the list, but to make is simple, 
            start it from the index 0. 
    2. Lomuto partition
        - Components:
            - *p-index* - partition index
            - *pivot pointer*
            - *i-counter* - same as *p-index*
        - Algorithms:
            1. Set pivot as the most right value. (index [-1])
            2. Set the *p-index* as the most left value. 
            3. Move the *p-index* until it found value that *bigger than* pivot value, then stop.
            4. Then, *i-counter* will start on where the *p-index* has stop (for initial). 
            5. *i-counter* then move until it found value that **less* than pivot, then it will stop. (inverse rule compare to step 3)
            6. Now, (as both stop) *i-counter* value will swap with the value of *p-index* value.
            7.  Iterate step 3, 5 and 6, until the end of the list. 
- Complexity:
    - Average time complexity : `O(n log n)`
    - Worst time complexity: `O(n**2)` 
        - if link already sorted (WHY?)

### 3. Insertion Sort
- Using pointer
- Complexity performance
    - Worst case: O(n**2) -- all not sorted and if list too big
    - Best case O(n) -- even if it sorted, comparing still done
- Pseudocode:
    1. For element in arr, set anchor, with index `i`. 
    2. Set another index, `j`, that is position 1 step behind `i`.
    3. For (while) element in arr, if element `j` is bigger than anchor, the element next to `j` (`j + 1`) value will become the `j` index element value. (insertion happen!)
    4. `j` index will negatively increment (to ensure it is behind `i`)
    5. If element `j` is less than anchor, break, the element `j + 1` value will become anchor value. 
- Disadvantage:
    1. Towards the end of insertion, it took too much **Comparison** and
    **Swaps** and reduce the efficiency.
    2. When too much bigger numbers on the left side.
- Solution: Shell sort


### 4. Merge sort
- Using Divide and Conquer
- Psuedocode:
    1. We need to create a sorted array using divide and conquer technique
        - divide until it can't
        - compare, small is left, big is right
        - swap
        - combine - until produce 2 sorted array
    1. Use the sorted array from step 1. Say arr A and arr B.
    2. Set an empty array. 
    3. on arr A, compare first element to the element in arr B; iteratively on arr B. 
    4. If arr B element is less than the element arr A, insert the arr B element in the empty array. arr A is stay on the element, arr B is move/iterate.
    5. If arr B element is bigger than the element arr A, insert the arr A element in the empty array. arr B is stay, arr A is move/iterate.
    6. Iterate step 3 to 5. 

### 5. Timsort
- Merge sort + Insertion sort

### 6. Shell sort
- Optimization of *insertion sort*
- Creating sub array (gap)
- Due to the weakness of insertion sort whenever the arr has bigger value on the left side and smaller value on the right side, shell sort will use gap in order to partially sorting the array in the form of more bigger value on the right and smaller value on the left side; even though the array is not completely sorted.
- Gap it reduced by iteration, gap = 1 is insertion sort.
- Psuedocode:
    **Note**
    - The original psuedocode is similar to insertion sort, with gap

    1. Set gap (size // 2)
    2. For index `i` in range (gap and size), first element `i` will become ancor, set index `j` equal to `i`. 
    3. (while) index `j` is b equal to bigger than gap, and element on `j - gap` bigger than anchor, 
    element `j` is (copy) element `j - gap`
    4. j negatively increment with gap. 
    5. Break while, element `j` value copy anchor value. 
    6. Break nested for loop, gap negatively increment with division 2. 

### 7. Selection Sort
- Pseudocode:
    - **Select** an element
    - Check all the value on the right side
        - If found value less than the selected element, 
            - swap
            - move
    - Iterate. 
- Complexity: `O log(n^2)` - due to 2 loop 

### 8. Heap Sort
...
