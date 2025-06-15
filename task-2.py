import random

def get_numbers_ticket(min, max, quantity):
    try:
        sorted_random_numbers_within_range = []
        if(min >=1 and max <=1000 and min <= quantity <= max):
            sorted_random_numbers_within_range = random.sample(range(min, max+1), quantity) 
            sorted_random_numbers_within_range.sort()            
            return sorted_random_numbers_within_range
        else:
            return sorted_random_numbers_within_range
    except TypeError:
        return "Incorrect input. Try again with integer numbers"

print(get_numbers_ticket(1, 49, 6))

