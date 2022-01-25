# Ryan Lugo: RJL 1/25/22

from timeit import repeat


def divisible_by_five(table):
    for number in table:
        if number % 5 == 0 and number <= 150:
            print("d")
        elif number > 500:
            break
        else:
            repeat

print(divisible_by_five([5,10,20,9,8,20,19,17,200,502,20,20]))