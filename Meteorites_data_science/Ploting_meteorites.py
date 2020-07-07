# import matplotlib.pyplot as plt
from  matplotlib import pyplot
from day_1  import meteorites
from collections import defaultdict

counts = defaultdict(int)
for meteor in meteorites:
    year = meteor["year"][6:10]
    counts[year] += 1

print(counts)

pyplot.bar(counts.keys(), counts.values())
# pyplot.plot(counts.keys(), counts.values())
# pyplot.scatter()

pyplot.show()