# Team Names:
# Course: CS151, Dr. Rajeev
# Lab Number: 11
# Problem Summary: Compare iterative and recursive implementations of fibonacci
# sequence and binary search.
#
# Inputs:
#
#   Choice of which function to time:
#       recursive fibonacci,
#       iterative fibonacci,
#       recursive binary search
#       iterative binary search
#
#   Corresponding argument for function:
#       term to calculate if fibonacci
#       number of random searches to perform if binary search
#
# Outputs: Running time of the function chosen with given arguments.
#
# Original by Dr. M. Olsen, 2018
# Modified by Dr. P. Simari, 2019

import random
import time

# global constant for size of binary search list [DO NOT EDIT]
SEARCH_SIZE = 1000000


# ------------------------------------------------------------------------------
# Purpose: Finds numbers in the Fibonacci sequence using iteration
# Parameters: n - element of the Fibonacci sequence to find
# Returns: The nth element of the Fibonacci sequence
def fibonacci_iterative(n):

    # if desired term is the 1st or 2nd
    if n < 3:

        return 1

    else:

        # initialize previous terms
        t_prev1 = 1
        t_prev2 = 1

        # for i from 3 to n
        for i in range(3, n+1):

            # calculate the i-th term
            t_i = t_prev2 + t_prev1

            # update previous terms
            t_prev2 = t_prev1
            t_prev1 = t_i

        return t_i


# ------------------------------------------------------------------------------
# Purpose: Finds numbers in the Fibonacci sequence by recursion
# Parameters: n - element of the Fibonacci sequence to find
# Returns: The nth element of the Fibonacci sequence
def fibonacci_recursive(n):

    # if desired term is the 1st or 2nd
    if n < 3:

        return 1

    else:

        # the n-th term is the sum of the previous two
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# ------------------------------------------------------------------------------
# Purpose: Performs a binary search
# Parameters: sorted_list - a sorted list of values to search;
#             value - the value to find in the list
# Returns: The index of the value in the list, or -1 if not present
def binary_search_iterative(sorted_list, value):

    # set initial range to include whole list
    start = 0
    end = len(sorted_list) - 1

    # as long as the search range is not empty
    while start <= end:

        # find index at middle of range (use integer division)
        mid = (start + end)//2

        # if value is at the middle index
        if sorted_list[mid] == value:

            # found the value: return the index
            return mid

        # else if value is smaller than what is at middle index
        elif value < sorted_list[mid]:

            # search in first half (discard second half)
            end = mid - 1

        else:

            # search in second half (discard first half)
            start = mid + 1

    return -1


# ------------------------------------------------------------------------------
# Purpose: Performs a binary search
# Parameters: sorted_list - a sorted list of values to search;
#             value - the value to find in the list;
#             start - the index of the first element to search from;
#             end - the index of the last element to search to
# Returns: The index of the value in the list, or -1 if it does not present
def binary_search_recursive(sorted_list, value, start, end):

    # TODO: Implement this function using recursion

    return -1


# ------------------------------------------------------------------------------
# Purpose: Measures time taken by n random binary searches on a sorted list of
# size SEARCH_SIZE (global constant) using the iterative implementation.
# Parameters: n - number of times to perform the search
# Returns: total time taken for all searches
def time_binary_search_iterative(n):

    # create a sorted list to search through
    sorted_list = list(range(SEARCH_SIZE))

    # initialize total time spent to zero
    total_time = 0

    # repeat n times
    for i in range(n):

        # pick a random number to search for
        target = random.randint(0, SEARCH_SIZE)

        # perform binary search and add running time to total time
        start = time.process_time()
        binary_search_iterative(sorted_list, target)
        total_time += time.process_time()-start

    return total_time


# ------------------------------------------------------------------------------
# Purpose: Measures time taken by n random binary searches on a sorted list of
# size SEARCH_SIZE (global constant) using the recursive implementation.
# Parameters: n - number of times to perform the search
# Returns: total time taken for all searches
def time_binary_search_recursive(n):

    # create a sorted list to search through
    sorted_list = list(range(SEARCH_SIZE))

    # initialize total time spent to zero
    total_time = 0

    # repeat n times
    for i in range(n):

        # pick a random number to search for
        target = random.randint(0, SEARCH_SIZE)

        # perform binary search and add running time to total time
        start = time.process_time()
        binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
        total_time += time.process_time() - start

    return total_time


# ------------------------------------------------------------------------------
# Purpose: Get type-safe integer input from the user
# Parameters: Message to display to the user
# Returns: int typed in by the user
def input_int(msg):

    # ask user for an integer using given message as prompt
    candidate = input(msg)

    # while the user hasn't provided an integer
    while not candidate.isdigit():

        # ask again
        print("Invalid input. Please enter an integer.")
        candidate = input(msg)

    # return user's input, typecast to an int
    return int(candidate)


# ------------------------------------------------------------------------------
# Purpose: Get menu selection from the user
# Parameters: none
# Returns: int of menu choice
def get_menu_choice():

    # create a string with menu options
    menu_options = "\t1. Naive Recursive Fibonacci\n" +\
                   "\t2. Iterative Fibonacci\n" +\
                   "\t3. Recursive Binary Search\n" +\
                   "\t4. Iterative Binary Search\n" +\
                   "\t0. Exit"

    # present menu to user
    print()
    print("Please select which function you would like to time: ")
    print()
    print(menu_options)

    # Get valid menu choice from user (re-ask as necessary)
    print()
    choice = input_int("Your selection: ")

    # while choice is not in valid range
    while not (0 <= choice <= 4):

        # output error and re-input choice
        print("Error, invalid choice. Please choose 0-4: ")
        print()
        print(menu_options)
        print()
        choice = input_int("Your selection: ")

    return choice


# ------------------------------------------------------------------------------
# Purpose: Allows comparing running times of function implementations
# Parameters: none
# Returns: none
def main():

    # output purpose
    print("This program measures the running time of various functions.")

    # Get user's choice
    choice = get_menu_choice()

    # while the user hasn't chosen to quit...
    while choice != 0:

        # perform choice
        if choice == 1:

            # Recursive Fibonacci
            n = input_int("Enter the term number to calculate: ")

            start = time.process_time()
            fibonacci_recursive(n)
            total = time.process_time() - start

        elif choice == 2:

            # Iterative Fibonacci
            n = input_int("Enter the term number to calculate: ")

            start = time.process_time()
            fibonacci_iterative(n)
            total = time.process_time() - start

        elif choice == 3:

            # Recursive Binary Search
            n = input_int("Enter the number of searches to perform: ")
            total = time_binary_search_recursive(n)

        elif choice == 4:

            # Iterative Binary Search
            n = input_int("Enter the number of searches to perform: ")
            total = time_binary_search_iterative(n)

        # Output timing results rounded to 1/100 of a second.
        print("The function ran in", round(total, 2), "seconds.")

        # Ask user to choose another option
        choice = get_menu_choice()


# ------------------------------------------------------------------------------
main()
# ------------------------------------------------------------------------------
