# Ryan Lugo: RJl 1/25/22

def sum_of_numbers(number):
    counter = 0
    table = []
    while counter < number:
        counter += 1
        table.append(counter)
    counter = 0
    for i,v in enumerate(table):
        counter += v
    return counter

print(sum_of_numbers(10))