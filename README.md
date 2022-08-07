# Data Structures and Algorithms Practice/Leetcode Problems

# Note: as of now, this readme is a work in progress! I haven't added most solved problems (files in this repo) to the list yet, but I'm working on it :)

A collection of problems that I solved to learn and practice data structures and algorithms. Most problems here come from [Leetcode](http://leetcode.com), the names and numbers are provided in some cases. For every problem, I do my best to maximize efficiency (thinking in terms of time/space complexity) and provide alternative implementations that offer interesting trade-offs. For this reason, a lot of the files contain several functions that either do the same thing in different ways, or solve variations of the same problem. The solutions are commented and explained to the best of my ability. I try and add notes and provide main takeaways from solving each problem.

Currently I'm using Python3 for DSA practice. I believe Python is great for writing readable, clear solutions that allow one to focus on the algorithmic nature of a problem rather than implementation details. However, as I prefer C/C++ for my other projects, I am looking forward to adding more C/C++ implementations. There are a lot of problems where the differences between Python and C/C++ code might be non-trivial, and solving those in C/C++ would be an interesting and useful experience for me.

## Trees
1. [Check if A Binary Tree Is Balanced](https://github.com/brasssmonkey/dsa/blob/main/BalancedBinTree.py): several different approaches, learned a lot with this one!
2. [Invert Binary Tree](https://github.com/brasssmonkey/dsa/blob/main/InvertBtree.py): an iterative algorithm to invert a binary tree.
3. [Find Lowest Common Ancestor of Two Nodes in a Binary Search Tree](https://github.com/brasssmonkey/dsa/blob/main/LowestCommonAncestor.py)
4. [Maximum Depth of a Binary Tree](https://github.com/brasssmonkey/dsa/blob/main/MaxDepth.py)

## Binary Search
1. [Koko Eating Bananas](https://github.com/brasssmonkey/dsa/blob/main/Koko.py): very neat problem! My take on an efficient solution utilizes binary search.
2. [Basic Binary Search 1](https://github.com/brasssmonkey/dsa/blob/main/binarySearchLC.py), [Basic Binary Search 2](https://github.com/brasssmonkey/dsa/blob/main/binarySearch.py)
3. [Find The Duplicate Number in an Array Using Binary Search](https://github.com/brasssmonkey/dsa/blob/main/findDupbinSearch.py)

## Bitwise Operations
1. [Sum Two Integers Without Using + or -](https://github.com/brasssmonkey/dsa/blob/main/binarySum.py)
2. [Find the Duplicate Number in an Array Using Bit Manipulation](https://github.com/brasssmonkey/dsa/blob/main/binaryfindDup.py): very fun and elegant solution.
3. [Count Set Bits in a Number](https://github.com/brasssmonkey/dsa/blob/main/countBits.py): several alternative solutions.
4. [Find The Sum of Two Numbers Using Bitwise Operations](https://github.com/brasssmonkey/dsa/blob/main/getSum.py)

## Implementations of Data Structures
1. [(Random) Singly-Linked List](https://github.com/brasssmonkey/dsa/blob/main/LL.py): an implementation of a singly-linked list class that helped me test and debug numerous linked list problems. This implementation supports an extra "random" pointer added to each node (I added this to help test the problem [Random Linked List]()). It is most definitely a work in progress: moving forward, I am planning to add sentinels, array representation of a link list (to simplify debugging), and more methods and features. For now, treat this as a bare-bones class for testing/debugging.

## Linked Lists
1. [Reverse Singly Linked List](https://github.com/brasssmonkey/dsa/blob/main/LLreverse_train.py)
2. [Copy Random List](https://github.com/brasssmonkey/dsa/blob/main/copyRandomList.py): copy a linked list where an extra random pointer is attached to each node.
3. 

## Dynamic Programming
1. [Find Max Subarray](https://github.com/brasssmonkey/dsa/blob/main/MaxSub.py): within an array, find a contiguous subarray that sums up to maximum value.
2. 

## Arrays
1. [Is This String a Valid Palindrome?](https://github.com/brasssmonkey/dsa/blob/main/ValPal.py)
2. [Find The Sum of All Elements in an Array](https://github.com/brasssmonkey/dsa/blob/main/binaryListsum.py): this solution uses binary recursion to optimize space usage.
3. [Find The Duplicate Number in an Array](https://github.com/brasssmonkey/dsa/blob/main/findDup.py): a LOT of possibilities with this problem. Multiple alternative solutions are provided.

## Hashmaps
1. 

## Stacks
1. [Evaluate Reverse Polish Notation](https://github.com/brasssmonkey/dsa/blob/main/evaluateRPN.py)

## Miscellaneous
1. [English Ruler](https://github.com/brasssmonkey/dsa/blob/main/EnglishRuler.py): elementary algorithm that prints out an english ruler in your terminal.
2. [Find The Duplicate Number in an Array Using Floyd's Cycle-Finding Algorithm](https://github.com/brasssmonkey/dsa/blob/main/floydsFindDup.py): a very interesting alternative solution to the findDuplicate problem.
3. [Fibonacci Numbers](https://github.com/brasssmonkey/dsa/blob/main/goodFib.py): an efficient algorithm to generate Fibonacci numbers.


## In Progress
