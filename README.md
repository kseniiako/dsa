# Data Structures and Algorithms Practice/Leetcode Problems

## Note: As of now, this readme is a work in progress! I haven't added many solved problems (files in this repo) to the list yet, but I'm working on it :)

A collection of problems that I solved to learn and practice data structures and algorithms. Most problems here come from [Leetcode](http://leetcode.com), the names and numbers are provided in some cases. For every problem, I do my best to maximize efficiency (thinking in terms of time/space complexity) and provide alternative implementations that offer interesting trade-offs. For this reason, a lot of the files contain several functions that either do the same thing in different ways, or solve variations of the same problem. The solutions are commented and explained to the best of my ability. I try and add notes and provide main takeaways from solving each problem.

Currently I'm using Python3 for DSA practice. I believe Python is great for writing readable, clear solutions that allow one to focus on the algorithmic nature of a problem rather than implementation details. However, as I prefer C/C++ for my other projects, I am looking forward to adding more C/C++ implementations. There are a lot of problems where the differences between Python and C/C++ code might be non-trivial, and solving those in C/C++ would be an interesting and useful experience for me.

## [Array to Tree and Tree To Array Converter](https://github.com/brasssmonkey/dsa/blob/main/arrayBasedTree.py)
This is a pair of functions that allow conversion between standard (root-based) binary tree representation and a representation of a binary tree as an array of the values of its nodes, where you can determine a node's parents and children from its position in the array. A very helpful tool for testing and debugging functions that work with binary tree-based structures!

## Trees
1. [Check if A Binary Tree Is Balanced](https://github.com/brasssmonkey/dsa/blob/main/BalancedBinTree.py): several different approaches, learned a lot with this one!
2. [Invert Binary Tree](https://github.com/brasssmonkey/dsa/blob/main/InvertBtree.py): an iterative algorithm to invert a binary tree.
3. [Find Lowest Common Ancestor of Two Nodes in a Binary Search Tree](https://github.com/brasssmonkey/dsa/blob/main/LowestCommonAncestor.py)
4. [Maximum Depth of a Binary Tree](https://github.com/brasssmonkey/dsa/blob/main/MaxDepth.py)
5. [Right Side View of a Binary Tree](https://github.com/brasssmonkey/dsa/blob/main/treeRightSideView.py): very cool question! I wrote three solutions; they all depend on BFS for level order traversal, but employ different mechanisms to keep track of what level we are currently on.
6. [Level Order Traversal of a Binary Tree](https://github.com/brasssmonkey/dsa/blob/main/levelOrderTraversal.py): predictably, a BFS-based algorithm.
7. [Count Good Nodes in a Binary Tree](https://github.com/brasssmonkey/dsa/blob/main/countGoodNodes.py): fun algorithm that uses DFS.

## Binary Search
1. [Koko Eating Bananas](https://github.com/brasssmonkey/dsa/blob/main/Koko.py): very neat problem! My take on an efficient solution utilizes binary search.
2. [Basic Binary Search 1](https://github.com/brasssmonkey/dsa/blob/main/binarySearchLC.py), [Basic Binary Search 2](https://github.com/brasssmonkey/dsa/blob/main/binarySearch.py)
3. [Find The Duplicate Number in an Array Using Binary Search](https://github.com/brasssmonkey/dsa/blob/main/findDupbinSearch.py)
4. [Search Rotated Sorted Array](https://github.com/brasssmonkey/dsa/blob/main/searchRotatedArray.py): a very fun quesion that builds up on binary search concepts with a small twist.
5. [Find Minimum in Rotated Sorted Array](https://github.com/brasssmonkey/dsa/blob/main/minInRotatedArray.py): an easier version of the previous problem. The file contains two slightly different solutions, the second one is pretty clever: it pre-saves potential output values to potentially speed up the search (narrow down future iterations).

## Bitwise Operations
1. [Sum Two Integers Without Using + or -](https://github.com/brasssmonkey/dsa/blob/main/binarySum.py)
2. [Find the Duplicate Number in an Array Using Bit Manipulation](https://github.com/brasssmonkey/dsa/blob/main/binaryfindDup.py): very fun and elegant solution.
3. [Count Set Bits in a Number](https://github.com/brasssmonkey/dsa/blob/main/countBits.py): several alternative solutions.
4. [Find The Sum of Two Numbers Using Bitwise Operations](https://github.com/brasssmonkey/dsa/blob/main/getSum.py)

## Implementations of Data Structures
1. [(Random) Singly-Linked List](https://github.com/brasssmonkey/dsa/blob/main/LL.py): an implementation of a singly-linked list class that helped me test and debug numerous linked list problems. This implementation supports an extra "random" pointer added to each node (I added this to help test the problem [Random Linked List]()). It is most definitely a work in progress: moving forward, I am planning to add sentinels, array representation of a link list (to simplify debugging), and more methods and features. For now, treat this as a bare-bones class for testing/debugging.
2. [Kth Largest Element](https://github.com/brasssmonkey/dsa/blob/main/KthLargestElement.py): a heap-based class to get nth largest element in a stream. Very helpful problem for learning to think about streams.
3. [Time-Based Key-Value Storage](https://github.com/brasssmonkey/dsa/blob/main/timeBasedKeyValueStore.py): a dictionary-based data structure that remembers when each value was added. Get method retrieves value that was current at a given time; its implementation relies on binary search.

## Linked Lists
1. [Reverse Singly Linked List](https://github.com/brasssmonkey/dsa/blob/main/LLreverse_train.py)
2. [Copy Random List](https://github.com/brasssmonkey/dsa/blob/main/copyRandomList.py): copy a linked list where an extra random pointer is attached to each node.

## Dynamic Programming
1. [Find Max Subarray](https://github.com/brasssmonkey/dsa/blob/main/MaxSub.py): within an array, find a contiguous subarray that sums up to maximum value.
2. [Climbing Stairs](https://github.com/brasssmonkey/dsa/blob/main/climbingStairs.py): classic simple dynamic programming problem which turns out to be the fibonacci sequence in disguise.
3. [Min Cost Climbing Stairs](https://github.com/brasssmonkey/dsa/blob/main/minCostClimbingStairs.py): similar to Climbing Stairs, but instead of keeping track of the number of different options we keep track of the total cost of climbing (a cost is tied to each step).
4. [House Robber](https://github.com/brasssmonkey/dsa/blob/main/houseRobber.py): an amazing problem that allowed me to learn more about dynamic programming and memoization. It is simple but versatile, and the diversity of possible solutions makes one thing about trade-offs. Three solutions (exponential-time brute force, recursive with memoization, and dynamic programming iterative) are provided.
5. [House Robber II](https://github.com/brasssmonkey/dsa/blob/main/houseRobberII.py): a circular spin on House Robber problem.
6. [Longest Consecutive Sequence](https://github.com/brasssmonkey/dsa/blob/main/longestConsecutiveSequence.py): a good problem to learn to think about intelligent sequence building.
7. [Longest Increasing Subsequence](https://github.com/brasssmonkey/dsa/blob/main/longestIncreasingSubsequence.py): one of those cases where I didn't know how to approach a problem and reading other's explanations/analyses taught me a lot. A LOT! Dynamic Programming simply rocks :)

## Arrays
1. [Is This String a Valid Palindrome?](https://github.com/brasssmonkey/dsa/blob/main/ValPal.py)
2. [Find The Sum of All Elements in an Array](https://github.com/brasssmonkey/dsa/blob/main/binaryListsum.py): this solution uses binary recursion to optimize space usage.
3. [Find The Duplicate Number in an Array](https://github.com/brasssmonkey/dsa/blob/main/findDup.py): a LOT of possibilities with this problem. Multiple alternative solutions are provided.
4. [Top K Frequent Elements](https://github.com/brasssmonkey/dsa/blob/main/topKFrequentElements.py): a very cool problem that can be approached in a variety of ways. I have two implementations using a heap and bucket sort.

## Heaps
1. [Last Stone Weight](https://github.com/brasssmonkey/dsa/blob/main/lastStoneWeight.py): a simple heap-based algorithm that utilizes a little trick for making maxheaps using heapq.
2. [K Closest Points to Origin](https://github.com/brasssmonkey/dsa/blob/main/kClosestPointstoOrigin.py): a very fun problem that got me thinking about heaps and tweaking heap-based approaches. Leetcode article suggests an O(nlogn) sorting-based solution, too, but since we don't care about the order of outputs, full sorting is a waste of time; heaps are faster and more interesting to work with (imho, in this problem). However, the article also suggests a divide-and-conquer quickselect approach, which is very intriguing and more efficient on certain inputs. It is implemented [insert reference/link one implemented].

## Greedy Algorithms
1. [Jump Game](https://github.com/brasssmonkey/dsa/blob/main/jumpGame.py): a fun and easy classic
2, [Jump Game II](https://github.com/brasssmonkey/dsa/blob/main/jumpGameII.py): another fun algorithm that looks like it calls for dynamic programming, but can be solved in O(n) time using a greedy approach with a breadth-first search heuristic.

## Intervals
1. [Meetings Rooms](https://github.com/brasssmonkey/dsa/blob/main/meetingRooms.py): simple problem: sorting an array of arrays and checking that a condition is fulfilled in the sorted array.
2. [Meeting Rooms II](https://github.com/brasssmonkey/dsa/blob/main/meetingRoomsII.py): a greedy algorithm for calculating the minimum necessary number of meeting rooms. This is a seemingly tricky problem that has a surprisingly clear and intuitive solution. (You know, as greedy algorithms tend to be :) ) 
3. [Insert Interval](https://github.com/brasssmonkey/dsa/blob/main/insertInterval.py): a fun problem to start thinking about intervals.
4. [Merge Intervals](https://github.com/brasssmonkey/dsa/blob/main/mergeIntervals.py): another interesting and approachable problem to think about the mechanics of merging.

## Stacks
1. [Evaluate Reverse Polish Notation](https://github.com/brasssmonkey/dsa/blob/main/evaluateRPN.py)

## Miscellaneous
1. [English Ruler](https://github.com/brasssmonkey/dsa/blob/main/EnglishRuler.py): elementary algorithm that prints out an english ruler in your terminal.
2. [Find The Duplicate Number in an Array Using Floyd's Cycle-Finding Algorithm](https://github.com/brasssmonkey/dsa/blob/main/floydsFindDup.py): a very interesting alternative solution to the findDuplicate problem.
3. [Fibonacci Numbers 1 (recursive only)](https://github.com/brasssmonkey/dsa/blob/main/goodFib.py), [Fibonacci Numbers 2 (recursive and iterative)](https://github.com/brasssmonkey/dsa/blob/main/fibonacci.py): recursive and iterative versions of an O(n) time memoization-based algorithm to generate nth Fibonacci number. I'm proud of the iterative one, lol!

## In Progress
