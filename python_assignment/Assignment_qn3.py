#Qns 3
import numpy as np
# Initialise a 100 by 9 null matrix to be filled with data
ClassList = np.zeros((100,9))
# Fills the first column with numbers 1 to 100
ClassList[:,0]=range(1,101)
# First for loop to generate random integer values as marks
for i in range(0,100):

    ClassList[i,1]= np.random.randint(40,101)
    ClassList[i,2]= np.random.randint(35,101)
    ClassList[i,3]= np.random.randint(50,101)
    ClassList[i,4]= np.random.randint(40,91)
    ClassList[i,5]= np.random.randint(60,86)
# Calculates the sum of columns 2 through 5 and fills column 6 with this value
    ClassList[i,6]=np.sum(ClassList[i,1:6])
# Calculates the average of columns 2 through 5 and fills column 6 with this value
    ClassList[i,7]=np.average(ClassList[i,1:6])
# Calculates the average of all the rows in column 6 as the class average
ClassAverage=np.average(ClassList[:,7])
# Second for loop to check conditional statement
for i in range(0,100):
    ClassList[i,8] = 1 if ClassList[i,7] >= ClassAverage else 2
# Prints completed ClassList
print(ClassList)
print('Average Class Score:', ClassAverage)

