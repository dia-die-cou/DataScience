import random
numbers = []
'''
# (way 1)
for _ in range(10):
    numbers.append(random.randint(1, 100))
print(numbers)
'''

'''
# (way 2)
numbers = [random.randint(1, 100) for _ in Range(10)]ç
print(numbers)
'''

'''
# (way 3)
numbers = {i: random.randint(1, 100) for i in range(10)}
'''


'''
# (using zip)
zipped_items = list(zip(column_row)
for a, b in zipped_items
    print(a)
    print(b)
'''
'''
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i) 
'''

'''
def multiple_of(n, base):
    return n % base == 0
for n in range(1, 101):
    multiple_of(n,)
'''