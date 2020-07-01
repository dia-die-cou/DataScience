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


meteorites = []
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

        meteorites.append(meteor)
        
        '''
        if meteor["mass (g)"]:
            meteor["mass (g)"] = float(meteor["mass (g)"])
        else:
            continue
        '''
'''
# (one way not dynamic)
next(content)
for row in content:
    # row = row.split(",")
    meteor = {
        "name": row[0],
        "id": row[1],
        "nametype": row[2],
        "recclass": row[3],
        "mass": row[4],
        "fall": row[5],
        "year": row[6],
        "reclat": row[7],
        "namereclong": row[8],
        "GeoLocation": row[9]
    }
    # if meteor["mass"]:
    #     meteor["mass"] = meteor["mass"]

    meteorites.append(meteor)
'''

#'''
# (largest mass)
largest = max(meteorites, key=get_mass)
#'''
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