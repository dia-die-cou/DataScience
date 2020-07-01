# for i in range(10):
# print(i)
import csv

def file(file_name):
    file = open(file_name, "r", encoding="utf-8")
    content = csv.reader(file)
    # file.close()
    return(content)

def get_mass(meteor):
    return meteor["mass (g)"]

def get_name(meteor):
    return len(meteor["name"])

content = file("NASA.csv")
# lines = content.splitlines()
def process_meteorites(contents):
    processors = [
        str, int, str, str, float, str, str, float, float, str
    ]

    column_names = next(content)
    for row in content:
        processed_data = []
        for proc, data in zip(processors, row):
            try:
                processed_data.append(proc(data))
            except  ValueError:
                break
        else:
            # meteor = {column_names[i]: row[i] for i in range(len(column_names))}
            meteor = {name: data for name, data in zip(column_names, processed_data)}  # Pythonic
            yield meteor

meteorites = process_meteorites(content)

# '''
# (largest mass)
largest = max(meteorites, key=get_mass)
# '''
'''
# (largest name lenght)
largest = max(meteorites, key=get_name)
'''
print(largest)

# a = print
# a("hello")

# file.close()

'''
zipped_items = list(zip(column_row)
for a, b in zipped_items
    print(a)
    print(b)
'''