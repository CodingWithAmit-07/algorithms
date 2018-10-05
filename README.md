# Algorithms in C and Python

## List of Algorithms

###### Level 1: Easy
###### Level 2: Medium
###### Level 3: Hard
###### Level 4: Memory based

#### **: If there multiple solutions for a given solution, go with this.

- [Karatsuba algo](karatsuba.py): Efficient way to multiply 2 numbers, karatsuba algo.
- [Check cycle in graph](cycle_in_graph.py): Uses DFS approach to check if cycle exists in a directed graph.
- [Topological sort](topological_sort.py): Topological order of directed acyclic graph(DAG) using DFS.
- [Level order tree traversal](Level-3/level_order_tree_traversal.c): Level order traversal of a tree | O(n^2) | Level 3.
- [Level order tree traversal using queue**](Level-2/level_order_tree_traversal_using_queue.c): Level order traversal of a tree using queue | O(n) solution, requires extra space to manage queue | O(n) time and space | Level 2.
- [Shortest path of DAG](shortest_path_for_DAG.py): Find shortest in a directed acyclic graph from a source vertex to all reachable vertex | O(V + E).
- [Bellman ford](Level-3/bellman_ford.py): Bellman ford algo to find shortest path in a graph | O(VE) | Level 3.
- [Edit distance](Level-3/edit_distance.c): Find minimum operations required to convert a source string to target string | Level 3.
- [Flip your caps](Level-3/flip_your_cap.c): You all will conform | flip your cap(s) puzzle | Level 3.
- [Find 1-D peak](Level-2/find_peak_element.c): Find 1-D peak from an array | Level 2.
- [Find 2-D peak](Level-3/find_2d_peak.c): Find 2-D peak from a 2-D array | Level 3.
- [Find second largest number](Level-1/second_largest_in_array.c): Find second largest number from an array | Level 1.
- [Find element with rank k](Level-1/rank_k_element_in_2_sorted_array_O_k.c): Find element with rank k(or kth smallest number) between 2 sorted arrays in ascending sorted | O(n) | Level 1.
- [Find element with rank k - log(n)**](Level-3/rank_k_element_in_2_sorted_array_log_k.c): Find element with rank k(or kth smallest number) between 2 sorted arrays in ascending sorted having distinct elements | O(log(n)) | Level 3.
- [Search element in rotated sorted array](Level-3/search_in_rotated_sorted_array.c): Search an element from rotated sorted array | Level 3.
- [Heap sort using max heap](Level-3/heap_sort_using_max_heap.c): Build a max heap and sort array in ascending order.
- [Heap sort using min heap](Level-3/heap_sort_using_min_heap.c): Build a min heap and sort array in descending order.
- [Check strings has unique characters](Level-1/unique_characters_check_in_string.c): Check if a string has all unique characters or not | Level 1.
- [2 strings are permutations](Level-2/strings_permutation_check.c): Check if 2 strings are permutations of each other or not | Level 2.
- [Update input string](Level-2/url_formatter.c): Update(in-place) input string to have space replaced with %20 | O(n) | Level 2.
- [Is permutation palindrome](Level-2/is_any_permutation_palindrome.c): Check if any permutation of given string is palindrome or not | Level 2.
- [Check 2 strings, one edit away](Level-2/are_two_strings_one_edit_away.c): Check if 2 strings are max one edit away or not | O(n) | Level 2.
- [String compression](Level-2/string_compression.c): Compress string, show count for consecutive repeating characters | O(n) | Level 2.
- [Rotate square matrix](Level-3/rotate_matrix.c): Rotate square matrix clockwise by 90 degrees | O(n) | Level 3.
- [Clear row and column if 0 found](Level-3/clear_matrix_rows_and_coulmns.c): If an element in a matrix is 0, its entire row and column are set to 0 | O(MxN) | Level 3.
- [2 strings are rotations](Level-2/are_2_strings_rotations.c): Check if 2 strings are rotations of each other or not | O(n) | Level 2.
- [Longest increainng subsequence - O(n^2)](Level-3/LIS_O_n2.c): Find length of longest increasing subsequence from an unsorted array | O(n^2) | Level 3.
- [Longest increainng subsequence - O(nlogn)**](Level-3/LIS_O_nlogn.c): Find length of longest increasing subsequence from an unsorted array | O(nlogn) | Level 3.
- [Binary representation](Level-1/binary_representation.c): Print binary representation of an integer | Level 1.
- [Insert M into N](Level-2/insert_bits_from_M_into_N.c): Insert bits in M to N at positions between i and j | Level 2.
- [Decimal fraction to binary](Level-1/decimal_fraction_to_binary.c): Convert binary fraction number between 0 and 1 to binary representation | Level 1.
- [Flip a bit, get max sequence of 1s](Level-2/flip_a_bit_to_get_max_seq_of_ones.c): Flip a bit to get maximum sequence of 1s in sequence | O(b) | Level 2.
- [Next largest number, same set bits](Level-4/next_largest_same_num_of_bits_set.c): Given a positive integer, find next largest number having same number of set bits | O(b) | Level 4.
- [Previous number, same set bits](Level-4/previous_num_having_same_num_of_bits_set.c): Given a positive integer, find previous number having same number of set bits | O(b) | Level 4.
- [Bit flips required to convert](Level-2/bits_flipped_to_convert.c): Determine the number of bits need to flip to convert integer A to B | Level 2.
- [Swap odd and even bits](Level-2/swap_odd_even_bits.c): Program to swap odd and even bits in an integer | Level 2.
- [Update screen array, draw line](Level-3/draw_line.c): Update pixels array based on input pixel points to draw a line | Level 3.
- [Knapsack problem](Level-4/knapsack.c): Given a knapsack (bag with capacity W), and N items having weights and values, Select items such that value is maximized | O(nxW) | Level 4.
- [Knapsack problem - Maximize weight](Level-4/knapsack_maximize_weight.c): Given a knapsack, maximize weights that can be carried in given knapsack, No item values given | O(nxW) | Level 4.
- [Merge 2 sorted arrays, in place](Level-2/merge_2_sorted_arrays_in_place.c): Merge 2 sorted arrays, in place | O(A + B) | Level 2.
- [Groups anagrams](Level-2/group_anagrams.py): Write a method to sort an array of strings so that all the anagrams are next to each other. | O(MxNxlog(N)) | Level 2.
- [Sorted search, no size](Level-1/search_in_infinite_sorted_array.c): Search an element from an infinite sized (size of array not given) sorted array | O(log(p)) | Level 1.
- [Search in sparse array](Level-2/search_string_in_sparse_array.py): Search a string from sparsely populated array of strings (other places has empty string) | O(log(n)) | Level 2.
- [Find all duplicates in array](Level-2/find_duplicates_in_4k_space.c): Find all duplicates in array (range 1 to 32,000) with memory 4k | O(n) | Level 2.
- [Search in sorted matrix](Level-3/sorted_matrix_search.c): Search for an element in a matrix having each row and each column sorted | O(M + N) | Level 3.
- [Remove obstacle](Level-2/remove_obstacle.py): Remove obstacle, amazon online test | O(MxN) | Level 2.
- [Rank from stream](Level-3/rank_from_stream.c): Find rank of an element from a stream of data | O(logn) | Level 3.
- [Peaks and valleys, sorting method](Level-2/peaks_and_valleys_O_nlogn.py): Arrange an unsorted in alternating sequence of peaks and valleys | O(NlogN) | Level 2.
- [Peak and valley, O(n) method**](Level-3/peaks_and_valleys_O_n.py): Arrange an unsorted array in alternating sequence of peaks and valleys | O(n) | Level 3.
- [Count ways to run n steps](Level-2/count_steps.py): Count the number of ways possible to run stairs having n steps (can take 1, 2 or 3 steps) | O(n) | Level 2.
- [Path of robot in grid](Level-3/robot_in_a_grid.py): Find path traversed by robot to reach from 0, 0 to row - 1, col - 1 | O(rc) | Level 3.
- [Min from sorted rotated](Level-3/min_in_sorted_rotated_array.c): Find min element from sorted rotated array | O(log(n)) | Level 3.
- [Tree level with max width](Level-3/level_with_max_width.c): Find tree level having max width/nodes | O(n) | Level 3.
- [Find magic index](Level-2/magic_index.c): Find magic index from an sorted array having distinct elements | O(log(n)) | Level 2.
- [Find magic index, duplicates allowed**](Level-3/magic_index_with_duplicates.c): Find magic index from an sorted array (having duplicates) | O(log(n)) | Level 3.
- [Generate all subsets of a set](Level-3/generate_all_subsets.py): Generate all subsets of a given set | O(n2^n) | Level 3.
- [Generate all subsets, binary method**](Level-2/generate_all_subsets_binary_method.py): Generate all subsets of a given set, binary representation method | O(n2^n) | Level 2.
- [Multiply 2 integers](Level-3/multiply_integers.c): Multiply 2 positive integers without using multiply operator | O(log(s)) | Level 3.
- [Print fibonacci numbers](Level-1/fibonacci.c): Print first n fibonacci numbers | O(n) | Level 1.
- [Tower of hanoi](Level-3/tower_of_hanoi.c): Print steps to solve tower of hanoi problem for n disks | O(2^n) | Level 3.
- [Compute all permutations - Unique chars**](Level-4/compute_all_permutations_unique_chars.py): Compute all permutations of a given string having unique characters | O(n^2 * n!) | Level 4.
- [Compute all permutations - Repeated chars](Level-4/compute_all_permutations_non_unique_chars.py.py): Compute all permutations of a given string having repeated characters | O(n * n!) | Level 4+.
- [Pair of valid parens](Level-2/pair_of_parens.py): Print all valid combinations of n pairs of parentheses | O(n * n!) | Level 2.
- [Paint fill](Level-2/paint_fill.py): Fill surrounding area with new color | O(2^r * 2^c) | Level 2.
- [Ways to represent n cents](Level-4/ways_to_represent_n_cents.c): Find number of ways to represent n cents using quarters, dimens, nickels and pennies | O(n * NUM_OF_DENOMS) | Level 4.
- [Place 8 queens on 8x8](Level-4/place_eight_queens.py): Print all ways to arrange 8 queens on a 8x8 chessboard so that none attack any other | O(GRID_SIZE^3) | Level 4.
- [Stack boxes to maximize height](Level-4/stack_boxes.py): Stack boxes to to have maximum height | O(2^n) | Level 4.
- [Boolean evaluation ways](Level-3/boolean_evaluation_ways.py): Total number of ways to get expected boolean result from a boolean expression | O(n) | Level 3.
- [Print prime numbers](Level-3/print_all_prime_numbers.py): Print all prime numbers from 1 to n, sieve of eratosthenes method | O(sqrt(n)log(log(n))) | Level 3.
- [Quick sort](Level-4/quick_sort.c): Implement quick sort for array of random numbers | O(nlogn) | Level 4.
- [Find min range, k sorted arrays](Level-3/min_range_k_sorted_arrays.c): Find min range which will have elements from all k arrays | O(n\*k) | Level 3.
- [Shortest winter days](Level-3/shortest_winter_days.c): Find shortest winter days from temperatures given in an array | O(n) | Level 3.
- [Min positive integer missing](Level-2/smallest_positive_missing.py): Find minimum positive number from an array having random integers | O(n) | Level 2.
- [Min positive integer missing - O(1) space**](Level-3/smallest_positive_num_missing_O_1_space.c): Find minimum positive number from an array having random integers | O(n) | Level 3.
- [Season with max amplitude](Level-2/season_with_max_amplitude.py): Find season with max amplitude | O(n) | Level 2.
- [Create sequence of 'a' and 'b'](Level-3/three_non_consecutive_ab.py): Given 2 numbers A and B, create sequence with at max 2 consecutive 'a' and 'b | O(A + B) | Level 3.
- [Check strings same](Level-1/case_insensitive_strcmp.c): Write a function to check if 2 strings are same, ignoring case | Level 1.
- [Multiple of 4](Level-1/check_multiple_of_4.c): Check if a number of 4 or not | Level 1.
- [Find 7n/8](Level-1/find_7by8_of_n.c): Find 7n/8 without using * and / operators | Level 1.
- [Clear both elements](Level-1/unset_both.c): Clear both array elements having at least a 0 and 1 | Level 1.
- [Binary palindrom](Level-2/is_num_binary_palindrdom.c): Check if a numbers binary representation is palindrome or not | Level 1.
- [Product of elements](Level-2/product_array_elements_except_self.c): Create a array having product of all elements except element at self index | Level 2.
- [Modified fibonacci](Level-1/modified_fibonacci.py): ######### File header pending ############# | Level 1.
- [Next word in dictionary](Level-2/next_word_in_dictionary.py): ########### File header pending ########## | Level 2.
- [Find log(n)](Level-1/find_log_n.c): Write one liner program to find log(n) with some base | O(n/b) | Level 1
- [Bubble sort](Level-2/bubble_sort.py): Implement bubble sort | O(n^2) | Level 2.
- [Selection sort](Level-2/selection_sort.py): Implement selection sort | O(n^2) | Level 2.
- [Insertion sort](Level-2/insertion_sort.py): Implement insertion sort | O(n^2) | Level 2.
- [Counting sort](Level-2/counting_sort.c): Implement count sort | O(n + k) | Level 2.
- [Radix sort](Level-4/radix_sort.c): Implement radix sort | O(digits\*(n + base)) | Level 4.
- [Merge sort](Level-3/merge_sort.c): Implement merge sort | O(nlogn) | Level 3.
- [Binary search tree](Level-3/binary_search_tree.c): BST insert, traverse, delete operations | Level 3.
- [AVL trees](Level-4/avl_balanced_tree.c): Implement AVL balanced trees - Insert, delete, search | Level 4.
- [Year with max population](Level-3/year_with_max_population.py): Given birth and death years, find year with max population | O(Y + P) | Level 3.
- [Linked list in python](Level-1/linked_list.py): Implement linked list in python.
- [Remove duplicates from linked list](Level-2/remove_duplicates_from_linked_list.py): Remove duplicates from a linked list | O(n) time and space | Level 2.
- [kth from last in linked list](Level-3/kth_from_last_in_linked_list.py): Find kth element from last of a singly linked list | O(n) | Level 3.
- [Delete node from linked list](Level-2/delete_node_from_linked_list.py): Given only reference to an arbitary node of a linked list, delete that node | O(1) | Level 2.
- [Reverse linked list](Level-3/reverse_linked_list.py): Reverse a linked list | O(n) | Level 3.
- [Graph BFS traversal](Level-3/graph_breadth_first_search.py): Breadth first search traversal of directed graph | O(V + E) | Level 3.
- [Happy number](Level-2/is_happy_number.c): Check if a given number is happy or not | O(n) | Level 2.
- [Partitio linked list](Level-2/partition_linked_list.py): Partition 2 linked lists with respect to a given value | O(n) | Level 2.
- [Sum digits of 2 linked list, digits in reverse order](Level-2/sum_of_linked_lists_reverse_order.py): Add 2 numbers stored in linked list in reverse order(12 is 2->1) | O(n) | Level 2.
- [Sum digits of 2 linked list, digits in forward order](Level-3/sum_of_linked_list_same_order.py): Add 2 numbers stored in linked list in forward order(12 is 1->2) | O(n) | Level 3.
- [Is linked list palindrome](Level-2/is_linked_list_palindrome.py): Check if linked list is palindrome or not | O(n) | Level 2.
- [Median in 2 sorted arrays](Level-4/median_in_2_sorted_arrays.py): Find median from 2 sorted arrays | O(log(min(m + n))) | Level 4.
- [Linked list intersection](Level-2/linked_list_intersection.py): Find if two linked list intersect each other | O(m + n) | Level 2.
- [Longest palindrome](Level-3/longest_palindrome_in_a_string.py): Find longest palindrome from a given string | O(n^2) | Level 3.
- [LCA in binary tree](Level-4/lowest_common_ancestor_in_binary_tree.py): Find lowest common ancestor in binary tree | O(n) | Level 4.
- [LCA in BST](Level-3/lowest_common_ancestor_in_binary_search_tree.py): Find lowest common ancestor in binary search tree | O(logn) | Level 3.
- [Starting node of loop in linked list](Level-4/starting_of_loop_in_linked_list.py): Detect loop in linked list and find startig node of loop | O(n) | Level 4.
- [Spiral matrix](Level-3/spiral_matrix.py): Given a number N, create matrix having values from 1 to N^2 in spiral form | O(N^2) | Level 3.
- [Print matrix in spiral](Level-3/print_matrix_in_spiral.py): Given a matrix, print its elements in clockwise spiral form | O(MxN) | Level 3.
- [Look and say sequence](Level-2/look_and_say_seq.py): Print look and say sequence for given number of input lines | O(N) | Level 2.
- [LCM and HCF](Level-1/gcd_and_lcm.py): Find GCD(or HCF) and LCM of 2 numbers | Level 1.
- [Vertical level order tree traversal](Level-2/vertical_level_order_tree_traversal.py): Perform vertical level order tree traversal | O(n) | Level 2.
- [Separate positives and negatives](Level-2/separate_positive_and_negative_nums.c): Move all positive to start and negative to end of array, 2 pointer problem | O(n) | Level 2.
- [Track kth largest, stream of numbers](Level-2/track_kth_largest_stream_of_nums.py): Keep track of kth largest number from a stream of numbers | O(k) | Level 2.
- [Track median, stream of numbers](Level-4/track_median_stream_of_nums.py): Keep track of median from stream of numbers | O(nlogn) | Level 4.
- [Check prime](Level-2/is_prime.go): Check if a given number is prime or not | O(sqrt(n)) | Level 2.
- [Find square root](Level-4/babylonian_square_root.go): Find square root of a number using babylonian convergence method | Level 4.
- [Substring matching, Rabin karp](Level-4/rabin_karp.c): Implement rabin karp algo for substring matching | O(m + n) | Level 4.
- [DFS traversal](Level-3/graph_depth_first_search.py): Creates a directed graph and performs DFS traversal | O(V + E) | Level 3.
- [Cycle in graph](Level-3/cycle_in_graph.py): Check if there is cycle in a directed graph, uses DFS | O(V + E) | Level 3.
- [Pairs having given sum](Level-2/pairs_having_given_sum.c): Given an array and required sum, find pairs in array that sums to required sum | O(n) time and space | Level 2.
- [Connections in matrix](Level-2/connections_in_matrix.py): Count possible connections in matrix of 0s and 1s | O(MxN) | Level 2.
- [Next power of 2](Level-1/next_pow_of_2.c): Find next power of 2 for a given number | Level 1.
- [Round off float](Level-1/round_off.c): Round off a float number to nearest integer | Level 1.
- [Sum of digits](Level-1/sum_num.c): Find sum of digits of a given integer | Level 1.
- [Generic linked list](Level-3/generic_linked_list.c): Generic linked list in C language | Level 3.
- [Count frequency of numbers](Level-1/frequency_of_elements.c): Count frequency of numbers in array | O(N) time and space | Level 1.
- [Count frequency, without space](Level-2/frequency_of_elements_without_space.c): Count frequency of numbers in array | O(N) time and O(1) space | Level 2.
- [Repeating numbers](Level-2/find_repeating_elements.c): Find all repeating numbers in a array | O(N) | Level 2.
- [Inversion of 3](Level-2/inversion_of_3.c): Find number of combinations which follows: a[i] > a[j] > a[k] with i < j < k in a unsorted array | O(N^2) | Level 2.
- [Equilibrium index](Level-2/find_equilibrium_index.c): Find equilibrium index in a array(Equal sum of left and right sub array) | O(N) | Level 2.
- [Majority element from array](Level-2/majority_element_in_array.c): Find majority(more than n/2 times) element from an array | Moore's voting algo | O(N) | Level 2.
- [Leaders in array](Level-1/leaders_in_array.c): Print all leaders in array(greater than all elements right to that) | O(N) | Level 1.
- [Odd occuring numberr](Level-2/find_2_odd_occurring_numbers.c): A array has all numbers occurring even numbers of times and 2 occurring odd number of times, find these 2 numbers | O(N) | Level 2.
- [Even occurring numbers](Level-3/find_2_even_occurring_numbers.c): Find 2 numbers in array(numbers from 1 to n - 2) occurring even number of times, other all occur odd number of times | O(N) | Level 3.
- [Common in 3 sorted arrays](Level-1/common_elements_in_3_sorted_array.c): Find common elements in 3 sorted arrays | O(n1 + n2 + n3) | Level 1.
- [Sorted subsequence of size 3](Level-3/sorted_subsequence_of_size_3.c): Find sorted subsequence of size 3 in an unsorted array | O(N) time and space | Level 3.
- [Sorted subsequence of size 3, O(1) space](Level-4/sorted_subsequence_of_size_3_without_space.c): Find sorted subsequence of size 3 in an unsorted array | O(N) time | Level 4.
- [Max average of len K](Level-2/max_average_of_len_k.c): Find sub array of len K having maximum average | O(N) | Level 2.
- [Subarray having given sum](Level-3/subarray_having_given_sum.c): Find a sub array(positive numbers) having sum | O(N) | Level 3.
- [Trie implementation](Level-3/trie_insert_search_delete.py): Implement trie and perform insert, search and delete operations | O(L) | Level 3.
- [Trie autocomplete](Level-3/trie_autocomplete.py): Implement word autocomplete feature using trie | O(ALPHABET_SIZE*N*L) | Level 3.
- [Trie, sorted strings](Level-2/trie_words_in_sorted_order.py): Print all words in trie, in sorted order | O(ALPHABET_SIZE*N*L) | Level 2.
- [Trie, longest prefix matching](Level-2/trie_longest_prefix_matching.py): Given a string, find a word from trie which matches longest prefix | O(n) | Level 2.
- [Pattern matching using suffix tries](Level-4/pattern_matching_using_suffix_tries.py): Implement suffix tries for pattern matching | O(m) | Level 4.
- [Triplets in GP](Level-2/find_triplets_in_gp.c): Given a sorted array, print triplets in GP | O(N^2) | Level 2.
- [ASCII to int](Level-2/atoi_using_bitwise.c): Given an ascii string convert it to integer, atoi conversion | O(N) | Level 2.
- [Largest sum of subarray](Level-3/largest_sum_of_subarray.c): Given an unsorted array(+ve and -ve numbers), find max sum possible of a subarray | Kadane's algo | O(N) | Level 3.
