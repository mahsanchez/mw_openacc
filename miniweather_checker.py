# Copyright (c) 2020 NVIDIA Corporation.  All rights reserved.
#!/usr/bin/env python3

from netCDF4 import Dataset
import numpy



# Main #

# First file (baseline)
nc_f1 = '../source_code/checker/reference.nc'
try:
  rootgrp1 = Dataset(nc_f1, 'r')    # rootgrp is the object
except:
  print("Please copy reference.nc from the SOLUTION folder of your preferred programming language.")
  exit()

# Second file (new)
nc_f2 = '../source_code/checker/new.nc'
try:
  rootgrp2 = Dataset(nc_f2, 'r')    # rootgrp is the object
except:
  print("Please copy new.nc from the folder of your preferred programming language.")
  exit()

# Inputs:
t_compare = 1

print("Group 1 has ",rootgrp1.dimensions['t'].size," time slices")
print("Group 2 has ",rootgrp2.dimensions['t'].size," time slices")
print("Target Time Slice = ",t_compare)
print(" ")

# Error checking:
# ---------------
if (rootgrp1.dimensions['t'].size < t_compare):
    print("Not enough time slices in file 1. Reduce t_compare. Stopping");
    exit()
#end if
if (rootgrp2.dimensions['t'].size < t_compare):
    print("Not enough time slices in file 2. Reduce t_compare. Stopping.");
    exit()
#end if

# Check if the two files use the same "time" for the comparison?


# Pull out t_compare slice of variables dens, uwnd, wwnd, theta
# --------------------------------------------------------------
# File 1:
dens1 = rootgrp1.variables['dens'][t_compare,:,:]
uwnd1 = rootgrp1.variables['uwnd'][t_compare,:,:]
wwnd1 = rootgrp1.variables['wwnd'][t_compare,:,:]
theta1 = rootgrp1.variables['theta'][t_compare,:,:]

# File 2:
dens2 = rootgrp2.variables['dens'][t_compare,:,:]
uwnd2 = rootgrp2.variables['uwnd'][t_compare,:,:]
wwnd2 = rootgrp2.variables['wwnd'][t_compare,:,:]
theta2 = rootgrp2.variables['theta'][t_compare,:,:]

# Compare "dens":
print(" ")
print("** Density **")
temp1 = abs(numpy.amax(dens1))
temp2 = abs(numpy.amax(dens2))
temp3 = numpy.amax(dens1 - dens2)
temp4 = (temp3/temp1)*100.0
temp5 = (temp3/temp2)*100.0
print("Max Absolute Value in File 1 = ",temp1)
print("Max Absolute Value in File 2 = ",temp2)
print("Largest Difference between files = ",temp3)
print("  File 1 Difference Percentage of Max Value = ",temp4," %")
print("  File 2 Difference Percentage of Max Value = ",temp5," %")

# Compare "uwnd":
print(" ");
print("** U Wind **")
temp1 = abs(numpy.amax(uwnd1))
temp2 = abs(numpy.amax(uwnd2))
temp3 = numpy.amax(uwnd1 - uwnd2)
temp4 = (temp3/temp1)*100.0
temp5 = (temp3/temp2)*100.0
print("Max Absolute Value in File 1 = ",temp1)
print("Max Absolute Value in File 2 = ",temp2)
print("Largest Difference between files = ",temp3)
print("  File 1 Difference Percentage of Max Value = ",temp4," %")
print("  File 2 Difference Percentage of Max Value = ",temp5," %")

# Compare "wwnd":
print(" ");
print("** W Wind **")
temp1 = abs(numpy.amax(wwnd1))
temp2 = abs(numpy.amax(wwnd2))
temp3 = numpy.amax(wwnd1 - wwnd2)
temp4 = (temp3/temp1)*100.0
temp5 = (temp3/temp2)*100.0
print("Max Absolute Value in File 1 = ",temp1)
print("Max Absolute Value in File 2 = ",temp2)
print("Largest Difference between files = ",temp3)
print("  File 1 Difference Percentage of Max Value = ",temp4," %")
print("  File 2 Difference Percentage of Max Value = ",temp5," %")

# Compare "theta":
print(" ");
print("** Theta **")
temp1 = abs(numpy.amax(theta1))
temp2 = abs(numpy.amax(theta2))
temp3 = numpy.amax(theta1 - theta2)
temp4 = (temp3/temp1)*100.0
temp5 = (temp3/temp2)*100.0
print("Max Absolute Value in File 1 = ",temp1)
print("Max Absolute Value in File 2 = ",temp2)
print("Largest Difference between files = ",temp3)
print("  File 1 Difference Percentage of Max Value = ",temp4," %")
print("  File 2 Difference Percentage of Max Value = ",temp5," %")



exit()

