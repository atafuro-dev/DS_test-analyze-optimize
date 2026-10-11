# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers): 
    if not numbers:
        return None
    #optimization
    counts = {} #prior to optimzation - the time it takes to continue to re-examine lists would increase as the inputs increased (not very optimal)
    for num in numbers: #builds dictionary: using a dictinary to count frequencies will reduce the time complexity issue but will maintain the space complexity.
        counts[num] = counts.get(num, 0) + 1

    return max(counts, key=counts.get) #finds the maximum frequency
    #optimzation edits end here, and performance is maintained
numbers = [1, 3, 2, 3, 4, 1, 3, 1]
print(most_frequent(numbers))
#ouput: 1

"""
Time and Space Analysis for problem 1:
- Best-case: The number set contains numbers with a higher frequency and the function is able to return the max frequency number count. 
- Worst-case: The number set contains all unique values and the code will continue to loop through the entire list.
- Average-case: Typically, it will be a set of numbers with a few high frequency integers and the function will return the expected count. 
- Space complexity: O(n) - a larger input will have a larger run time and memory, but it is a single loop of code running. 
- Why this approach? This approach allows for a search of the input list, and allows for the function to return the count of any high frequency (max) occuring number. 
- Could it be optimized? This approach could be optimized as the list is being sorted through every loop, and if the list is longer than it could be less efficient. 
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    return list(dict.fromkeys(nums)) #creates dictionary with list items 
nums = [4, 5, 4, 6, 5, 7]
output = remove_duplicates(nums) #calls the function on the list
print(output) #prints function called on the list
#output: [4, 5, 6, 7]

"""
Time and Space Analysis for problem 2:
- Best-case: The list is straightforward, and has duplicates that are easily stripped away. 
- Worst-case: The list has different data types and duplicates, and the code does not take away the duplicates or does not maintain the initial order. The code could also miss duplicates which is also not optimal. 
- Average-case: A list with duplicates will be stripped of duplicate values, and the output will be the unique values in their original order without duplicates. 
- Space complexity: O(n) - the dictionary is created, and looped through once to remove duplicates and output values. 
- Why this approach? This seemed to be the most straightforward way of removing values, but preserving order. The code creates a dictionary with the list items, and then calls on the function 
using dict.fromkeys to remove any duplicates in the list inputted. Since a dictionary needs unique values, any duplicates will be stripped away while not changing the order. 
- Could it be optimized? For this example, if the list were mostly straightforward or an average case, I feel as if this is an optimal approach. If the list were more complex, then maybe it would be a good idea
to optimize. There may be a node-based approach involved to ensure odd cases could be taken into consideration. 
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    unique_pairs = set()

    for num in nums:
        complement = target - num #calculates what the pair may need to be to sum to the target (new method)

        if complement in seen:
            pair = (min(num, complement), max(num, complement)) #treats (A,B) and (B,A) as the same (new method)
            unique_pairs.add(pair) #adding any additional pairs to the set output and prevents duplicate tuples
        seen.add(num)
    return list(unique_pairs) 
nums = (1, 2, 3, 4)
target_sum = 5 
print(find_pairs(numbers, target_sum))

"""
Time and Space Analysis for problem 3:
- Best-case: The values in the list have multiple combinations to add to the target sum, and the output is able to create the sets of values that total to the target value. 
- Worst-case: There are no values that total to the target sum, and the code does not have an output or it does not correctly calculate values and compare to the sum.
- Average-case: Some values will have a total to the target sum, and they will be shown in the output. 
- Space complexity: O(2^n) - the recursive combinations exponentially grow with the higher count of values in the list. 
- Why this approach? This approach allows for the interchangeable sets of values that add to the total target sum to be search, and added to a new list of sets. 
The target sum can be changed easily, and the output prints in the expected set format (ex. [(2, 3), (1, 4)])).
- Could it be optimized? I think this approach could be optimized, especially with larger sets, as the recursive combinations and searching grows it can slow down the process. 
In the Big O summary, it is noted that these can explode quickly and it becomes a large problem for larger inputs of values. 
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    my_list = []
    current_capacity = 6

    print(f" Initial Capacity is {current_capacity}")

    for element in n:
        #is the list full?
        if len(my_list) == current_capacity: #resizing
            old_capacity = current_capacity
            current_capacity *= 2 #doubling capacity 
            
            print(f"\n[!] Capacity Reached ({old_capacity}/{old_capacity}).")
            print(f" Creating a new list with double the capacity: {current_capacity}.")

            print("Copying elements:") 

            for item in my_list: 
                print(f" Copying {item}.")
    
        my_list.append(element)
        print(f"Added: {element} | Current List: {my_list}.")  
    
    return my_list

n = [1, 2, 3, 4, 5, 6, 7]
add_n_items(n)


"""
Time and Space Analysis for problem 4:
- When do resizes happen? Resizes occur when the data reaches over the initial capacity allowed. 
- What is the worst-case for a single append? The worst case for a single append would be that it does not follow the copy logic, and the value is not adding to the current or new list. 
- What is the amortized time per append overall? O(1)
- Space complexity: O(n^2) - I chose this as there are multiple loops in one, and I feel this could become a large slow down for larger inputs. 
- Why does doubling reduce the cost overall? Doubling could reduce the overall cost as it is a mostly efficient way to quickly re-organize data and still output it. Rather than having the code
stop and error out, this would re-copy and continue adding data. While it may not be the most efficient for larger sets, it can cut cost in my opinion. 
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10] #keeps running total of sums up until a certain index
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    result = [] #starting with an empty list
    running_total = 0 
    for num in nums:
        running_total += num #adds the num to running total 0
        result.append(running_total) #adds the running total just calculated to the list
    return result
numbers = [1, 2, 3, 4]
print(running_total(nums))


"""
Time and Space Analysis for problem 5:
- Best-case: The values easily flow through and continue to add to one another, while adding the total to the final result. 
- Worst-case: The values only add to the next value or themselves, and not continue to add until the end of the input while also not adding the results to the list. 
- Average-case: The input will be ran through and the totals of each combination will calculate, and be added to the running total. 
- Space complexity: O(n)
- Why this approach? This approach allows for each total to be added together, as well as kept track of by being added to the running total result. 
- Could it be optimized? I feel as if this approach is pretty straightforward, even with longer lists. It seems like it should just keep calculating, and adding no matter how many values. 
"""
