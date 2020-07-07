# region
import sys
sys.path.append(sys.path.pop(0))

import math
import numpy as np
from matplotlib import pyplot

# x_coords = [0,1,2,3,4,5]
# y_coords = [0,5,0,5,0,5]

# pyplot.plot(x_coords, y_coords)
# # pyplot.show()
# pyplot.savefig("myplotlib.png")
# endregion
for  
x_coords = np.arange(1, 11, 0.1)
# x_coords = range(1, 10, 0.1) # It doesn't work
y_coords = np.sin(x_coords)
# y_coords = [math.sin(x) for x in x_coords]

# region
# pyplot.plot(x_coords, y_coords, "k") # Prints the graph line black
# pyplot.plot(x_coords, y_coords, "r") # Prints the graph line red
# pyplot.plot(x_coords, y_coords, "b") # Prints the graph line blue
# pyplot.plot(x_coords, y_coords, "g") # Prints the graph line green
# pyplot.plot(x_coords, y_coords, "w") # Prints the graph line white
pyplot.plot(x_coords, y_coords, "k.") # Prints the graph line black with dots
# pyplot.plot(x_coords, y_coords, "kx") # Prints the graph line black with X
# endregion

# region
# pyplot.ylim(1, 10) # y axi limit
# pyplot.xlim(-1, 1) # x axi limit
pyplot.xticks([0,1,2,3,4,5,6,7,8,9,10,11])
pyplot.title("My first graph") # Graph title
# pyplot.xlabel("x axis") # Names the side of the x axis
pyplot.xlabel("y axis", x=0.9, y=0) # Names the side of the x axis written to the left
pyplot.ylabel("y axis") # Names the side of the y axis
# endregion


pyplot.show() # Shows the graph
# pyplot.savefig("myplotlib.png") # Save it to a file.png called myplotlib.png