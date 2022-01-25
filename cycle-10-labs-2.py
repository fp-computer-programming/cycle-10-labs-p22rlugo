# Ryan Lugo: RJL 1/25/22

from timeit import repeat


def divisible_by_five(table):
    numbers_divisble = [] # Empty table for later use
    for number in table: # For each number in the table
        if number % 5 == 0 and number <= 150: # Has to meet the two conditions (Don't know why you want something less than 150 but it can't be higher than 500?)
            numbers_divisble.append(number) # Add each number to a table to be returned to the user
        elif number > 500: # Simple else if condition which if met it will stop the function
            break

    return numbers_divisble

print(divisible_by_five([5,10,20,9,8,20,19,17,200,20,20]))