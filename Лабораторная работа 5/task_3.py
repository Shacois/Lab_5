import random

def get_unique_list_numbers() -> list[int]:
    random_list = []
    for i in range(15):
        n = random.randint(-10, 10)
        while n in set(random_list):
            n = random.randint(-10, 10)
        random_list.append(n)
    return random_list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
