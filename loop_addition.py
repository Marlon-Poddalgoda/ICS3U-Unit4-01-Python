#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on December 2020
# This program calculates the sum of all positive integers between
#      0 and a user input


def main():
    # this function will calculate the sum of integers between 0
    #      and a user input using a loop

    print("This program adds up all the positive integers from 0 and a "
          "user's input.")

    # loop counter variable
    loop_counter = 0

    # sum of positive integers variable
    numbers_sum = 0

    # input
    user_input = input("Enter a positive integer: ")
    print("")

    # process
    try:
        user_input_int = int(user_input)

        if user_input_int > 0:
            while loop_counter < user_input_int:
                # calculations
                numbers_sum = numbers_sum + (loop_counter + 1)
                loop_counter = loop_counter + 1
            # output
            print("The sum of all the positive numbers between 0 "
                  "and {0} is {1}".format(user_input_int, numbers_sum))
        else:
            # output
            print("{} is not a positive integer!"
                  .format(user_input_int))
    except Exception:
        # output
        print("That's not a number! Try again.")


if __name__ == "__main__":
    main()
