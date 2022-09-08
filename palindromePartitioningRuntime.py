# This file contains just text (no code). It an analysis of runtime 
# complexity of a standard solution to Palindrome Partitioning (Leetcode 131).
# This explanation belongs to Leetcode user codease.

# 1. A string of length N will have (N, N-1, N-2, .. 1) substrings
# at positions (0, 1, 2, ... N-1) respectively. So the total number of
# substrings of a string is N + N-1 + ... + 1 = O(N^2). It is not exponential.

# 2. The number 2^N in complexity analysis above is in fact the number of nodes in
# the search tree, not the number of substrings. It is the number of possible 
# partitionings (each partitioning to partition the string into substrings).

# This can be derived as follows:
# Imagine the string as a sequence of N characters separated by a pipe
# between neighbors, such as a string "abcde" = a|b|c|d|e. This representation
# will have N-1 pipes: in this example, four.
# If you want the partitioning to have 4 substrings, then you can ask: how many
# ways can I select three pipes out of the four pipes? Answer is 4 choose 3, i. e.
# 4C3 = 4. The 4 ways to partition are {{"a", "b", "c", "de"}, {"a", "b", "cd", "e"},
# {"a", "bc", "d", "e"}, {"ab", "c", "d", "e"}}.

# Arguing like the above, the total number of ways to partition this example is when we
# ask all questions "how many ways can I select 0 or 1 or 2 or 3 or 4 pipes?". 4C0 +
# 4C1 + 4C2 + 4C3 + 4C4 = 2^4 = 16 partitionings.

# In general, a string of length N will have (N-1)C0 + (N-1)C1 + ... + (N-1)C(N-1) =
# = 2^(N-1) = O(2^N) partitionings.

# For each partitioning, we do two things:
# Build the substrings for that partition.
# Check whether each substring in that partitioning is a palindrome
# or not.
# Since the number of characters in each partitioning is N, cost of the above
# operations is N + N = 2N = O(N).
# Later, in approach 2, when we improve the logic using dynamic programming,
# it does not change the overall time complexity since we would still need to build
# the substrings!

# Combining all of these, intermediate conclusions, we get O(n*(2^n)).

# DFS in the stnadard implementation (see Leetcode/my file) works by first finding
# all partitionings where the first substring chosen has 1 character, i. e. ends at start.
# Then the first substring chosen has two characters... Overall. the endth iteration
# of the loop has all characters up to end in the first substring.

# Along the way, if a substring is found that is not a palindrome, the search tree gets
# pruned. That is, we won't go deeper, and further partitioning effort stops (all partitionings
# that would have included that non-palindrome/that substring will not get completed). 