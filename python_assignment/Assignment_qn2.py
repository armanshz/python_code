#Qns 2(i)
value = 0
while True:
    value = value+1
    print(value)

#Qns 2(ii)
import numpy as np
# Initialises a 1D array A with elements 1 to 10
A = np.arange(1,11)
# Saves A as tempfile.npy
np.save(r"E:\python\tempfile.npy",A)

#Qns 2(iii)
import numpy as np
A = np.linspace(0,20,6)
print(A)

#Qns 2(iv)
import time as time
from datetime import datetime as dt
# Retrieves current system time
currentTime = dt.now()
# Formats current time into HH:MM:SS format
formatTime = currentTime.strftime("%H:%M:%S")
print("The time now is", formatTime)
print("Sleeping for 5 seconds...")
# Pauses execution for 5 seconds
time.sleep(5)
# Calls current system time again
currentTime = dt.now()
formatTime = currentTime.strftime("%H:%M:%S")
print("The time now is",formatTime)

#Qns 2(v)
import math
ans = math.cos(math.pi/math.sqrt(4))
print(ans)

