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

meteorites = meteorites[meteorites.year != 0]

print(meteorites.head(10)) # Takes first 10
# print(meteorites.tail(10)) # Takes the last 10
# print(meteorites.dtypes) # See how pandas interpreted meteorites

figure, axes = pyplot.subplots()

def map_value(value, min_value, max_value, lower, upper):
	return (value - min_value ) / (max_value - min_value) * (upper - lower) + lower


step = 20

for lat in range(0, 180, step):
	selected = meteorites[lat < meteorites.reclong]
	selected = meteorites[meteorites.reclong < (lat + step)]

	sizes = []
	for mass in selected["mass (g)"]:
		size = map_value(mass, 0, 6000000, 1, 200)
		sizes.append(size)

	axes.scatter(selected.year, selected.reclat, s=sizes, alpha=0.5)
pyplot.show()