# Ryan Lugo: RJl 1/25/22

def sum_of_numbers(number):
    counter = 0 # Set this to zero since we are always counting up (Doesn't account for negatives ofc)
    table = [] # Make an empty "table" to add each number
    while counter < number:
        counter += 1 # Used for each number that is going to be added until it reaches the number given
        table.append(counter) # Add it to the table for later adding
    counter = 0 # Set counter to 0 since it compeleted the while loop, and we use it for the final adding/math
    for i,v in enumerate(table): # Just add each number in the table together
        counter += v
    return counter

print(sum_of_numbers(10))