# Import Packages
import numpy as np
import matplotlib.pyplot as plt

# Declare X-axis
degree_list = np.arange(0, 721) # This is "x". range from 0 to 720

# Draw Diagrams
plt.figure(figsize=(12,8))
plt.plot(degree_list, np.sin(np.deg2rad(degree_list)), label="y1") # y1=sin(x)
plt.plot(degree_list, np.cos(np.deg2rad(degree_list)), label="y2") # y2=cos(x)
plt.plot(degree_list, np.sin(np.deg2rad(2 * degree_list)), label="y3") # y3=sin(2x)
plt.plot(degree_list, np.sin(np.deg2rad(1/2 * degree_list)), label="y4") # y4=sin(x/2)
plt.plot(degree_list, 0.5 * np.sin(np.deg2rad(degree_list-15)), label="y5") # y5=0.5sin(x-15)
plt.title("sin & cos functions", fontsize=20) # define title
plt.ylabel("Values", fontsize=18) # define vertical text
plt.xlabel("Degree", fontsize=18) # define horizontal text
plt.yticks(np.arange(-1.0,1.25, step=0.25), fontsize=14) # set y-ticks
plt.xticks(np.arange(0, 721, step=60), fontsize=14) # set x-ticks, each 60 degree has one degree
plt.legend(fontsize=18) # show legend
plt.show() # show the whole image