#Python Crash Course Chapter 15 Generating Data
#Data visualization involves exploring data through visual representations. It’s closely associated with data mining, which uses code to explore the patterns and connections in a data set.

import matplotlib.pyplot as plt

inputvalues = [1, 2, 3, 4, 5] #When you give plot() a sequence of numbers, it assumes the first data point corresponds to an x-coordinate value of 0, but our first point corresponds to an x-value of 1. We can override the default behavior by giving plot() both the input and output values used to calculate the squares
squares = [1, 4, 9, 16, 25]
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)
plt.tick_params(axis="both", labelsize = 14)
plt.plot(squares) #can plot more than one line in a chart
plt.plot(inputvalues, squares, linewidth = 5)
plt.show()
#To plot a single point, use the scatter() function. Pass the single (x, y) values of the point of interest to scatter().
plt.scatter(2, 4, s = 200) #s is size of dots
plt.show()
#To plot a series of points, we can pass scatter() separate lists of x- and y-values.  No line connecting the points.  Points only.
xvalues = [1, 2, 3, 4, 5]
yvalues = [1, 4, 9, 16, 25]
plt.scatter(xvalues, yvalues, s = 100)
plt.show()
#Let’s use a loop in Python to do the calculations for us. Here’s how this would look with 1000 points.
xvalues1000 = list(range(1, 1001))
yvalues1000 = [x**2 for x in xvalues1000]
plt.scatter(xvalues1000, yvalues1000, s=40) #default is blue dots with a black outline
plt.scatter(xvalues1000, yvalues1000, c="red", edgecolor="none", s=40) #remove onlines around points set edgecolor = "none". Set color of points or dots c="red" or c=(R, G, B) values between 0 and 1.
plt.scatter(xvalues1000, yvalues1000, c=yvalues1000, cmap=plt.cm.Blues, edgecolor="none", s=40) #A colormap is a series of colors in a gradient that moves from a starting to ending color. Colormaps are used in visualizations to emphasize a pattern in the data. For example, you might make low values a light color and high values a darker color.  Here’s how to assign each point a color based on its y-value in blue.
#You can see all the colormaps available in pyplot at http://matplotlib.org/; go to Examples, scroll down to Color Examples, and click colormaps_reference.  Specifically, http://matplotlib.org/examples/color/colormaps_reference.html.
plt.axis([0, 1100, 0, 1100000]) #the axis() function to specify the range of each axis w. Requires four values: the minimum and maximum values for the x-axis and the y-axis. Here, we run the x-axis from 0 to 1100 and the y-axis from 0 to 1,100,000.
plt.show()
#If you want your program to automatically save the plot to a file, you can replace the call to plt.show() with a call to plt.savefig().  File saved in same directory of python file.
plt.savefig('squares_plot.png', bbox_inches='tight') #bbox_inches trims extra whitespace from the plot. If you want the extra whitespace around the plot, you can omit bbox_inches.

xvaluescube = list(range(1, 5001))
yvaluescube = [x**3 for x in xvaluescube]
plt.axis([0, 5100, 0, 126000000000])
plt.scatter(xvaluescube, yvaluescube, c=yvaluescube, cmap=plt.cm.Reds, edgecolor="none", s=30)
plt.show()
#Start page 331