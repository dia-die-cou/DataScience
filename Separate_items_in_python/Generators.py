from sys import getsizeof

def calculator(maxs):
    numbers = []
    for i in range(maxs):
        numbers.append(i)
    print("Size: ", getsizeof(numbers))
    return sum(numbers)

def eager_total(maxs):
    numbers = []
    for i in range(maximum):
        numbers.append(i)
    return numbers


def lazy_total(maxs):
    print("Stage 1")
    for i in range(0, maxs):
        print("stage 2", i)
        yield i
        print("Stage 3", i)

answer = lazy_total(99999)
next(answer)
next(answer)
print("Total: ", answer)




'''
def lazy_total(maxs):
    for i in range(maxs):
        yield i



answer = sum(lazy_total(44873400))
'''


# mprof run .\FILENAME.PY
# mprof plot