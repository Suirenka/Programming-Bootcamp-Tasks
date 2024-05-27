# Author: An Cheng
# Date: 27/05/24
# -----------------------------
# Description: Given a list of digits, determine the integer that it represents
#              For example, given the list: [8,3,5,1],
#              the program will output 8351 as an integer.
# This program demonstrates how to combine digits in a list into a integer.
# Since we already know the list is consists of digits, we could calculate the integer by
# 1. start with 0, add the first number in the list
# 2. continuously add the following numbers and multiply the previous sum by 10 until the last digit
# Then it prints the sum as the result
# This program works since we've already provided with a list of digits (ints) and
# we are required to give a int output so we can directly calculate it

# main function to determine the interger it represents
# usually we will have one main function for each program
def main():
    given_list = [8, 3, 5, 1] # given list
    output = 0 # a integer variable that hold the output
    for digit in given_list: # add each digit to the end
        output = output*10 + digit
    print(output) # print the output

# when running this file, this will call the main function
if __name__ == "__main__":
    main() # call the main function