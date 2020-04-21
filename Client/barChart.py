from matplotlib import pyplot as plt
import numpy
import math
dev_x = ["Cofetarie 1","Cofetarie 2", "Cofetarie 3", "Cofetarie 4"]

dev_y = [2345, 1892, 3005,1924]
plt.polar()
plt.barh(dev_x,dev_y,0.25, math.radians(150))

plt.title("Castig zilnic in diferitele cofetarii din lant")

plt.show()