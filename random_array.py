import numpy as np
import sys

#_________________________________________

x = np.random.randint(0, 256, size=(10, 10))

np.set_printoptions(threshold=sys.maxsize)

print ('#---------------------------------------------------- \n')

print ('x = np.random.randint(0, 256, size=(10, 10)) \n')

print (x)

print ('#---------------------------------------------------- \n')

print ('# CHECK THE OUTPUT.FILE TO SEE THE RESULT OF THE ARRAY \n')

print ('#---------------------------------------------------- \n')


with open("output.csv", "a") as f:
        print(x, file=f)

#print (x)

#np.set_printoptions(threshold=np.inf, linewidth=100)

