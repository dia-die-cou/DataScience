''' 
git config user.name diego
git config user.email diego.dia.cou@techtalents.club
'''

'''
mprof run .\FILENAME.PY
mprof plot
'''

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

import getpass
r = range(10)
print(dir(r))

r_i = iter(r)

print(dir(r_i))

print(next(r_i))
print(next(r_i))
print(next(r_i))
print(next(r_i))
print(next(r_i))
print(next(r_i))
print(next(r_i))
print(next(r_i))
print(next(r_i))
print(next(r_i))
# print(next(r_i))

# print(next(range(10)))

my_list = [3, 5, 5, 7, 9, 4]
my_list_iter = iter(my_list)

print(my_list_iter)
print(type(my_list_iter))


my_text = "hello"
my_text_iter = iter(my_text)


class a:
    def __iter__(self):
        return iter("hello!")


A = a()
iter(A)
for c in a():
    print(c)
'''
while user_input := input("Continue?: ") == "no":
'''

i = 0
while True:
    i = i + 3 if i < 3 else 0
    print("[", end='')
    for j in in range(3):
        if i == j:
            print("*", end="")

getpass.getpass("Enter your password: ")

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
