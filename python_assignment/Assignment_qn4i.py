#Qns 4(i)
# Produce analytical solution graph
import numpy as np
import matplotlib.pyplot as plt

x,y = np.arange(51), np.zeros([51])
y[0] = 1

for n in range(1,51):
    y[n] = np.sqrt(2/1+np.exp(-10*x[n]))

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Plot of analytical solution of y(x)")
plt.legend(['Analytical'])
plt.grid()
plt.show()

#Comparision of analytical and numerical solutions
import numpy as np
import matplotlib.pyplot as plt
# Initialises x and y axes for analytical curve
x, y = np.arange(51), np.zeros([51])
# Initialises step sizes 0.1 and 0.05
step1, step2 = 0.1,0.05
# Initialises x and y axes for numerical curves
xEu1, xEu5 = np.arange(0,50.1,0.1), np.arange(0,50.05,0.05)
yEu1, yEu5 = np.zeros([501]), np.zeros([1001])
# Sets y(0) to 1 for all 3 curves
y[0], yEu1[0], yEu5[0] = 1, 1, 1
# For loop to calculate analytical y values
for n in range(1,51):
      y[n] = np.sqrt(2/1+np.exp(-10*x[n]))
# For loop to calculate numerical y values (step size =0.1)
for n in range(1,501):
    yEu1[n] = yEu1[n-1]+ step1*(5*yEu1[n-1]-2.5*yEu1[n-1]**3)
# For loop to calculate numerical y values (step size =0.05)
for n in range(1,1001):
    yEu5[n] = yEu5[n-1]+ step2*(5*yEu5[n-1]-2.5*yEu5[n-1]**3)
# Plots all 3 curves, each with a different colour, adds labels, a title a legend and a grid
plt.plot(x,y)
plt.plot(xEu1,yEu1,'orange')
plt.plot(xEu5,yEu5,'grey')
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Analytical and numerical plots of y(x)")
plt.legend(['Analytical','h = 0.1','h= 0.05'])
plt.grid()
plt.show()

