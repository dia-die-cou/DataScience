import pandas as pd
from matplotlib import pyplot
import datetime

def parse_year_string(year_string):
	if not year_string:
		return 0

	if year_string.endswith("M"):
		format_pattern = "%m/%d/%Y %I:%M:%S %p"
	else:
		format_pattern = "%m/%d/%Y %H:%M:%S"

	return datetime.datetime.strptime(year_string, format_pattern).year


converters = {
	"year": parse_year_string
}

meteorites = pd.read_csv("../Meteorites_data_science/NASA.csv", converters=converters)
print(meteorites.head(10)) # Takes first 10
# print(meteorites.tail(10)) # Takes the last 10
# print(meteorites.dtypes) # See how pandas interpreted meteorites

figure, axes = pyplot.subplots()

def map_value(value, min_value, max_value, lower, upper):
	return (value - min_value ) / (max_value - min_value) * (upper - lower) + lower

sizes = []

for mass in meteorites["mass (g)"]:
	size = map_value(mass, 0, 6000000, 1, 200)
	sizes.append(size)

axes.scatter(meteorites.year, meteorites.reclat)
pyplot.show()