#Qn 4(ii)
#Produce analytical soultion graph [root = 0]
import numpy as np
import matplotlib.pyplot as plt
# Initialises x and y axes, each containing 50 values for x = 0 to 50
x,y = np.arange(1,51), np.zeros(50)
# For loop to calculate analytical y values
for n in range(0,50):
    y[n] = (x[n]-np.sqrt(x[n]**2-2*np.log(x[n])))
# Plots x and y using matplotlib, adding labels, a title, a legend and a grid
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Analytical solution for y(x) [root = 0]")
plt.legend(['Analytical'])
plt.grid()
plt.show()

#Produce analytical soultion graph [root = 2]
import numpy as np
import matplotlib.pyplot as plt
# Initialises x and y axes, each containing 50 values for x = 0 to 50
x,y = np.arange(1,51), np.zeros(50)
# For loop to calculate analytical y values
for n in range(1,50):
    y[n] = (x[n]+np.sqrt(x[n]**2-2*np.log(x[n])))
# Plots x and y using matplotlib, adding labels, a title, a legend and a grid
plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Analytical solution for y(x) [root = 2]")
plt.legend(['Analytical'])
plt.grid()
plt.show()


#comparison of analytical vs numerical solution (Euler’s method, step size 0.1 and 0.05) for negative root = 0 
import numpy as np
import matplotlib.pyplot as plt

# (Analytical curve) Initialises x axis, sets x from 1 to 50, and y axis as empty array of same size (to be filled with y values later)
x, y = np.arange(1,51), np.zeros(50)
# Initialises step sizes 0.1 and 0.05 as step1 and step2
step1, step2 = 0.1,0.05
# Initialises x and y axes for the numerical curves. y axis would have 491 values for h = 0.1, and 981 values for h = 0.05
xEu1, xEu5 = np.arange(1,50.1,0.1), np.arange(1,50.05,0.05)
yEu1, yEu5 = np.zeros([491]), np.zeros([981])
# Sets y(0) for all 3 curves = 0 [Analytical negative root]
y[0], yEu1[0], yEu5[0] = 0, 0, 0
# For loop to calculate y values [Analytical negative root]
for n in range(0,50):
     y[n] = (x[n]-np.sqrt(x[n]**2-2*np.log(x[n])))
# For loop to calculate y values (h= 0.1)
for n in range(1,491):
    yEu1[n] = yEu1[n-1] + step1*((1-xEu1[n-1]*yEu1[n-1])/(xEu1[n-1]**2-xEu1[n-1]*yEu1[n-1]))
# For loop to calculate y values (h= 0.05)
for n in range(1,981):
    yEu5[n] = yEu5[n-1] + step2*((1-xEu5[n-1]*yEu5[n-1])/(xEu5[n-1]**2-xEu5[n-1]*yEu5[n-1]))
# Plots all 3 curves on their respective axes, each with a different colour, adds labels, a grid and legends for identification
plt.plot(x,y)
plt.plot(xEu1,yEu1,'orange')
plt.plot(xEu5,yEu5,'grey')
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Analytical and numerical plots of y(x) [root = 0]")
plt.legend(['Analytical','h = 0.1','h= 0.05'])
plt.grid()
plt.show()


#comparison of analytical vs numerical solution (Euler’s method, step size 0.1 and 0.05) for positive root = 2
import numpy as np
import matplotlib.pyplot as plt

# (Analyti-cal curve) Initialises x axis, sets x from 1 to 50, and y axis as empty array of same size (to be filled with y values later)
x, y = np.arange(1,51), np.zeros(50)
# Initialises step sizes 0.1 and 0.05 as step1 and step2
step1, step2 = 0.1,0.05
# Initialis-es x and y axes for the numerical curves. y axis would have 491 values for h = 0.1, and 981 values for h = 0.05
xEu1, xEu5 = np.arange(1,50.1,0.1), np.arange(1,50.05,0.05)
yEu1, yEu5 = np.zeros([491]), np.zeros([981])
# Sets y(0) for all 3 curves = 2
y[0], yEu1[0], yEu5[0] = 2, 2, 2
# For loop to calculate y values (Analytical)
for n in range(0,50):
     y[n] = (x[n]+np.sqrt(x[n]**2-2*np.log(x[n])))
# For loop to calculate y values (h= 0.1)
for n in range(1,491):
    yEu1[n] = yEu1[n-1] + step1*((1-xEu1[n-1]*yEu1[n-1])/(xEu1[n-1]**2-xEu1[n-1]*yEu1[n-1]))
# For loop to calculate y values (h= 0.05)
for n in range(1,981):
    yEu5[n] = yEu5[n-1] + step2*((1-xEu5[n-1]*yEu5[n-1])/(xEu5[n-1]**2-xEu5[n-1]*yEu5[n-1]))
# Plots all 3 curves on their respective axes, each with a different colour, adds labels, a grid and legends for identification
plt.plot(x,y)
plt.plot(xEu1,yEu1,'orange')
plt.plot(xEu5,yEu5,'grey')
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Analytical and numerical plots of y(x) [root = 2]")
plt.legend(['Analytical','h = 0.1','h= 0.05'])
plt.grid()
plt.show()